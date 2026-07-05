# 华心云 (HXCloud) 咨询记录相关 API 文档

> **系统**: 西华大学心理健康管理系统 (华心云)  
> **Base URL**: `http://jerrypsy.top:8105/admin-api`  
> **租户ID**: `163`  
> **认证方式**: Bearer Token  
> **更新日期**: 2026-07-05

---

## 目录

1. [认证接口](#1-认证接口)
2. [访谈记录 (psy:interview-record)](#2-访谈记录-psyinterview-record)
3. [访谈模板 (psy:interview-template)](#3-访谈模板-psyinterview-template)
4. [咨询记录 (psa:consult-record)](#4-咨询记录-psaconsult-record)
5. [咨询视图 (psa:consult-view)](#5-咨询视图-psaconsult-view)
6. [我的来访者 (psy:my-visitor)](#6-我的来访者-psymy-visitor)
7. [关联接口](#7-关联接口)

---

## 1. 认证接口

### 1.1 登录

```bash
curl -X POST http://jerrypsy.top:8105/admin-api/system/auth/login \
  -H 'Content-Type: application/json' \
  -H 'tenant-id: 163' \
  -d '{"username":"0720200029","password":"Admin.123456"}'
```

**响应示例**:
```json
{
    "code": 0,
    "msg": "",
    "data": {
        "userId": 155,
        "accessToken": "7d41210e66684e4dbac9a95a408a8f7e",
        "refreshToken": "25b0b3c758ce44908d6d8bb8b84ba635",
        "expiresTime": 1783257727525,
        "weakPassword": false
    }
}
```

**说明**: 
- `accessToken` 用于后续请求的 `Authorization: Bearer <token>` 头
- `tenant-id: 163` 必须在每个请求的 Header 中携带

---

## 2. 访谈记录 (psy:interview-record)

> **模块说明**: 访谈记录用于记录心理咨询师对学生进行的访谈/面谈内容，通常在心理测评后对学生进行回访。包含学生基本信息、使用的访谈模板、访谈时间、访谈结果详情等。

### 2.1 分页查询访谈记录

```bash
curl -X GET "http://jerrypsy.top:8105/admin-api/psy/interview-record/page?pageNo=1&pageSize=10" \
  -H "Authorization: Bearer 7d41210e66684e4dbac9a95a408a8f7e" \
  -H "tenant-id: 163"
```

**请求参数** (Query Params):

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| pageNo | int | 是 | 页码，从1开始 |
| pageSize | int | 是 | 每页条数 |
| studentName | string | 否 | 学生姓名（模糊查询） |
| studentCode | string | 否 | 学号 |
| interviewTemplateName | string | 否 | 访谈模板名称 |

**响应示例**:
```json
{
    "code": 0,
    "msg": "",
    "data": {
        "total": 242,
        "list": [
            {
                "id": 308,
                "creatorName": "阎思思",
                "createTime": 1766127521000,
                "studentId": 119521,
                "studentName": "相语",
                "studentCode": "9220251692212",
                "studentDeptId": null,
                "studentDeptName": "西华学院",
                "studentDistrictCode": "pidu",
                "studentGradeCode": "2025",
                "studentCultivationLevel": "yuke",
                "studentMajorId": null,
                "studentMajorName": "边防预科",
                "studentClassId": null,
                "studentClassName": "边防预科25",
                "studentGender": "2",
                "interviewTemplateName": "2025新生测评后访谈",
                "interviewTemplateId": 11,
                "interviewTime": "2025-12-11 13:00:00",
                "interviewResultDetails": "<p>访谈结果HTML内容...</p>",
                "remark": null
            }
        ]
    }
}
```

**字段说明**:

| 字段 | 类型 | 说明 |
|------|------|------|
| id | int | 记录ID |
| creatorName | string | 创建者（咨询师）姓名 |
| createTime | long | 创建时间（毫秒时间戳） |
| studentId | int | 学生系统ID |
| studentName | string | 学生姓名 |
| studentCode | string | 学号 |
| studentDeptName | string | 院系名称 |
| studentDistrictCode | string | 校区编码（pidu=郫都） |
| studentGradeCode | string | 年级编码 |
| studentCultivationLevel | string | 培养层次（yuke=预科, benke=本科） |
| studentMajorName | string | 专业名称 |
| studentClassName | string | 班级名称 |
| studentGender | string | 性别（1=男, 2=女） |
| interviewTemplateName | string | 访谈模板名称 |
| interviewTemplateId | int | 访谈模板ID |
| interviewTime | string | 访谈时间（YYYY-MM-DD HH:mm:ss） |
| interviewResultDetails | string | 访谈结果详情（HTML格式） |
| remark | string | 备注 |

### 2.2 查询我的访谈记录

```bash
curl -X GET "http://jerrypsy.top:8105/admin-api/psy/interview-record/page_my?pageNo=1&pageSize=10" \
  -H "Authorization: Bearer 7d41210e66684e4dbac9a95a408a8f7e" \
  -H "tenant-id: 163"
```

**说明**: 仅查询当前登录咨询师创建的访谈记录，参数同 2.1。

### 2.3 获取单条访谈记录

```bash
curl -X GET "http://jerrypsy.top:8105/admin-api/psy/interview-record/get?id=308" \
  -H "Authorization: Bearer 7d41210e66684e4dbac9a95a408a8f7e" \
  -H "tenant-id: 163"
```

**请求参数**:

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| id | int | 是 | 记录ID |

**响应**: `data` 字段为完整的访谈记录对象，结构同 2.1 中 list 的单条记录。

### 2.4 创建访谈记录

```bash
curl -X POST "http://jerrypsy.top:8105/admin-api/psy/interview-record/create" \
  -H "Authorization: Bearer 7d41210e66684e4dbac9a95a408a8f7e" \
  -H "tenant-id: 163" \
  -H "Content-Type: application/json" \
  -d '{
    "studentId": 119521,
    "studentCode": "9220251692212",
    "studentName": "相语",
    "studentDeptName": "西华学院",
    "studentDistrictCode": "pidu",
    "studentGradeCode": "2025",
    "studentCultivationLevel": "yuke",
    "studentMajorName": "边防预科",
    "studentClassName": "边防预科25",
    "studentGender": "2",
    "interviewTemplateId": 11,
    "interviewTemplateName": "2025新生测评后访谈",
    "interviewTime": "2025-12-11 13:00:00",
    "interviewResultDetails": "<p>访谈结果详情HTML</p>",
    "remark": "备注内容"
  }'
```

**请求体字段说明**:

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| studentId | int | 是 | 学生ID（通过选择学生按钮获取） |
| studentCode | string | 是 | 学号 |
| studentName | string | 是 | 学生姓名 |
| studentDeptName | string | 否 | 院系名称 |
| studentDistrictCode | string | 否 | 校区编码 |
| studentGradeCode | string | 否 | 年级编码 |
| studentCultivationLevel | string | 否 | 培养层次 |
| studentMajorName | string | 否 | 专业名称 |
| studentClassName | string | 否 | 班级名称 |
| studentGender | string | 否 | 性别 |
| interviewTemplateId | int | 是 | 访谈模板ID |
| interviewTemplateName | string | 是 | 访谈模板名称 |
| interviewTime | string | 是 | 访谈时间（YYYY-MM-DD HH:mm:ss） |
| interviewResultDetails | string | 是 | 访谈结果详情（HTML） |
| remark | string | 否 | 备注（最多512字） |

**响应**:
```json
{"code": 0, "msg": "", "data": null}
```

### 2.5 更新访谈记录

```bash
curl -X PUT "http://jerrypsy.top:8105/admin-api/psy/interview-record/update" \
  -H "Authorization: Bearer 7d41210e66684e4dbac9a95a408a8f7e" \
  -H "tenant-id: 163" \
  -H "Content-Type: application/json" \
  -d '{
    "id": 308,
    "studentId": 119521,
    "interviewTemplateId": 11,
    "interviewTemplateName": "2025新生测评后访谈",
    "interviewTime": "2025-12-11 14:00:00",
    "interviewResultDetails": "<p>更新后的访谈结果</p>",
    "remark": "更新备注"
  }'
```

**说明**: 请求体需包含 `id` 字段，其余字段同创建接口。

### 2.6 删除访谈记录

```bash
curl -X DELETE "http://jerrypsy.top:8105/admin-api/psy/interview-record/delete?id=308" \
  -H "Authorization: Bearer 7d41210e66684e4dbac9a95a408a8f7e" \
  -H "tenant-id: 163"
```

### 2.7 导出访谈记录

```bash
curl -X GET "http://jerrypsy.top:8105/admin-api/psy/interview-record/export-excel?pageNo=1&pageSize=100" \
  -H "Authorization: Bearer 7d41210e66684e4dbac9a95a408a8f7e" \
  -H "tenant-id: 163" \
  -o interview_records.xlsx
```

---

## 3. 访谈模板 (psy:interview-template)

> **模块说明**: 访谈模板定义了访谈记录的标准化格式，包含模板名称、访谈表单详情（HTML格式的问卷/表单内容）、人员适用范围等。创建访谈记录时需选择一个访谈模板。

### 3.1 分页查询访谈模板

```bash
curl -X GET "http://jerrypsy.top:8105/admin-api/psy/interview-template/page?pageNo=1&pageSize=10" \
  -H "Authorization: Bearer 7d41210e66684e4dbac9a95a408a8f7e" \
  -H "tenant-id: 163"
```

**响应示例**:
```json
{
    "code": 0,
    "msg": "",
    "data": {
        "total": 1,
        "list": [
            {
                "id": 11,
                "creatorName": null,
                "createTime": 1764321752000,
                "interviewTemplateName": "2025新生测评后访谈",
                "interviewTemplateDetails": "<p>请简要描述学生基本情况：</p><p><br></p><p><br></p><p>该学生的风险等级为：</p><p><br></p><p><br></p><p>该学生的评估结论与建议为：</p><p><br></p><p><br></p><p><br></p>",
                "personnelScope": "全校新生",
                "remark": null
            }
        ]
    }
}
```

**字段说明**:

| 字段 | 类型 | 说明 |
|------|------|------|
| id | int | 模板ID |
| creatorName | string | 创建者姓名 |
| createTime | long | 创建时间（毫秒时间戳） |
| interviewTemplateName | string | 访谈模板名称（最多60字） |
| interviewTemplateDetails | string | 访谈表单详情（HTML格式） |
| personnelScope | string | 人员适用范围（最多60字） |
| remark | string | 备注（最多256字） |

### 3.2 获取单个访谈模板

```bash
curl -X GET "http://jerrypsy.top:8105/admin-api/psy/interview-template/get?id=11" \
  -H "Authorization: Bearer 7d41210e66684e4dbac9a95a408a8f7e" \
  -H "tenant-id: 163"
```

### 3.3 创建访谈模板

```bash
curl -X POST "http://jerrypsy.top:8105/admin-api/psy/interview-template/create" \
  -H "Authorization: Bearer 7d41210e66684e4dbac9a95a408a8f7e" \
  -H "tenant-id: 163" \
  -H "Content-Type: application/json" \
  -d '{
    "interviewTemplateName": "测试模板",
    "interviewTemplateDetails": "<p>模板内容HTML</p>",
    "personnelScope": "测试范围",
    "remark": "备注"
  }'
```

### 3.4 更新访谈模板

```bash
curl -X PUT "http://jerrypsy.top:8105/admin-api/psy/interview-template/update" \
  -H "Authorization: Bearer 7d41210e66684e4dbac9a95a408a8f7e" \
  -H "tenant-id: 163" \
  -H "Content-Type: application/json" \
  -d '{
    "id": 11,
    "interviewTemplateName": "2025新生测评后访谈（更新）",
    "interviewTemplateDetails": "<p>更新后的模板内容</p>",
    "personnelScope": "全校新生",
    "remark": null
  }'
```

### 3.5 删除访谈模板

```bash
curl -X DELETE "http://jerrypsy.top:8105/admin-api/psy/interview-template/delete?id=11" \
  -H "Authorization: Bearer 7d41210e66684e4dbac9a95a408a8f7e" \
  -H "tenant-id: 163"
```

### 3.6 导出访谈模板

```bash
curl -X GET "http://jerrypsy.top:8105/admin-api/psy/interview-template/export-excel?pageNo=1&pageSize=100" \
  -H "Authorization: Bearer 7d41210e66684e4dbac9a95a408a8f7e" \
  -H "tenant-id: 163" \
  -o interview_templates.xlsx
```

---

## 4. 咨询记录 (psa:consult-record)

> **模块说明**: 咨询记录是心理咨询师对学生进行正式咨询（个体/团体）的详细记录，包含主观记录（来访者自述）、客观记录（咨询师观察）、咨询问题类型、危机风险等级、建档日期、来访编号、关键描述、建议等。每条咨询记录关联一个预约记录(appointId)。

### 4.1 分页查询咨询记录

```bash
curl -X GET "http://jerrypsy.top:8105/admin-api/psa/consult-record/page?pageNo=1&pageSize=5" \
  -H "Authorization: Bearer 7d41210e66684e4dbac9a95a408a8f7e" \
  -H "tenant-id: 163"
```

**请求参数** (Query Params):

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| pageNo | int | 是 | 页码 |
| pageSize | int | 是 | 每页条数 |
| studentName | string | 否 | 学生姓名 |
| studentCode | string | 否 | 学号 |
| consultingQuestionType | string | 否 | 咨询问题类型 |
| riskType | string | 否 | 风险等级 |

**响应示例**:
```json
{
    "code": 0,
    "msg": "",
    "data": {
        "total": 1834,
        "list": [
            {
                "id": 1849,
                "appointId": 2192,
                "consultingQuestionType": "xinli",
                "subjectiveRecord": "来访者小胡说：...",
                "objectiveRecord": "【客观记录】本次为本学期最后一次咨询...",
                "filingDate": null,
                "visitCode": null,
                "keyDesc": null,
                "riskType": "wufengxian",
                "noComingReason": null,
                "consultRecordStatus": "wancheng",
                "remark": null,
                "filepath": null,
                "type": "geti",
                "suggestion": "【评估与建议】..."
            }
        ]
    }
}
```

**字段说明**:

| 字段 | 类型 | 说明 |
|------|------|------|
| id | int | 咨询记录ID |
| appointId | int | 关联的预约记录ID |
| consultingQuestionType | string | 咨询问题类型（`xinli`=心理, 其他待确认） |
| subjectiveRecord | string | 主观记录（来访者自述） |
| objectiveRecord | string | 客观记录（咨询师观察） |
| filingDate | string | 建档日期（YYYY-MM-DD） |
| visitCode | string | 来访编号 |
| keyDesc | string | 关键描述（最多256字） |
| riskType | string | 危机风险等级（`wufengxian`=无风险, 其他待确认） |
| noComingReason | string | 未到访原因 |
| consultRecordStatus | string | 咨询记录状态（`wancheng`=完成） |
| remark | string | 备注 |
| filepath | string | 附件路径 |
| type | string | 咨询类型（`geti`=个体, 其他待确认） |
| suggestion | string | 咨询建议 |

### 4.2 获取单条咨询记录

```bash
curl -X GET "http://jerrypsy.top:8105/admin-api/psa/consult-record/get?id=1849" \
  -H "Authorization: Bearer 7d41210e66684e4dbac9a95a408a8f7e" \
  -H "tenant-id: 163"
```

### 4.3 根据预约ID获取咨询记录

```bash
curl -X GET "http://jerrypsy.top:8105/admin-api/psa/consult-record/getConsultRecordByAppointId?appointRecordId=2192" \
  -H "Authorization: Bearer 7d41210e66684e4dbac9a95a408a8f7e" \
  -H "tenant-id: 163"
```

**说明**: 通过预约记录ID查询对应的咨询记录，适用于从预约管理页面跳转查看。

### 4.4 创建咨询记录

```bash
curl -X POST "http://jerrypsy.top:8105/admin-api/psa/consult-record/create" \
  -H "Authorization: Bearer 7d41210e66684e4dbac9a95a408a8f7e" \
  -H "tenant-id: 163" \
  -H "Content-Type: application/json" \
  -d '{
    "appointId": 2192,
    "consultingQuestionType": "xinli",
    "subjectiveRecord": "来访者自述内容...",
    "objectiveRecord": "咨询师客观观察...",
    "filingDate": "2026-03-04",
    "visitCode": "V20260304001",
    "keyDesc": "关键词描述",
    "riskType": "wufengxian",
    "noComingReason": null
  }'
```

**请求体字段说明**:

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| appointId | int | 是 | 预约记录ID |
| consultingQuestionType | string | 否 | 咨询问题类型 |
| subjectiveRecord | string | 否 | 主观记录 |
| objectiveRecord | string | 否 | 客观记录 |
| filingDate | string | 否 | 建档日期 |
| visitCode | string | 否 | 来访编号 |
| keyDesc | string | 否 | 关键描述 |
| riskType | string | 是 | 危机风险等级 |
| noComingReason | string | 否 | 未到访原因 |

### 4.5 创建紧急咨询记录

```bash
curl -X POST "http://jerrypsy.top:8105/admin-api/psa/consult-record/createEmergencyConsultRecord" \
  -H "Authorization: Bearer 7d41210e66684e4dbac9a95a408a8f7e" \
  -H "tenant-id: 163" \
  -H "Content-Type: application/json" \
  -d '{
    "consultingQuestionType": "xinli",
    "subjectiveRecord": "紧急咨询记录内容...",
    "riskType": "gaofengxian"
  }'
```

**说明**: 用于创建紧急/临时咨询记录，无需关联预约。

### 4.6 更新咨询记录

```bash
curl -X PUT "http://jerrypsy.top:8105/admin-api/psa/consult-record/update" \
  -H "Authorization: Bearer 7d41210e66684e4dbac9a95a408a8f7e" \
  -H "tenant-id: 163" \
  -H "Content-Type: application/json" \
  -d '{
    "id": 1849,
    "appointId": 2192,
    "consultingQuestionType": "xinli",
    "subjectiveRecord": "更新后的主观记录...",
    "riskType": "wufengxian"
  }'
```

### 4.7 删除咨询记录

```bash
curl -X DELETE "http://jerrypsy.top:8105/admin-api/psa/consult-record/delete?id=1849" \
  -H "Authorization: Bearer 7d41210e66684e4dbac9a95a408a8f7e" \
  -H "tenant-id: 163"
```

### 4.8 导出咨询记录

```bash
curl -X GET "http://jerrypsy.top:8105/admin-api/psa/consult-record/export-excel?pageNo=1&pageSize=100" \
  -H "Authorization: Bearer 7d41210e66684e4dbac9a95a408a8f7e" \
  -H "tenant-id: 163" \
  -o consult_records.xlsx
```

---

## 5. 咨询视图 (psa:consult-view)

> **模块说明**: 咨询视图是一个只读的综合查询视图，将预约记录、排班记录、咨询记录、学生信息等数据整合在一起展示。它关联了 scheduleRecordId、roomId、counselorId 等信息，提供了比 consult-record 更丰富的上下文信息。**该视图仅支持分页查询，不支持增删改操作。**

### 5.1 分页查询咨询视图

```bash
curl -X GET "http://jerrypsy.top:8105/admin-api/psa/consult-view/page?pageNo=1&pageSize=5" \
  -H "Authorization: Bearer 7d41210e66684e4dbac9a95a408a8f7e" \
  -H "tenant-id: 163"
```

**请求参数** (Query Params):

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| pageNo | int | 是 | 页码 |
| pageSize | int | 是 | 每页条数 |
| studentName | string | 否 | 学生姓名 |
| studentCode | string | 否 | 学号 |
| counselorName | string | 否 | 咨询师姓名 |
| actualDate | string | 否 | 咨询日期 |

**响应示例**:
```json
{
    "code": 0,
    "msg": "",
    "data": {
        "total": 208,
        "list": [
            {
                "scheduleRecordId": 5761,
                "roomId": 10,
                "studentName": "刘俊志",
                "studentCode": "3120220971019",
                "studentDeptName": "计算机与软件工程学院",
                "studentDistrictCode": "pidu",
                "studentGradeCode": "2022",
                "studentCultivationLevel": "benke",
                "studentMajorName": "计算机类",
                "studentClassName": "计算机类22-1",
                "studentSourceType": "chengzhen",
                "appointRecordSource": "taren",
                "appointRecordMethod": "xianchang",
                "roomName": "409",
                "counselorName": "王中瑞",
                "actualDate": "2026-03-04",
                "consultingQuestionType": "xinli",
                "type": "geti",
                "districtCode": "pidu",
                "counselorId": 4,
                "dayOfWeek": "3",
                "actualDateStartTime": 1772607600000,
                "actualDateEndTime": 1772610600000,
                "startTime": "15:00",
                "endTime": "15:50",
                "duringTimeMin": 50,
                "timeSegment": "15:00-15:50",
                "timeOfDay": "xiawu",
                "studentId": 85656,
                "studentDeptId": 130,
                "studentMajorId": 2401,
                "studentClassId": 1105,
                "studentGender": "1",
                "appointRecordStatus": "wancheng",
                "appointRecordStyle": "xianxia",
                "problemDesc": null,
                "otherInfo": null,
                "id": 1612,
                "appointId": 1661,
                "subjectiveRecord": "...",
                "suggestion": null,
                "objectiveRecord": null,
                "filingDate": null,
                "visitCode": null,
                "keyDesc": null,
                "riskType": "wufengxian",
                "consultRecordStatus": "wancheng",
                "filepath": null,
                "remark": null
            }
        ]
    }
}
```

**额外字段说明** (相比 consult-record 新增):

| 字段 | 类型 | 说明 |
|------|------|------|
| scheduleRecordId | int | 排班记录ID |
| roomId | int | 咨询室ID |
| roomName | string | 咨询室名称 |
| counselorId | int | 咨询师ID |
| counselorName | string | 咨询师姓名 |
| actualDate | string | 实际咨询日期 |
| dayOfWeek | string | 星期几 |
| actualDateStartTime | long | 实际开始时间戳 |
| actualDateEndTime | long | 实际结束时间戳 |
| startTime | string | 开始时间（HH:mm） |
| endTime | string | 结束时间（HH:mm） |
| duringTimeMin | int | 咨询时长（分钟） |
| timeSegment | string | 时间段 |
| timeOfDay | string | 时段（xiawu=下午） |
| studentSourceType | string | 学生来源类型（chengzhen=城镇） |
| appointRecordSource | string | 预约来源（taren=他人） |
| appointRecordMethod | string | 预约方式（xianchang=现场） |
| appointRecordStatus | string | 预约状态（wancheng=完成） |
| appointRecordStyle | string | 预约形式（xianxia=线下） |
| problemDesc | string | 问题描述 |
| districtCode | string | 校区编码 |

---

## 6. 我的来访者 (psy:my-visitor)

> **模块说明**: 我的来访者模块用于管理咨询师的来访者（学生）信息。可以查看来访者的院系、专业、班级等基本信息，以及咨询次数统计（总咨询次数、本学期咨询次数、首次咨询时间、最近咨询时间等）。支持从预约记录中自动统计学生来访信息。

### 6.1 分页查询我的来访者

```bash
curl -X GET "http://jerrypsy.top:8105/admin-api/psy/my-visitor/page?pageNo=1&pageSize=10" \
  -H "Authorization: Bearer 7d41210e66684e4dbac9a95a408a8f7e" \
  -H "tenant-id: 163"
```

**请求参数** (Query Params):

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| pageNo | int | 是 | 页码 |
| pageSize | int | 是 | 每页条数 |
| studentCode | string | 否 | 学号 |
| studentName | string | 否 | 学生姓名 |

**响应示例** (从页面分析):

| 字段 | 类型 | 说明 |
|------|------|------|
| studentCode | string | 学号 |
| studentName | string | 学生姓名 |
| deptName | string | 院系名称 |
| districtCode | string | 校区编码 |
| gradeCode | string | 年级编码 |
| cultivationLevel | string | 培养层次 |
| majorName | string | 专业名称 |
| firstTime | string | 首次咨询时间 |
| lastTime | string | 最近咨询时间 |
| totalCount | int | 总咨询次数 |
| myCount | int | 我的咨询次数 |

> **注意**: 该接口在当前用户(0720200029)下调用返回500错误，可能是权限问题或该用户无来访者数据。

### 6.2 获取单个来访者

```bash
curl -X GET "http://jerrypsy.top:8105/admin-api/psy/my-visitor/get?id=1" \
  -H "Authorization: Bearer 7d41210e66684e4dbac9a95a408a8f7e" \
  -H "tenant-id: 163"
```

### 6.3 创建来访者

```bash
curl -X POST "http://jerrypsy.top:8105/admin-api/psy/my-visitor/create" \
  -H "Authorization: Bearer 7d41210e66684e4dbac9a95a408a8f7e" \
  -H "tenant-id: 163" \
  -H "Content-Type: application/json" \
  -d '{
    "studentCode": "3120220971019",
    "studentName": "刘俊志",
    "deptId": 130,
    "deptName": "计算机与软件工程学院",
    "districtCode": "pidu",
    "gradeCode": "2022",
    "cultivationLevel": "benke",
    "classId": 1105,
    "className": "计算机类22-1",
    "totalTimes": 1,
    "currentTermTimes": 1
  }'
```

### 6.4 更新来访者

```bash
curl -X PUT "http://jerrypsy.top:8105/admin-api/psy/my-visitor/update" \
  -H "Authorization: Bearer 7d41210e66684e4dbac9a95a408a8f7e" \
  -H "tenant-id: 163" \
  -H "Content-Type: application/json" \
  -d '{
    "id": 1,
    "description": "备注信息",
    "totalTimes": 5,
    "currentTermTimes": 2
  }'
```

### 6.5 删除来访者

```bash
curl -X DELETE "http://jerrypsy.top:8105/admin-api/psy/my-visitor/delete?id=1" \
  -H "Authorization: Bearer 7d41210e66684e4dbac9a95a408a8f7e" \
  -H "tenant-id: 163"
```

### 6.6 导出来访者

```bash
curl -X GET "http://jerrypsy.top:8105/admin-api/psy/my-visitor/export-excel?pageNo=1&pageSize=100" \
  -H "Authorization: Bearer 7d41210e66684e4dbac9a95a408a8f7e" \
  -H "tenant-id: 163" \
  -o my_visitors.xlsx
```

---

## 7. 关联接口

### 7.1 学生分页查询（按预约）

> 用于来访者页面的"选择学生"功能

```bash
curl -X GET "http://jerrypsy.top:8105/admin-api/psc/student/pageByAppoint?pageNo=1&pageSize=10&studentName=" \
  -H "Authorization: Bearer 7d41210e66684e4dbac9a95a408a8f7e" \
  -H "tenant-id: 163"
```

---

## 附录：字典值参考

### 咨询问题类型 (consultingQuestionType)
| 值 | 说明 |
|------|------|
| xinli | 心理 |

### 危机风险等级 (riskType)
| 值 | 说明 |
|------|------|
| wufengxian | 无风险 |
| difengxian | 低风险 |
| zhongfengxian | 中风险 |
| gaofengxian | 高风险 |

### 咨询记录状态 (consultRecordStatus)
| 值 | 说明 |
|------|------|
| wancheng | 完成 |

### 咨询类型 (type)
| 值 | 说明 |
|------|------|
| geti | 个体 |

### 校区编码 (districtCode)
| 值 | 说明 |
|------|------|
| pidu | 郫都校区 |

### 培养层次 (cultivationLevel)
| 值 | 说明 |
|------|------|
| yuke | 预科 |
| benke | 本科 |

### 性别 (gender)
| 值 | 说明 |
|------|------|
| 1 | 男 |
| 2 | 女 |

### 学生来源类型 (studentSourceType)
| 值 | 说明 |
|------|------|
| chengzhen | 城镇 |

### 预约来源 (appointRecordSource)
| 值 | 说明 |
|------|------|
| taren | 他人 |

### 预约方式 (appointRecordMethod)
| 值 | 说明 |
|------|------|
| xianchang | 现场 |

### 预约状态 (appointRecordStatus)
| 值 | 说明 |
|------|------|
| wancheng | 完成 |

### 预约形式 (appointRecordStyle)
| 值 | 说明 |
|------|------|
| xianxia | 线下 |

### 时段 (timeOfDay)
| 值 | 说明 |
|------|------|
| xiawu | 下午 |

---

## API 端点汇总

| 模块 | 方法 | 路径 | 说明 |
|------|------|------|------|
| 认证 | POST | `/system/auth/login` | 登录 |
| 访谈记录 | GET | `/psy/interview-record/page` | 分页查询 |
| 访谈记录 | GET | `/psy/interview-record/page_my` | 查询我的记录 |
| 访谈记录 | GET | `/psy/interview-record/get` | 获取单条 |
| 访谈记录 | POST | `/psy/interview-record/create` | 创建 |
| 访谈记录 | PUT | `/psy/interview-record/update` | 更新 |
| 访谈记录 | DELETE | `/psy/interview-record/delete` | 删除 |
| 访谈记录 | GET | `/psy/interview-record/export-excel` | 导出 |
| 访谈模板 | GET | `/psy/interview-template/page` | 分页查询 |
| 访谈模板 | GET | `/psy/interview-template/get` | 获取单条 |
| 访谈模板 | POST | `/psy/interview-template/create` | 创建 |
| 访谈模板 | PUT | `/psy/interview-template/update` | 更新 |
| 访谈模板 | DELETE | `/psy/interview-template/delete` | 删除 |
| 访谈模板 | GET | `/psy/interview-template/export-excel` | 导出 |
| 咨询记录 | GET | `/psa/consult-record/page` | 分页查询 |
| 咨询记录 | GET | `/psa/consult-record/get` | 获取单条 |
| 咨询记录 | GET | `/psa/consult-record/getConsultRecordByAppointId` | 按预约ID查询 |
| 咨询记录 | POST | `/psa/consult-record/create` | 创建 |
| 咨询记录 | POST | `/psa/consult-record/createEmergencyConsultRecord` | 创建紧急记录 |
| 咨询记录 | PUT | `/psa/consult-record/update` | 更新 |
| 咨询记录 | DELETE | `/psa/consult-record/delete` | 删除 |
| 咨询记录 | GET | `/psa/consult-record/export-excel` | 导出 |
| 咨询视图 | GET | `/psa/consult-view/page` | 分页查询（只读） |
| 来访者 | GET | `/psy/my-visitor/page` | 分页查询 |
| 来访者 | GET | `/psy/my-visitor/get` | 获取单条 |
| 来访者 | POST | `/psy/my-visitor/create` | 创建 |
| 来访者 | PUT | `/psy/my-visitor/update` | 更新 |
| 来访者 | DELETE | `/psy/my-visitor/delete` | 删除 |
| 来访者 | GET | `/psy/my-visitor/export-excel` | 导出 |
| 学生 | GET | `/psc/student/pageByAppoint` | 按预约查询学生 |
