# 华心云 - 月报管理 API (psm/)

## 概述
月报管理是心理咨询中心对重点关注学生的月度跟踪记录。流程为：
1. 管理员创建月报 → 系统自动为每个关注学生生成月报详情
2. **辅导员先填写** (`instructor_collect` 状态) → 填写 `instructorMeasure` 等字段
3. **咨询师确认** (`counselor_collect` 状态) → 填写 `counselorMeasure` 等字段 → 状态变为 `done`
4. 管理员汇总收集 (`collecting` → `done`)

## ⚠️ 操作红线：明细确认 ≠ 整条月报完成

- `monthRecordDetailStatus` 是学生明细状态：`instructor_collect` / `counselor_collect` / `done`。
- `psmMonthRecordStatus` 是整条月报主表状态：`collecting` / `done`。
- 咨询师批量确认只调用 `/psm/month-record-detail/updateByCounselor`，处理的是学生明细。
- `/psm/month-record/collectRecord?id=` 会把整条月报主表标记为完成，并写入 `collectTime`、`collectName`。除非用户明确要求“提交整条月报/标记整条月报完成”，脚本和助手都禁止调用。
- 已实测：`PUT /psm/month-record/update` 返回成功也不会把主表从 `done` 恢复为 `collecting`；前端打包 API 也没有撤销接口。误操作后一般需要数据库或后端服务端修复。

## API 端点列表

### 月报记录 (month-record)
| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/psm/month-record/page` | 分页查询月报列表 |
| GET | `/psm/month-record/get?id=` | 获取单条月报 |
| POST | `/psm/month-record/collectRecord?id=` | ⚠️ 整条月报收集完成，禁止自动调用 |

### 月报详情 (month-record-detail) — ⭐ 核心
| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/psm/month-record-detail/page` | 分页查询月报详情列表 |
| GET | `/psm/month-record-detail/get?id=` | 获取单条月报详情 |
| POST | `/psm/month-record-detail/create` | 创建月报详情 |
| POST | `/psm/month-record-detail/updateByCounselor` | ⭐ **咨询师确认** |
| POST | `/psm/month-record-detail/updateByInstructor` | 辅导员填写 |
| GET | `/psm/month-record-detail/reset?id=` | 重置月报详情 |
| GET | `/psm/month-record-detail/delete?id=` | 删除月报详情 |
| GET | `/psm/month-record-detail/export-excel` | 导出Excel |

---

## 1. 月报列表

```bash
curl -s 'http://jerrypsy.top:8105/admin-api/psm/month-record/page?pageNo=1&pageSize=10' \
  -H 'Authorization: Bearer <token>' \
  -H 'tenant-id: 163'
```

### 查询参数
| 参数 | 类型 | 说明 |
|------|------|------|
| pageNo | int | 页码 |
| pageSize | int | 每页条数 |
| psmMonthRecordStatus | string | 状态过滤：`collecting`(采集中), `done`(已完成) |

### 返回示例
```json
{
  "code": 0,
  "data": {
    "total": 10,
    "list": [
      {
        "id": 73,
        "monthName": "2026年6月心理月报（0629）",
        "deadDate": "2026-07-06",
        "total": 1183,
        "instructorCount": 80,
        "counselorCount": 512,
        "psmMonthRecordStatus": "collecting",
        "collectTime": null,
        "collectName": null
      }
    ]
  }
}
```

### 字段说明
| 字段 | 说明 |
|------|------|
| id | 月报ID |
| monthName | 月报名称 |
| deadDate | 截止日期 |
| total | 学生总数 |
| instructorCount | 辅导员已填写数 |
| counselorCount | 咨询师已确认数 |
| psmMonthRecordStatus | 状态 (`collecting`/`done`) |

---

## 2. ⭐ 月报详情列表（核心查询接口）

