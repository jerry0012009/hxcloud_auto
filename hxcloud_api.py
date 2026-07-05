#!/usr/bin/env python3
"""
华心云 (HXCloud) API 工具库
用法: from hxcloud_api import HXCloud
"""

import requests
import json
from datetime import datetime


class HXCloud:
    """华心云 API 客户端"""
    
    BASE_URL = "http://jerrypsy.top:8105/admin-api"
    TENANT_NAME = "西华大学"
    TENANT_ID = 163
    
    def __init__(self, username="0720200029", password="Admin.123456"):
        self.username = username
        self.password = password
        self.token = None
        self.user_id = None
        self.user_info = None
        self.session = requests.Session()
        self.session.headers.update({"tenant-id": str(self.TENANT_ID)})
    
    def login(self):
        """登录并获取Token"""
        resp = self.session.post(f"{self.BASE_URL}/system/auth/login", json={
            "username": self.username,
            "password": self.password
        })
        data = resp.json()
        if data["code"] != 0:
            raise Exception(f"登录失败: {data['msg']}")
        
        self.token = data["data"]["accessToken"]
        self.user_id = data["data"]["userId"]
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        })
        
        # 获取用户信息
        info = self.get_user_info()
        self.user_info = info
        return data["data"]
    
    def get_user_info(self):
        """获取用户权限信息"""
        resp = self.session.get(f"{self.BASE_URL}/system/auth/get-permission-info")
        return resp.json()["data"]
    
    def _get(self, path, params=None):
        """GET请求"""
        resp = self.session.get(f"{self.BASE_URL}{path}", params=params)
        return resp.json()
    
    def _post(self, path, data=None):
        """POST请求"""
        resp = self.session.post(f"{self.BASE_URL}{path}", json=data)
        return resp.json()
    
    # ==================== 月报管理 ====================
    
    def get_month_records(self, page_no=1, page_size=10, status=None):
        """获取月报列表"""
        params = {"pageNo": page_no, "pageSize": page_size}
        if status:
            params["psmMonthRecordStatus"] = status
        return self._get("/psm/month-record/page", params)
    
    def get_month_record(self, record_id):
        """获取单条月报"""
        return self._get("/psm/month-record/get", {"id": record_id})
    
    def get_month_details(self, month_record_id, page_no=1, page_size=100,
                          status=None, counselor_id=None, student_name=None):
        """获取月报详情列表"""
        params = {
            "monthRecordId": month_record_id,
            "pageNo": page_no,
            "pageSize": page_size
        }
        if status:
            params["monthRecordDetailStatus"] = status
        if counselor_id:
            params["belongCounselorId"] = counselor_id
        if student_name:
            params["studentName"] = student_name
        return self._get("/psm/month-record-detail/page", params)
    
    def get_month_detail(self, detail_id):
        """获取单条月报详情"""
        return self._get("/psm/month-record-detail/get", {"id": detail_id})
    
    def counselor_confirm(self, detail_id, counselor_measure):
        """
        咨询师确认月报详情
        自动获取原始记录并更新 counselorMeasure 字段
        """
        # 1. 获取原始记录
        record = self.get_month_detail(detail_id)["data"]
        if not record:
            raise Exception(f"记录不存在: {detail_id}")
        
        # 2. 更新咨询师措施
        record["counselorMeasure"] = counselor_measure
        
        # 3. 提交
        return self._post("/psm/month-record-detail/updateByCounselor", record)
    
    def batch_counselor_confirm(self, month_record_id, counselor_id, 
                                  measure_map, dry_run=False):
        """
        批量咨询师确认
        measure_map: {detail_id: "咨询师措施内容", ...}
                     或 callable: fn(record) -> str
        """
        results = []
        
        # 获取待确认列表
        if isinstance(measure_map, dict):
            detail_ids = list(measure_map.keys())
        else:
            # measure_map is callable, get all pending records
            resp = self.get_month_details(
                month_record_id, 
                status="counselor_collect",
                counselor_id=counselor_id,
                page_size=500
            )
            detail_ids = [r["id"] for r in resp["data"]["list"]]
        
        for did in detail_ids:
            record = self.get_month_detail(did)["data"]
            
            if callable(measure_map):
                measure = measure_map(record)
            else:
                measure = measure_map[did]
            
            record["counselorMeasure"] = measure
            
            if dry_run:
                results.append({"id": did, "student": record["studentName"], 
                               "measure": measure, "status": "dry_run"})
            else:
                resp = self._post("/psm/month-record-detail/updateByCounselor", record)
                results.append({"id": did, "student": record["studentName"],
                               "measure": measure, "result": resp})
        
        return results
    
    # ==================== 咨询记录 ====================
    
    def get_consult_records(self, page_no=1, page_size=10, **kwargs):
        """获取咨询记录列表"""
        params = {"pageNo": page_no, "pageSize": page_size}
        params.update(kwargs)
        return self._get("/psa/consult-record/page", params)
    
    def get_consult_record(self, record_id):
        """获取单条咨询记录"""
        return self._get("/psa/consult-record/get", {"id": record_id})
    
    def get_consult_view(self, page_no=1, page_size=10, **kwargs):
        """获取咨询视图（联合查询，含学生和预约信息）"""
        params = {"pageNo": page_no, "pageSize": page_size}
        params.update(kwargs)
        return self._get("/psa/consult-view/page", params)
    
    def create_consult_record(self, data):
        """创建咨询记录"""
        return self._post("/psa/consult-record/create", data)
    
    def update_consult_record(self, data):
        """更新咨询记录"""
        return self._post("/psa/consult-record/update", data)
    
    # ==================== 访谈记录 ====================
    
    def get_interview_records(self, page_no=1, page_size=10, **kwargs):
        """获取访谈记录列表"""
        params = {"pageNo": page_no, "pageSize": page_size}
        params.update(kwargs)
        return self._get("/psy/interview-record/page", params)
    
    def get_my_interview_records(self, page_no=1, page_size=10):
        """获取我的访谈记录"""
        return self._get("/psy/interview-record/page_my", {
            "pageNo": page_no, "pageSize": page_size
        })
    
    def get_interview_templates(self, page_no=1, page_size=10):
        """获取访谈模板列表"""
        return self._get("/psy/interview-template/page", {
            "pageNo": page_no, "pageSize": page_size
        })
    
    # ==================== 排班管理 ====================
    
    def get_schedule_standards(self, page_no=1, page_size=50):
        """获取排班标准列表"""
        return self._get("/psa/schedule-standard/page", {
            "pageNo": page_no, "pageSize": page_size
        })


