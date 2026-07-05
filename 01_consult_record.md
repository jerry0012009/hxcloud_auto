# 华心云 - 咨询记录 API (psa/consult-record)

## 概述
咨询记录是咨询师完成咨询后填写的记录，包含主观记录(SOAP格式)、风险评估、干预建议等。

## API 端点列表

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/psa/consult-record/page` | 分页查询咨询记录列表 |
| GET | `/psa/consult-record/get?id=` | 获取单条咨询记录详情 |
| GET | `/psa/consult-record/getConsultRecordByAppointId?appointRecordId=` | 根据预约ID查询咨询记录 |
| POST | `/psa/consult-record/create` | 创建咨询记录 |
| POST | `/psa/consult-record/createEmergencyConsultRecord` | 创建紧急咨询记录 |
| POST | `/psa/consult-record/update` | 更新咨询记录 |
| GET | `/psa/consult-record/delete?id=` | 删除咨询记录 |
| GET | `/psa/consult-record/export-excel` | 导出Excel |

---

## 1. 分页查询咨询记录

```bash
curl -s 'http://jerrypsy.top:8105/admin-api/psa/consult-record/page?pageNo=1&pageSize=10' \
  -H 'Authorization: Bearer <token>' \
  -H 'tenant-id: 163'
```

### 查询参数
| 参数 | 类型 | 说明 |
|------|------|------|
| pageNo | int | 页码（从1开始） |
| pageSize | int | 每页条数 |
| consultingQuestionType | string | 咨询问题类型（如 `xinli`） |
| riskType | string | 风险类型 |
| filingDate | string | 归档日期范围 |
| subjectiveRecord | string | 主观记录（模糊搜索） |
| objectiveRecord | string | 客观记录（模糊搜索） |
| visitCode | string | 来访编号 |
| keyDesc | string | 关键字描述 |

### 返回数据结构
```json
{
  "code": 0,
  "msg": "",
  "data": {
    "total": 1834,
    "list": [
      {
        "id": 1612,
        "appointId": 1661,
        "consultingQuestionType": "xinli",
        "subjectiveRecord": "主观记录（Subjective）：\n来访者在咨询过程中提到了...",
        "objectiveRecord": null,
        "filingDate": null,
        "visitCode": null,
        "keyDesc": null,
        "riskType": "wufengxian",
        "noComingReason": null,
        "consultRecordStatus": "wancheng",
        "remark": null,
        "filepath": null,
        "type": "geti",
        "suggestion": null
      }
    ]
  }
}
```

### 字段说明
| 字段 | 类型 | 说明 |
|------|------|------|
| id | int | 记录ID |
| appointId | int | 关联的预约记录ID |
| consultingQuestionType | string | 咨询问题类型 (`xinli`=心理) |
| subjectiveRecord | string | 主观记录 - S (SOAP中的S) |
| objectiveRecord | string | 客观记录 - O (SOAP中的O) |
| riskType | string | 风险等级 (`wufengxian`=无风险) |
| consultRecordStatus | string | 记录状态 (`wancheng`=完成) |
| type | string | 类型 (`geti`=个体) |
| suggestion | string | 建议 - P (SOAP中的P) |
| visitCode | string | 来访编号 |
| keyDesc | string | 关键描述 |
| filepath | string | 附件路径 |
| remark | string | 备注 |

---

## 2. 获取单条咨询记录

```bash
curl -s 'http://jerrypsy.top:8105/admin-api/psa/consult-record/get?id=1612' \
  -H 'Authorization: Bearer <token>' \
  -H 'tenant-id: 163'
```

---

## 3. 根据预约ID查询咨询记录

```bash
curl -s 'http://jerrypsy.top:8105/admin-api/psa/consult-record/getConsultRecordByAppointId?appointRecordId=1661' \
  -H 'Authorization: Bearer <token>' \
  -H 'tenant-id: 163'
```

---

## 4. 创建咨询记录

```bash
curl -s -X POST 'http://jerrypsy.top:8105/admin-api/psa/consult-record/create' \
  -H 'Authorization: Bearer <token>' \
  -H 'tenant-id: 163' \
  -H 'Content-Type: application/json' \
  -d '{
    "appointId": 1661,
    "consultingQuestionType": "xinli",
    "subjectiveRecord": "主观记录内容...",
    "objectiveRecord": "客观记录内容...",
    "riskType": "wufengxian",
    "type": "geti",
    "suggestion": "建议内容..."
  }'
```

---

## 5. 更新咨询记录

```bash
curl -s -X POST 'http://jerrypsy.top:8105/admin-api/psa/consult-record/update' \
  -H 'Authorization: Bearer <token>' \
  -H 'tenant-id: 163' \
  -H 'Content-Type: application/json' \
  -d '{
    "id": 1612,
    "appointId": 1661,
    "subjectiveRecord": "更新后的主观记录...",
    "riskType": "wufengxian"
  }'
```

---

## SOAP 记录格式说明
咨询记录采用 SOAP 格式：
- **S (Subjective):** 主观记录 - 来访者自述
- **O (Objective):** 客观记录 - 咨询师观察
- **A (Assessment):** 风险评估 - 通过 `riskType` 字段
- **P (Plan):** 干预建议 - 通过 `suggestion` 字段

---

## 关联关系
```
预约记录 (psa/schedule-record)
  ↓ appointId
咨询记录 (psa/consult-record)
  ↓ studentId
学生信息 (psc/student)
```

## 与 consult-view 的关系
`/psa/consult-view/page` 是一个**联合查询视图**，将预约记录和咨询记录合并展示，包含学生信息、预约信息和咨询记录。返回字段更丰富，适合列表展示。

```bash
curl -s 'http://jerrypsy.top:8105/admin-api/psa/consult-view/page?pageNo=1&pageSize=10' \
  -H 'Authorization: Bearer <token>' \
  -H 'tenant-id: 163'
```

返回的额外字段包括:
- `scheduleRecordId`, `roomId`, `roomName` (咨询室)
- `studentName`, `studentCode`, `studentDeptName` (学生信息)
- `counselorName`, `counselorId` (咨询师)
- `actualDate`, `startTime`, `endTime`, `duringTimeMin` (时间)
- `appointRecordStatus`, `appointRecordStyle` (预约状态)
- `subjectiveRecord`, `riskType`, `consultRecordStatus` (咨询记录)