```bash
curl -s 'http://jerrypsy.top:8105/admin-api/psm/month-record-detail/page?monthRecordId=73&pageNo=1&pageSize=10' \
  -H 'Authorization: Bearer <token>' \
  -H 'tenant-id: 163'
```

### 查询参数
| 参数 | 类型 | 说明 |
|------|------|------|
| monthRecordId | int | **必填** - 月报ID |
| pageNo | int | 页码 |
| pageSize | int | 每页条数 |
| monthRecordDetailStatus | string | 状态过滤 |
| belongCounselorId | int | 咨询师ID过滤（如155=王中瑞） |
| studentName | string | 学生姓名 |
| studentCode | string | 学号 |

### 返回数据结构（完整字段）
```json
{
  "id": 17243,
  "monthRecordId": 73,
  "studentId": 108341,
  "studentName": "胡益杨",
  "studentCode": "3120244871130",
  "studentDeptId": 133,
  "studentDeptName": "航空航天与智能装备学院",
  "studentDistrictCode": "pidu",
  "studentGradeCode": "2024",
  "studentCultivationLevel": "benke",
  "studentMajorId": 2429,
  "studentMajorName": "航空航天类",
  "studentClassId": 1750,
  "studentClassName": "航天类24-1",
  "studentGender": "2",
  "focusReasonType": "xueye",
  "healthType": "lianghao",
  "learningStatus": "zhongdeng",
  "roommateStatus": "rongqia",
  "homeStatus": "hexie",
  "growthStatus": "fumu",
  "homeEconomyStatus": "zhongdeng",
  "majorChangeDesc": null,
  "studentDesc": "1.6月25日，学生告知存在心理疾病...",
  "suicideInjuryRiskType": "none",
  "crisisLevel": "none",
  "currentMeasure": "1.安排学生党员针对性学业帮扶\n2.告知家长学生心理状态变化",
  "counselorMeasure": null,
  "instructorMeasure": "无",
  "studentJournalLog": null,
  "monthRecordDetailStatus": "counselor_collect",
  "instructorCollectTime": 1782719356000,
  "instructorCollectName": null,
  "counselorCollectTime": null,
  "counselorCollectName": "王中瑞",
  "instructorRemoveStatus": "putong",
  "removeReasonType": null,
  "removeReasonDesc": null,
  "fileUrlOut": null,
  "focusId": 3712,
  "belongCounselorId": 155,
  "belongInstructorId": 110990,
  "belongCounselorName": "王中瑞",
  "belongInstructorName": "唐承邦",
  "psychiatricDiagnosis": "sleep",
  "medicationStatus": "under",
  "familyStructure": "wanzheng",
  "crisisPlanLevel": "three",
  "instructorHandlingMethod": "level5"
}
```

### 关键字段说明
| 字段 | 说明 | 可编辑角色 |
|------|------|-----------|
| monthRecordDetailStatus | 状态 | 系统自动流转 |
| studentDesc | 学生情况描述 | 辅导员 |
| currentMeasure | 目前采取措施 | 辅导员/咨询师 |
| instructorMeasure | 辅导员措施 | 辅导员 |
| counselorMeasure | 咨询师措施 | **咨询师** ⭐ |
| crisisLevel | 危机等级 | 辅导员 |
| psychiatricDiagnosis | 精神科诊断 | 辅导员 |
| medicationStatus | 用药情况 | 辅导员 |
| familyStructure | 家庭结构 | 辅导员 |
| crisisPlanLevel | 危机预案等级 | 辅导员 |
| instructorHandlingMethod | 辅导员处理方式 | 辅导员 |
| instructorRemoveStatus | 是否移除关注 | 辅导员 |
| belongCounselorId | 归属咨询师ID | 系统 |
| belongInstructorId | 归属辅导员ID | 系统 |

---

## 3. ⭐ 咨询师确认（updateByCounselor）— 关键操作