def format_timestamp(ts):
    """时间戳转可读格式"""
    if not ts:
        return "N/A"
    return datetime.fromtimestamp(ts / 1000).strftime("%Y-%m-%d %H:%M:%S")


def format_record(record):
    """格式化月报详情记录为可读文本"""
    lines = [
        f"学生: {record.get('studentName')} ({record.get('studentCode')})",
        f"学院: {record.get('studentDeptName')}",
        f"专业: {record.get('studentMajorName')} {record.get('studentClassName')}",
        f"状态: {record.get('monthRecordDetailStatus')}",
        f"学生情况: {record.get('studentDesc', 'N/A')}",
        f"目前措施: {record.get('currentMeasure', 'N/A')}",
        f"辅导员措施: {record.get('instructorMeasure', 'N/A')}",
        f"咨询师措施: {record.get('counselorMeasure', 'N/A')}",
        f"危机等级: {record.get('crisisLevel', 'N/A')}",
        f"精神科诊断: {record.get('psychiatricDiagnosis', 'N/A')}",
        f"用药情况: {record.get('medicationStatus', 'N/A')}",
        f"咨询师确认时间: {format_timestamp(record.get('counselorCollectTime'))}",
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    # 快速测试
    hx = HXCloud()
    hx.login()
    print(f"✅ 登录成功: {hx.user_info['user']['nickname']}")
    
    # 查看最新月报
    records = hx.get_month_records(page_size=3)
    print(f"\n📋 最近月报:")
    for r in records["data"]["list"]:
        print(f"  [{r['id']}] {r['monthName']} - {r['psmMonthRecordStatus']}")
    
    # 查看待确认的详情
    latest_id = records["data"]["list"][0]["id"]
    details = hx.get_month_details(
        latest_id, 
        status="counselor_collect",
        counselor_id=155,
        page_size=5
    )
    print(f"\n📋 待咨询师确认的记录 (月报ID={latest_id}):")
    for d in details["data"]["list"]:
        print(f"  [{d['id']}] {d['studentName']} ({d['studentCode']}) - {d['studentDeptName']}")
