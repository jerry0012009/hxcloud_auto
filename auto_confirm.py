#!/usr/bin/env python3
"""
月报咨询师确认 - 自动化脚本
策略：
1. 有历史记录 → 回填上次内容（77条）
2. 辅导员建议移除 → 直接同意（27条）
3. 无历史+非移除 → AI按规则生成（10条）
"""

import sys, json
sys.path.insert(0, '/root/jerry/HXCloud')
from hxcloud_api import HXCloud

DIAG_LABELS = {
    'dep': '抑郁', 'anx': '焦虑', 'sleep': '睡眠障碍',
    'ocd': '强迫', 'ptsd': 'PTSD', 'bipolar': '双相情感障碍',
    'psy': '精神分裂症', 'person': '人格障碍', 'others': '心理健康'
}

def get_diag_label(diag):
    return DIAG_LABELS.get(diag, '心理健康')

def generate_measure(rec):
    """根据学生信息生成咨询师措施"""
    crisis = rec.get('crisisPlanLevel', '')
    risk = rec.get('suicideInjuryRiskType', '')
    diag = rec.get('psychiatricDiagnosis', '')
    med = rec.get('medicationStatus', '')
    desc = rec.get('studentDesc', '') or ''

    parts = []

    if crisis == 'one':
        if risk in ('changshi', 'harm', 'harmaction', 'recentplan'):
            parts.append("注意评估是否有伤害自己和他人风险（如有明确的计划与尝试，需要突破保密移交监护权，由家长看护），及时调整危机风险等级，或通知家长与学校相关人员。建议该同学心理咨询。")
        else:
            parts.append("密切关注，遵医嘱治疗，建议在规律服药基础上，寻求校内外心理咨询配合。")
    elif crisis == 'two':
        if risk in ('recentidea', 'recentthought', 'recentplan'):
            parts.append("确认该同学目前情绪状态，是否自伤或伤人想法，如有相关风险需要通知并向家长建议继续遵医嘱治疗，或考虑移交家长监护，如无异常情况请继续保持关注。")
        else:
            parts.append("同意通知家长和学校相关人员，委托同学关注动态，鼓励来中心咨询。")
        if diag not in ('none', 'todo', None) and med == 'under':
            parts.append("建议遵医嘱治疗。")
    else:
        if diag not in ('none', 'todo', None):
            if med == 'tingyao':
                parts.append("保持关注，注意评估是否有伤害自己和他人风险，建议该同学遵医嘱服药，鼓励预约心理咨询中心咨询。")
            elif med == 'under':
                parts.append("保持关注，建议规律去精神科复诊，建议寻求心理咨询。")
            elif med == 'yizhu':
                parts.append(f"保持关注，提供关于{get_diag_label(diag)}的心理知识，鼓励预约心理咨询中心咨询。")
            else:
                parts.append(f"保持关注，提供关于{get_diag_label(diag)}的心理知识，鼓励精神科就诊，鼓励预约心理咨询中心咨询。")
        elif risk in ('recentidea', 'recentthought'):
            parts.append("保持关注生活中可能的突发事件，及时提供必要的支持，定期评估是否存在自伤风险，鼓励来心理中心咨询。")
        elif '挂科' in desc or '学业' in desc:
            parts.append("保持关注，跟进学业成绩，有挂科情况约谈交流，鼓励来心理中心咨询。")
        elif '宿舍' in desc or '舍友' in desc or '寝室' in desc:
            parts.append("保持关注与舍友关系，与生活中可能的突发事件，及时提供必要的支持，鼓励来心理中心咨询。")
        else:
            parts.append("保持关注，提供必要的支持，鼓励来心理中心咨询。")

    if diag == 'todo' or med == 'todo':
        parts.append("请补充该同学精神科诊断后的信息，目前是否正常上学，是否存在自杀或伤害他人的想法或计划。")

    return " ".join(parts)


def main():
    hx = HXCloud()
    hx.login()
    name = hx.user_info['user']['nickname']
    print(f"登录成功: {name}")

    # 1. 构建历史记录库: studentId -> last counselorMeasure
    student_last_measure = {}
    for mid in [69, 70, 71, 73]:
        resp = hx.get_month_details(mid, status="done", counselor_id=155, page_size=200)
        for r in resp['data']['list']:
            sid = r['studentId']
            if r.get('counselorMeasure'):
                if sid not in student_last_measure or r['monthRecordId'] > student_last_measure[sid]['monthRecordId']:
                    student_last_measure[sid] = r

    print(f"历史记录库: {len(student_last_measure)} 个学生")

    # 2. 获取待确认列表
    month_id = 73
    pending = []
    for page in range(1, 10):
        resp = hx.get_month_details(month_id, status="counselor_collect",
                                     counselor_id=155, page_no=page, page_size=50)
        batch = resp['data']['list']
        pending.extend(batch)
        if len(batch) < 50:
            break

    print(f"待确认: {len(pending)} 条")

    # 3. 分类处理
    results = {"history": 0, "remove": 0, "generated": 0, "fail": 0}

    for rec in pending:
        rid = rec['id']
        sid = rec['studentId']
        sname = rec['studentName']
        remove_status = rec.get('instructorRemoveStatus', '')

        # 策略1: 辅导员建议移除 → 同意
        if remove_status == 'jianyi_yichu':
            measure = "同意移除重点关注名单，保持对该同学的正常关注，鼓励自我成长，鼓励预约心理咨询。"
            results["remove"] += 1
            tag = "移除"

        # 策略2: 有历史 → 回填上次内容
        elif sid in student_last_measure:
            measure = student_last_measure[sid].get('counselorMeasure', '')
            results["history"] += 1
            tag = "回填"

        # 策略3: 无历史 → AI规则生成
        else:
            measure = generate_measure(rec)
            results["generated"] += 1
            tag = "生成"

        # 执行确认
        print(f"  [{tag}] {sname} => {measure[:60]}...")
        resp = hx.counselor_confirm(rid, measure)
        if resp.get('code') == 0:
            print(f"    ✅ 成功")
        else:
            print(f"    ❌ 失败: {resp.get('msg','')}")
            results["fail"] += 1

    print(f"\n完成! 回填:{results['history']} 移除:{results['remove']} "
          f"生成:{results['generated']} 失败:{results['fail']}")


if __name__ == "__main__":
    main()