### 请求
```bash
curl -s -X POST 'http://jerrypsy.top:8105/admin-api/psm/month-record-detail/updateByCounselor' \
  -H 'Authorization: Bearer <token>' \
  -H 'tenant-id: 163' \
  -H 'Content-Type: application/json' \
  -d '{
    "id": 17238,
    "monthRecordId": 73,
    "studentId": 103530,
    "studentDeptId": 134,
    "counselorMeasure": "学生近期状态稳定，学业帮扶已安排，继续保持关注",
    "currentMeasure": "保持关注",
    "crisisPlanLevel": "three",
    ... (其他原始字段保持不变)
  }'
```

### ⚠️ 必填字段
更新时**必须传回原始记录的完整数据**（先GET再PUT），至少以下字段不能为空：
- `id` - 记录ID
- `monthRecordId` - 月报ID
- `studentId` - 学生ID
- `studentDeptId` - 学生部门ID
- `currentMeasure` - 目前采取措施
- `crisisPlanLevel` - 危机预案等级
- `counselorMeasure` - 咨询师措施（**这是咨询师要填写的核心字段**）

### 推荐流程
```python
# 1. 获取原始记录
record = GET /psm/month-record-detail/get?id=17238

# 2. 修改咨询师相关字段
record['counselorMeasure'] = "新的咨询师措施内容"

# 3. 提交更新
POST /psm/month-record-detail/updateByCounselor (body=record)
```

### 成功返回
```json
{"code": 0, "msg": "", "data": true}
```

### 状态流转
```
counselor_collect (待咨询师确认)
    ↓ updateByCounselor
instructor_collect (待辅导员确认) 或 done (完成)
```

> **实测**: 咨询师确认后，状态直接变为 `done`（可能是因为辅导员已先填写）

---

## 4. 辅导员填写（updateByInstructor）

```bash
curl -s -X POST 'http://jerrypsy.top:8105/admin-api/psm/month-record-detail/updateByInstructor' \
  -H 'Authorization: Bearer <token>' \
  -H 'tenant-id: 163' \
  -H 'Content-Type: application/json' \
  -d '{
    "id": 17238,
    "instructorMeasure": "辅导员措施内容...",
    ... (其他字段)
  }'
```

---

## 5. 重置月报详情

```bash
curl -s 'http://jerrypsy.top:8105/admin-api/psm/month-record-detail/reset?id=17238' \
  -H 'Authorization: Bearer <token>' \
  -H 'tenant-id: 163'
```

---

## 自动化场景

### 场景1: 批量查询待确认的月报详情
```bash
# 查询咨询师(王中瑞, ID=155)待确认的所有记录
curl -s 'http://jerrypsy.top:8105/admin-api/psm/month-record-detail/page?monthRecordId=73&monthRecordDetailStatus=counselor_collect&belongCounselorId=155&pageNo=1&pageSize=100' \
  -H 'Authorization: Bearer <token>' \
  -H 'tenant-id: 163'
```

### 场景2: 自动化批量确认
```python
import requests

BASE = "http://jerrypsy.top:8105/admin-api"
HEADERS = {"Authorization": f"Bearer {token}", "tenant-id": "163"}

# 获取待确认列表
resp = requests.get(f"{BASE}/psm/month-record-detail/page",
    params={"monthRecordId": 73, "monthRecordDetailStatus": "counselor_collect",
            "belongCounselorId": 155, "pageNo": 1, "pageSize": 100},
    headers=HEADERS)

for record in resp.json()['data']['list']:
    # 根据学生情况填写咨询师措施
    record['counselorMeasure'] = generate_measure(record)  # 自定义逻辑
    
    # 提交确认
    requests.post(f"{BASE}/psm/month-record-detail/updateByCounselor",
        json=record, headers=HEADERS)

# 注意：到这里就结束。不要调用 /psm/month-record/collectRecord。
# collectRecord 是整条月报主表“收集完成”，必须由用户明确授权后才可执行。
```
