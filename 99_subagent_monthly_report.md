# 华心云 (HXCloud) 月报管理 API 文档

> **系统名称**: 西华大学心理健康管理系统 (华心云)  
> **Base URL**: `http://jerrypsy.top:8105/admin-api`  
> **租户ID**: `163`  
> **前端框架**: Vue.js 3 + Element Plus  
> **后端框架**: 基于 ruoyi-vue-pro (芋道) 框架  
> **提取来源**: `http://jerrypsy.top:8105/assets/index-Dl6RXgXM.js` 及相关 chunk 文件

---

## 目录

1. [认证接口](#1-认证接口)
2. [月报主表接口 (psm/month-record)](#2-月报主表接口)
3. [月报明细接口 (psm/month-record-detail)](#3-月报明细接口)
4. [前端组件映射关系](#4-前端组件映射关系)
5. [字典值参考](#5-字典值参考)
6. [咨询师确认流程说明](#6-咨询师确认流程说明)
7. [完整 curl 示例](#7-完整-curl-示例)

---

## 1. 认证接口

### 1.1 登录获取 Token

```bash
curl -X POST 'http://jerrypsy.top:8105/admin-api/system/auth/login' \
  -H 'Content-Type: application/json' \
  -H 'tenant-id: 163' \
  -d '{
    "username": "0720200029",
    "password": "Admin.123456"
  }'
```

**响应示例**:
```json
{
    "code": 0,
    "msg": "",
    "data": {
        "userId": 155,
        "accessToken": "ec583f961bc04de7bff58cafe7595a10",
        "refreshToken": "658230dae66f4e46a6b77d2c28b3c497",
        "expiresTime": 1783257724854,
        "weakPassword": false
    }
}
```

> 后续所有请求都需要携带请求头：
> - `Authorization: Bearer <accessToken>`
> - `tenant-id: 163`

---

## 2. 月报主表接口

> **JS 源码文件**: `assets/index-_gv_ahgh.js`  
> **前端组件**: `views/psm/monthrecord/`

### 2.1 分页查询月报列表

| 属性 | 值 |
|------|-----|
| **方法** | `GET` |
| **路径** | `/psm/month-record/page` |
| **说明** | 获取月报列表（分页），用于月报管理页面 |

**请求参数 (Query)**:

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `pageNo` | Integer | 否 | 页码，默认 1 |
| `pageSize` | Integer | 否 | 每页数量，默认 10 |

**curl 示例**:
```bash
curl -s 'http://jerrypsy.top:8105/admin-api/psm/month-record/page?pageNo=1&pageSize=10' \
  -H "Authorization: Bearer $TOKEN" \
  -H 'tenant-id: 163'
```

**响应示例**:
```json
{
    "code": 0,
    "msg": "",
    "data": {
        "total": 10,
        "list": [
            {
                "id": 73,
                "monthName": "2026年6月心理月报（0629）",
                "deadDate": "2026-07-06",
                "total": 1183,
                "instructorCount": 80,
                "counselorCount": 511,
                "psmMonthRecordStatus": "done",
                "collectTime": 1783240040000,
                "collectName": "王中瑞"
            }
        ]
    }
}
```

**响应字段说明**:

| 字段 | 类型 | 说明 |
|------|------|------|
| `id` | Long | 月报ID |
| `monthName` | String | 月报名称 |
| `deadDate` | String | 截止日期 (YYYY-MM-DD) |
| `total` | Integer | 关注学生总数 |
| `instructorCount` | Integer | 辅导员待确认数量 |
| `counselorCount` | Integer | 咨询师待确认数量 |
| `psmMonthRecordStatus` | String | 月报状态: `collecting`(收集中) / `done`(完成) |
| `collectTime` | Long | 收集完成时间 (毫秒时间戳) |
| `collectName` | String | 收集人姓名 |

---

### 2.2 获取单个月报详情

| 属性 | 值 |
|------|-----|
| **方法** | `GET` |
| **路径** | `/psm/month-record/get` |
| **说明** | 根据ID获取单个月报记录 |

**请求参数 (Query)**:

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `id` | Long | 是 | 月报ID |

**curl 示例**:
```bash
curl -s 'http://jerrypsy.top:8105/admin-api/psm/month-record/get?id=73' \
  -H "Authorization: Bearer $TOKEN" \
  -H 'tenant-id: 163'
```

**响应示例**:
```json
{
    "code": 0,
    "msg": "",
    "data": {
        "id": 73,
        "monthName": "2026年6月心理月报（0629）",
        "deadDate": "2026-07-06",
        "total": -1,
        "instructorCount": -1,
        "counselorCount": -1,
        "psmMonthRecordStatus": "collecting",
        "collectTime": null,
        "collectName": null
    }
}
```

> **注意**: 当月报状态为 `collecting` 时，`total`/`instructorCount`/`counselorCount` 返回 `-1`，表示正在收集中。

---

### 2.3 创建月报

| 属性 | 值 |
|------|-----|
| **方法** | `POST` |
| **路径** | `/psm/month-record/create` |
| **说明** | 创建新的月报记录（管理员操作） |

**请求体 (JSON)**:

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `monthName` | String | 是 | 月报名称 |
| `deadDate` | String | 是 | 截止日期 (YYYY-MM-DD) |

**curl 示例**:
```bash
curl -X POST 'http://jerrypsy.top:8105/admin-api/psm/month-record/create' \
  -H "Authorization: Bearer $TOKEN" \
  -H 'tenant-id: 163' \
  -H 'Content-Type: application/json' \
  -d '{
    "monthName": "2026年7月心理月报",
    "deadDate": "2026-08-06"
  }'
```

**响应**: `{"code": 0, "msg": "", "data": <新创建记录的ID>}`

---

### 2.4 更新月报

| 属性 | 值 |
|------|-----|
| **方法** | `PUT` |
| **路径** | `/psm/month-record/update` |
| **说明** | 更新月报记录 |

**请求体 (JSON)**: 同创建，需额外传入 `id` 字段。

**curl 示例**:
```bash
curl -X PUT 'http://jerrypsy.top:8105/admin-api/psm/month-record/update' \
  -H "Authorization: Bearer $TOKEN" \
  -H 'tenant-id: 163' \
  -H 'Content-Type: application/json' \
  -d '{
    "id": 73,
    "monthName": "2026年6月心理月报（0629）",
    "deadDate": "2026-07-10"
  }'
```

**响应**: `{"code": 0, "msg": "", "data": true}`

---

### 2.5 删除月报

| 属性 | 值 |
|------|-----|
| **方法** | `DELETE` |
| **路径** | `/psm/month-record/delete` |
| **说明** | 删除月报记录（管理员操作） |

**请求参数 (Query)**:

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `id` | Long | 是 | 月报ID |

**curl 示例**:
```bash
curl -X DELETE 'http://jerrypsy.top:8105/admin-api/psm/month-record/delete?id=73' \
  -H "Authorization: Bearer $TOKEN" \
  -H 'tenant-id: 163'
```

**响应**: `{"code": 0, "msg": "", "data": true}`

---

### 2.6 收集/提交月报

| 属性 | 值 |
|------|-----|
| **方法** | `POST` |
| **路径** | `/psm/month-record/collectRecord` |
| **说明** | 将月报从"收集中"变为"完成"状态。调用后月报状态变为 `done`，`collectTime` 和 `collectName` 会被自动填充 |

> ⚠️ **危险操作 / 主表级提交**：这是整条月报主表的“收集完成”，不是咨询师确认学生明细。批量确认咨询师意见时只允许调用 `/psm/month-record-detail/updateByCounselor`，不要在脚本收尾自动调用本接口。
>
> 已实测：误调用后，`PUT /psm/month-record/update` 即使返回 `data=true`，也不会把 `done` 恢复成 `collecting`；前端打包 API 未发现撤销接口。恢复通常需要数据库或后端服务端把主表状态改回 `collecting` 并清空 `collectTime/collectName`。

**请求参数 (Query)**:

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `id` | Long | 是 | 月报ID |

**curl 示例**:
```bash
curl -X POST 'http://jerrypsy.top:8105/admin-api/psm/month-record/collectRecord?id=73' \
  -H "Authorization: Bearer $TOKEN" \
  -H 'tenant-id: 163'
```

**响应**: `{"code": 0, "msg": "", "data": true}`

> **注意**: 此操作会将月报标记为完成，同时记录操作人和操作时间。除非用户明确要求“提交整条月报 / 标记整条月报完成 / 调 collectRecord”，否则禁止调用。

---

### 2.7 导出月报 Excel

| 属性 | 值 |
|------|-----|
| **方法** | `GET` |
| **路径** | `/psm/month-record/export-excel` |
| **说明** | 导出月报数据为 Excel 文件 |

**curl 示例**:
```bash
curl -s -o month_record.xlsx 'http://jerrypsy.top:8105/admin-api/psm/month-record/export-excel' \
  -H "Authorization: Bearer $TOKEN" \
  -H 'tenant-id: 163'
```

---

## 3. 月报明细接口

> **JS 源码文件**: `assets/index-CVapcIhi.js`  
> **前端组件**: `views/psm/monthrecorddetail/`

### 3.1 分页查询月报明细列表

| 属性 | 值 |
|------|-----|
| **方法** | `GET` |
| **路径** | `/psm/month-record-detail/page` |
| **说明** | 获取月报明细列表（分页），支持按月报ID和状态过滤 |

**请求参数 (Query)**:

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `pageNo` | Integer | 否 | 页码，默认 1 |
| `pageSize` | Integer | 否 | 每页数量，默认 10 |
| `monthRecordId` | Long | 否 | 月报ID，过滤特定月报的明细 |
| `status` | String | 否 | 状态过滤: `instructor_collect`(待辅导员确认) / `counselor_collect`(待咨询师确认) / `done`(完成) |

**curl 示例**:
```bash
# 查询待咨询师确认的明细
curl -s 'http://jerrypsy.top:8105/admin-api/psm/month-record-detail/page?monthRecordId=73&status=counselor_collect&pageSize=2' \
  -H "Authorization: Bearer $TOKEN" \
  -H 'tenant-id: 163'
```

**响应示例**:
```json
{
    "code": 0,
    "msg": "",
    "data": {
        "total": 116,
        "list": [
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
                "instructorHandlingMethod": "level5",
                "monthName": "2026年6月心理月报（0629）",
                "psmMonthRecordStatus": "collecting",
                "inFocusTime": 1782719215000
            }
        ]
    }
}
```

**响应字段详细说明**:

| 字段 | 类型 | 说明 |
|------|------|------|
| `id` | Long | 明细记录ID |
| `monthRecordId` | Long | 所属月报ID |
| **学生基本信息** | | |
| `studentId` | Long | 学生用户ID |
| `studentName` | String | 学生姓名 |
| `studentCode` | String | 学号 |
| `studentDeptId` | Long | 学院ID |
| `studentDeptName` | String | 学院名称 |
| `studentDistrictCode` | String | 校区编码: `pidu`(郫都) / `yibin`(宜宾) / `pengzhou`(彭州) |
| `studentGradeCode` | String | 年级: `2020`-`2025` 等 |
| `studentCultivationLevel` | String | 培养层次: `benke`(本科) / `shuoshi`(硕士) 等 |
| `studentMajorId` | Long | 专业ID |
| `studentMajorName` | String | 专业名称 |
| `studentClassId` | Long | 班级ID |
| `studentClassName` | String | 班级名称 |
| `studentGender` | String | 性别: `1`(男) / `2`(女) |
| **关注信息** | | |
| `focusReasonType` | String | 关注原因类型（见字典） |
| `focusId` | Long | 关注记录ID |
| `belongCounselorId` | Long | 所属咨询师用户ID |
| `belongCounselorName` | String | 咨询师姓名 |
| `belongInstructorId` | Long | 所属辅导员用户ID |
| `belongInstructorName` | String | 辅导员姓名 |
| **评估信息** | | |
| `healthType` | String | 个人身体状态（见字典） |
| `learningStatus` | String | 学习状况（见字典） |
| `roommateStatus` | String | 同伴与舍友关系（见字典） |
| `homeStatus` | String | 家庭情况（见字典） |
| `growthStatus` | String | 成长情况（见字典） |
| `homeEconomyStatus` | String | 家庭经济状况（见字典） |
| `suicideInjuryRiskType` | String | 自杀/伤人风险类型（见字典） |
| `crisisLevel` | String | 危机等级（见字典） |
| `psychiatricDiagnosis` | String | 精神科诊断（见字典） |
| `medicationStatus` | String | 服药情况（见字典） |
| `familyStructure` | String | 家庭结构（见字典） |
| `crisisPlanLevel` | String | 危机预案等级（见字典） |
| **描述信息** | | |
| `majorChangeDesc` | String | 重大变故详细描述 |
| `studentDesc` | String | 学生情况详情（辅导员填写） |
| `currentMeasure` | String | 目前采取措施（辅导员填写） |
| `counselorMeasure` | String | 咨询师建议和回复（**咨询师填写，counselor_collect 时必填**） |
| `instructorMeasure` | String | 辅导员措施（辅导员填写） |
| `studentJournalLog` | String | 学生日志 |
| **确认信息** | | |
| `monthRecordDetailStatus` | String | 状态: `instructor_collect` / `counselor_collect` / `done` |
| `instructorCollectTime` | Long | 辅导员确认时间（毫秒时间戳） |
| `instructorCollectName` | String | 辅导员姓名 |
| `counselorCollectTime` | Long | 咨询师确认时间（毫秒时间戳） |
| `counselorCollectName` | String | 咨询师姓名 |
| **移除关注信息** | | |
| `instructorRemoveStatus` | String | 辅导员移除建议: `putong`(普通确认) / `jianyi_yichu`(建议出库) |
| `removeReasonType` | String | 移除原因类型: `stable`(情况稳定) / `graduate`(毕业) / `dropout`(退学) / `others`(其他) |
| `removeReasonDesc` | String | 移除关注情况说明 |
| `fileUrlOut` | String | 移除关注相关附件 |
| `counselorRemoveStatus` | String | 咨询师移除确认: `tongyi`(同意) / `butongyi`(不同意) |
| `instructorHandlingMethod` | String | 辅导员处理方式（见字典） |

---

### 3.2 获取单条月报明细

| 属性 | 值 |
|------|-----|
| **方法** | `GET` |
| **路径** | `/psm/month-record-detail/get` |
| **说明** | 根据ID获取单条月报明细记录 |

**请求参数 (Query)**:

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `id` | Long | 是 | 明细记录ID |

**curl 示例**:
```bash
curl -s 'http://jerrypsy.top:8105/admin-api/psm/month-record-detail/get?id=17243' \
  -H "Authorization: Bearer $TOKEN" \
  -H 'tenant-id: 163'
```

**响应**: 与 3.1 中的单条记录结构相同（注意：get 接口返回的 `monthName`/`psmMonthRecordStatus`/`inFocusTime` 为 null，page 接口才有这些关联字段）。

---

### 3.3 ⭐ 咨询师确认提交 (updateByCounselor)

| 属性 | 值 |
|------|-----|
| **方法** | `POST` |
| **路径** | `/psm/month-record-detail/updateByCounselor` |
| **说明** | **咨询师确认提交月报明细**。咨询师填写 `counselorMeasure` 后提交，提交后状态变为 `done`，并自动记录确认时间和确认人。这是"咨询师确认"功能的核心接口 |

**请求体 (JSON)** — 所有字段均为必填（继承原有记录数据 + 新增咨询师填写部分）:

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `id` | Long | ✅ | 明细记录ID |
| `monthRecordId` | Long | ✅ | 所属月报ID |
| `studentId` | Long | ✅ | 学生ID |
| `studentName` | String | ✅ | 学生姓名 |
| `studentCode` | String | ✅ | 学号 |
| `studentDeptId` | Long | ✅ | 学院ID |
| `studentDeptName` | String | ✅ | 学院名称 |
| `studentDistrictCode` | String | ✅ | 校区编码 |
| `studentGradeCode` | String | ✅ | 年级 |
| `studentCultivationLevel` | String | ✅ | 培养层次 |
| `studentMajorId` | Long | ✅ | 专业ID |
| `studentMajorName` | String | ✅ | 专业名称 |
| `studentClassId` | Long | ✅ | 班级ID |
| `studentClassName` | String | ✅ | 班级名称 |
| `studentGender` | String | ✅ | 性别 |
| `focusReasonType` | String | ✅ | 关注原因类型 |
| `healthType` | String | ✅ | 身体状态 |
| `learningStatus` | String | ✅ | 学习状况 |
| `roommateStatus` | String | ✅ | 舍友关系 |
| `homeStatus` | String | ✅ | 家庭情况 |
| `growthStatus` | String | ✅ | 成长情况 |
| `homeEconomyStatus` | String | ✅ | 家庭经济 |
| `suicideInjuryRiskType` | String | ✅ | 自杀/伤人风险 |
| `crisisLevel` | String | ✅ | 危机等级 |
| `currentMeasure` | String | ✅ | 目前采取措施 |
| `instructorMeasure` | String | ✅ | 辅导员措施 |
| `monthRecordDetailStatus` | String | ✅ | 当前状态值 `counselor_collect` |
| `instructorRemoveStatus` | String | ✅ | 辅导员移除建议 |
| `psychiatricDiagnosis` | String | ✅ | 精神科诊断 |
| `medicationStatus` | String | ✅ | 服药情况 |
| `familyStructure` | String | ✅ | 家庭结构 |
| `crisisPlanLevel` | String | ✅ | 危机预案等级 |
| `instructorHandlingMethod` | String | ✅ | 辅导员处理方式 |
| `focusId` | Long | ✅ | 关注记录ID |
| `belongCounselorId` | Long | ✅ | 咨询师用户ID |
| `belongInstructorId` | Long | ✅ | 辅导员用户ID |
| **`counselorMeasure`** | **String** | **✅** | **【核心字段】咨询师建议和回复** — 咨询师需在此填写对学生情况的评估建议 |
| `counselorRemoveStatus` | String | 条件 | 移除确认: `tongyi`(同意出库) / `butongyi`(不同意出库)，当 `instructorRemoveStatus=jianyi_yichu` 时必填 |
| `majorChangeDesc` | String | 否 | 重大变故描述 |
| `studentDesc` | String | 否 | 学生情况详情 |
| `removeReasonType` | String | 条件 | 移除原因类型，当 `instructorRemoveStatus=jianyi_yichu` 时需填 |
| `removeReasonDesc` | String | 条件 | 移除原因说明，当 `instructorRemoveStatus=jianyi_yichu` 时需填 |
| `fileUrlOut` | String | 否 | 移除相关附件 |

**curl 示例**:
```bash
curl -X POST 'http://jerrypsy.top:8105/admin-api/psm/month-record-detail/updateByCounselor' \
  -H "Authorization: Bearer $TOKEN" \
  -H 'tenant-id: 163' \
  -H 'Content-Type: application/json' \
  -d '{
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
    "suicideInjuryRiskType": "none",
    "crisisLevel": "none",
    "currentMeasure": "1.安排学生党员针对性学业帮扶\n2.告知家长学生心理状态变化",
    "counselorMeasure": "建议持续关注学生情绪变化，定期安排心理咨询，必要时转介精神科。辅导员已做好安全告知和帮扶工作，继续执行。",
    "instructorMeasure": "无",
    "monthRecordDetailStatus": "counselor_collect",
    "instructorRemoveStatus": "putong",
    "psychiatricDiagnosis": "sleep",
    "medicationStatus": "under",
    "familyStructure": "wanzheng",
    "crisisPlanLevel": "three",
    "instructorHandlingMethod": "level5",
    "focusId": 3712,
    "belongCounselorId": 155,
    "belongInstructorId": 110990
  }'
```

**成功响应**: `{"code": 0, "msg": "", "data": true}`

**常见错误响应**:

| code | msg | 原因 |
|------|-----|------|
| 400 | 用户单位不能为空 | 缺少 `studentDeptId` 或 `studentDeptName` |
| 400 | 状态不能为空 | 缺少 `monthRecordDetailStatus` |
| 400 | 校区不能为空 | 缺少 `studentDistrictCode` |

---

### 3.4 辅导员确认提交 (updateByInstructor)

| 属性 | 值 |
|------|-----|
| **方法** | `POST` |
| **路径** | `/psm/month-record-detail/updateByInstructor` |
| **说明** | 辅导员确认提交月报明细。辅导员填写 `studentDesc`（学生情况详情）、`currentMeasure`（目前采取措施）、`instructorMeasure`（措施情况）等字段后提交 |

**请求体**: 与 3.3 结构相同，但核心填写字段为：
- `studentDesc` — 学生近期更新情况
- `currentMeasure` — 辅导员工作情况
- `instructorRemoveStatus` — 移除关注状态
- `monthRecordDetailStatus` — 值为 `instructor_collect`

**curl 示例**:
```bash
curl -X POST 'http://jerrypsy.top:8105/admin-api/psm/month-record-detail/updateByInstructor' \
  -H "Authorization: Bearer $TOKEN" \
  -H 'tenant-id: 163' \
  -H 'Content-Type: application/json' \
  -d '{
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
    "suicideInjuryRiskType": "none",
    "crisisLevel": "none",
    "studentDesc": "学生近期情况描述...",
    "currentMeasure": "辅导员采取的措施...",
    "instructorMeasure": "措施执行情况...",
    "monthRecordDetailStatus": "instructor_collect",
    "instructorRemoveStatus": "putong",
    "psychiatricDiagnosis": "sleep",
    "medicationStatus": "under",
    "familyStructure": "wanzheng",
    "crisisPlanLevel": "three",
    "instructorHandlingMethod": "level5",
    "focusId": 3712,
    "belongCounselorId": 155,
    "belongInstructorId": 110990
  }'
```

**成功响应**: `{"code": 0, "msg": "", "data": true}`

---

### 3.5 创建月报明细

| 属性 | 值 |
|------|-----|
| **方法** | `POST` |
| **路径** | `/psm/month-record-detail/create` |
| **说明** | 创建新的月报明细记录（管理员/系统操作） |

**curl 示例**:
```bash
curl -X POST 'http://jerrypsy.top:8105/admin-api/psm/month-record-detail/create' \
  -H "Authorization: Bearer $TOKEN" \
  -H 'tenant-id: 163' \
  -H 'Content-Type: application/json' \
  -d '{
    "monthRecordId": 73,
    "studentId": 108341,
    "studentName": "胡益杨",
    "studentCode": "3120244871130",
    "studentDeptId": 133,
    "studentDeptName": "航空航天与智能装备学院"
  }'
```

---

### 3.6 删除月报明细

| 属性 | 值 |
|------|-----|
| **方法** | `DELETE` |
| **路径** | `/psm/month-record-detail/delete` |
| **说明** | 删除月报明细记录 |

**curl 示例**:
```bash
curl -X DELETE 'http://jerrypsy.top:8105/admin-api/psm/month-record-detail/delete?id=17243' \
  -H "Authorization: Bearer $TOKEN" \
  -H 'tenant-id: 163'
```

---

### 3.7 重置月报明细

| 属性 | 值 |
|------|-----|
| **方法** | `POST` |
| **路径** | `/psm/month-record-detail/reset` |
| **说明** | 重置月报明细状态，退回上一步。例如将 `counselor_collect` 重置为 `instructor_collect` |

**curl 示例**:
```bash
curl -X POST 'http://jerrypsy.top:8105/admin-api/psm/month-record-detail/reset?id=17243' \
  -H "Authorization: Bearer $TOKEN" \
  -H 'tenant-id: 163'
```

**响应**: `{"code": 0, "msg": "", "data": true}`

---

### 3.8 导出月报明细 Excel

| 属性 | 值 |
|------|-----|
| **方法** | `GET` |
| **路径** | `/psm/month-record-detail/export-excel` |
| **说明** | 导出月报明细数据为 Excel 文件 |

**curl 示例**:
```bash
curl -s -o month_record_detail.xlsx 'http://jerrypsy.top:8105/admin-api/psm/month-record-detail/export-excel?monthRecordId=73&status=counselor_collect' \
  -H "Authorization: Bearer $TOKEN" \
  -H 'tenant-id: 163'
```

---

### 3.9 驳回月报明细 (reject) — 未找到后端实现

| 属性 | 值 |
|------|-----|
| **方法** | `PUT` |
| **路径** | `/psm/month-record-detail/reject/{id}` |
| **说明** | 前端 JS 中有定义 (`rejectMonthRecordDetail`)，但后端返回 404，**该接口可能未实现或路径不同** |

**curl 示例**:
```bash
curl -X PUT 'http://jerrypsy.top:8105/admin-api/psm/month-record-detail/reject/17243' \
  -H "Authorization: Bearer $TOKEN" \
  -H 'tenant-id: 163'
```

**实际响应**: `{"code": 404, "msg": "请求地址不存在:admin-api/psm/month-record-detail/reject/17243", "data": null}`

---

## 4. 前端组件映射关系

| 前端路由/组件 | 对应 JS Chunk | 调用的 API |
|---------------|---------------|------------|
| `views/psm/monthrecord/index.vue` | 主 bundle | `GET /psm/month-record/page` |
| `views/psm/monthrecord/MonthRecordForm.vue` | `MonthRecordForm-BlZVae1h.js` | `POST/PUT /psm/month-record/create` `/update` |
| `views/psm/monthrecord/MonthDetailListForm.vue` | `MonthDetailListForm-N2Yi-OGn.js` | `GET /psm/month-record-detail/page` |
| `views/psm/monthrecorddetail/index.vue` | (主 bundle) | `GET /psm/month-record-detail/page` |
| `views/psm/monthrecorddetail/CounselorSubmitIndex.vue` | `CounselorSubmitIndex-CYIIeBZf.js` | 页面: `queryStatus="counselor_collect"` |
| `views/psm/monthrecorddetail/InstructorSubmitIndex.vue` | (类似) | 页面: `queryStatus="instructor_collect"` |
| `views/psm/monthrecorddetail/MonthRecordDetailForm.vue` | `MonthRecordDetailForm-e1nvReL2.js` | `POST updateByCounselor` / `updateByInstructor` |

**API Service 文件**:

| Service 文件 | 导出名 | 包含接口 |
|-------------|--------|---------|
| `index-_gv_ahgh.js` | `M` | month-record CRUD + collectRecord |
| `index-CVapcIhi.js` | `M` | month-record-detail CRUD + updateBy* + reset + reject |

---

## 5. 字典值参考

> 以下字典值均通过 `GET /system/dict-data/simple-list` 接口获取并过滤

### 5.1 月报状态 (`psm_month_record_status`)

| 值 | 标签 | 说明 |
|-----|------|------|
| `collecting` | 收集中 | 月报正在收集，辅导员和咨询师正在填写 |
| `done` | 完成 | 月报已收集完成 |

### 5.2 月报明细状态 (`psm_month_record_detail_status`)

| 值 | 标签 | 说明 |
|-----|------|------|
| `instructor_collect` | 待辅导员确认 | 辅导员需填写学生情况、措施等 |
| `counselor_collect` | 待咨询师确认 | 辅导员已填写完毕，等待咨询师填写建议 |
| `done` | 完成 | 咨询师已确认，流程结束 |

### 5.3 关注原因类型 (`psm_focus_reason_type`)

| 值 | 标签 |
|-----|------|
| `qingxu` | 情绪异常 |
| `xueye` | 学业困难 |
| `xingwei` | 行为异常 |
| `weiji` | 危机干预 |
| `ceping` | 测评预警 |
| `fangtan` | 新生访谈 |
| `qita` | 其他需要关注的情况 |
| `todo` | 待完善 |

### 5.4 身体状态 (`psm_health_type`)

| 值 | 标签 |
|-----|------|
| `lianghao` | 健康状况良好 |
| `yiban` | 健康状况一般 |
| `manxing` | 有慢性身体疾病 |
| `jixing` | 有急性身体疾病 |
| `under` | 有精神科诊断，正在服药 |
| `tingyao` | 有精神科诊断，自行停药 |
| `zunyizhu` | 有精神科诊断，遵医嘱停药 |
| `canji` | 有残疾情况 |
| `others` | 其他健康问题 |
| `todo` | 待完善 |

### 5.5 学习状况 (`psm_learning_status`)

| 值 | 标签 |
|-----|------|
| `lianghao` | 成绩良好 |
| `zhongdeng` | 成绩中等 |
| `jiaocha` | 成绩较差 |
| `guake` | 多次挂科 |
| `jinggao` | 学业警告 |
| `quexaxingqu` | 缺乏学习兴趣 |
| `zhiyemimang` | 职业生涯迷茫 |
| `others` | 其他学业问题 |
| `todo` | 待完善 |

### 5.6 同伴与舍友关系 (`psm_roommate_status`)

| 值 | 标签 |
|-----|------|
| `rongqia` | 关系融洽，互帮互助 |
| `lianghao` | 关系良好，有一定互动 |
| `yiban` | 关系一般，不咸不淡 |
| `shuyuan` | 关系疏远，缺乏交流 |
| `chongtu` | 关系紧张，经常发生冲突 |
| `gudu` | 缺乏同伴，感到孤独 |
| `fuza` | 同伴关系复杂 |
| `others` | 其他情况 |
| `todo` | 待完善 |

### 5.7 家庭情况 (`psm_home_status`)

| 值 | 标签 |
|-----|------|
| `hexie` | 家庭关系和谐 |
| `jinzhang` | 父母经常争吵 |
| `damo` | 家庭关系淡漠 |
| `baoli` | 家庭暴力环境 |
| `others` | 其他情况 |
| `todo` | 待完善 |

### 5.8 成长情况 (`psm_growth_status`)

| 值 | 标签 |
|-----|------|
| `fumu` | 跟随父母长大 |
| `danqin` | 单亲养育 |
| `liushou` | 留守养育 |
| `jiyang` | 寄养或领养 |
| `others` | 其他情况 |
| `todo` | 待完善 |

### 5.9 家庭经济状况 (`psm_home_economy_status`)

| 值 | 标签 |
|-----|------|
| `fuyu` | 较为富裕 |
| `zhongdeng` | 中等收入 |
| `kunnan` | 有些困难 |
| `feichangkunnan` | 非常困难 |
| `others` | 其他 |
| `todo` | 待完善 |

### 5.10 自杀/伤人风险类型 (`psm_suicide_injury_risk_type`)

| 值 | 标签 |
|-----|------|
| `none` | 无自伤或伤人想法 |
| `notnow` | 现在没有自杀自伤想法，但曾有自杀自伤尝试 |
| `recentidea` | 近期有自伤想法，但一闪而过 |
| `recentthought` | 近期常有自杀或自伤观念，无具体计划 |
| `recentplan` | 近期有自杀或自伤计划，但未尝试 |
| `harm` | 近期有自伤或自残行为(非自杀目的) |
| `changshi` | 近期有自杀尝试 |
| `harmothers` | 有伤人观念，但无明确计划 |
| `harmplan` | 有伤人计划，但尚未实施 |
| `harmaction` | 已经实施伤人尝试或行为 |

### 5.11 危机等级 (`psm_crisis_level`)

| 值 | 标签 |
|-----|------|
| `none` | 无风险 |
| `low` | 低风险 |
| `mid` | 中风险 |
| `high` | 高风险 |

### 5.12 精神科诊断 (`psm_psychiatric_diagnosis`)

| 值 | 标签 |
|-----|------|
| `none` | 无精神科诊断 |
| `dep` | 抑郁 |
| `anx` | 焦虑 |
| `sleep` | 睡眠障碍 |
| `ocd` | 强迫 |
| `ptsd` | PTSD |
| `bipolar` | 双相情感障碍 |
| `psy` | 精神分裂症 |
| `person` | 人格障碍 |
| `others` | 其他 |

### 5.13 服药情况 (`psm_medication_status`)

| 值 | 标签 |
|-----|------|
| `none` | 无精神科诊断，未服药 |
| `under` | 有精神科诊断，正在服药 |
| `tingyao` | 有精神科诊断，自行停药 |
| `yizhu` | 有精神科诊断，遵医嘱停药 |
| `others` | 其他 |
| `todo` | 待完善 |

### 5.14 家庭结构 (`psm_family_structure`)

| 值 | 标签 |
|-----|------|
| `wanzheng` | 完整家庭 |
| `chongzu` | 重组家庭 |
| `qushi` | 单亲或双亲去世 |
| `liyi` | 父母离异或分居 |
| `others` | 其他情况 |
| `todo` | 待完善 |

### 5.15 危机预案等级 (`psm_danger_measure_level`)

| 值 | 标签 |
|-----|------|
| `three` | 三级预案(无风险，非突破保密情形) |
| `two` | 二级预案(有自杀自伤伤人风险，辅导员关注) |
| `one` | 一级预案(实施自杀自伤伤人行为，各部门协同) |

### 5.16 辅导员移除建议 (`psm_instructor_remove_status`)

| 值 | 标签 |
|-----|------|
| `putong` | 普通确认（继续关注） |
| `jianyi_yichu` | 建议出库（建议移除关注） |

### 5.17 移除原因类型 (`psm_remove_reason`)

| 值 | 标签 |
|-----|------|
| `stable` | 情况稳定 |
| `graduate` | 毕业 |
| `dropout` | 退学 |
| `others` | 其他 |
| `todo` | 待完善 |

### 5.18 辅导员处理方式 (`psm_instructor_handling_method`)

| 值 | 标签 |
|-----|------|
| `level1` | 1级：通知家长和学校相关人员，24小时防控或送专科医院，启动危机干预 |
| `level2` | 2级：通知家长和学校相关人员，告知风险，给予建议 |
| `level3` | 3级：辅导员持续关注并追踪学生后续发展变化 |
| `level4` | 4级：保持关注，正常自我成长 |
| `level5` | 5级：正常范围，无需特殊处理 |
| `others` | 其他 |
| `todo` | 待完善 |

---

## 6. 咨询师确认流程说明

```
月报创建 (psmMonthRecordStatus=collecting)
    │
    ▼
辅导员填写 → POST updateByInstructor
    │  (填写: studentDesc, currentMeasure, instructorRemoveStatus)
    │  (monthRecordDetailStatus: instructor_collect → counselor_collect)
    ▼
咨询师确认 → POST updateByCounselor
    │  (填写: counselorMeasure, counselorRemoveStatus)
    │  (monthRecordDetailStatus: counselor_collect → done)
    ▼
月报完成 → POST collectRecord
    (psmMonthRecordStatus: collecting → done)
```

> ⚠️ 上面的最后一步是整条月报主表提交，不属于咨询师批量确认。自动化任务默认只做到 `monthRecordDetailStatus: counselor_collect → done`，不得继续执行 `POST collectRecord`。

**前端页面路由**:
- 咨询师确认页面: `CounselorSubmitIndex.vue` → 查询 `status=counselor_collect` 的记录
- 辅导员确认页面: `InstructorSubmitIndex.vue` → 查询 `status=instructor_collect` 的记录

---

## 7. 完整 curl 示例

### 7.1 一键登录并查询待确认列表

```bash
#!/bin/bash

# 1. 登录
TOKEN=$(curl -s -X POST 'http://jerrypsy.top:8105/admin-api/system/auth/login' \
  -H 'Content-Type: application/json' \
  -H 'tenant-id: 163' \
  -d '{"username":"0720200029","password":"Admin.123456"}' | python3 -c "import json,sys; print(json.load(sys.stdin)['data']['accessToken'])")

echo "Token: $TOKEN"

# 2. 查询所有月报
echo "=== 月报列表 ==="
curl -s 'http://jerrypsy.top:8105/admin-api/psm/month-record/page?pageNo=1&pageSize=5' \
  -H "Authorization: Bearer $TOKEN" \
  -H 'tenant-id: 163' | python3 -m json.tool

# 3. 查询待咨询师确认的明细
echo "=== 待咨询师确认 ==="
curl -s 'http://jerrypsy.top:8105/admin-api/psm/month-record-detail/page?monthRecordId=73&status=counselor_collect&pageSize=5' \
  -H "Authorization: Bearer $TOKEN" \
  -H 'tenant-id: 163' | python3 -m json.tool

# 4. 获取单条明细详情
echo "=== 单条明细 ==="
curl -s 'http://jerrypsy.top:8105/admin-api/psm/month-record-detail/get?id=17243' \
  -H "Authorization: Bearer $TOKEN" \
  -H 'tenant-id: 163' | python3 -m json.tool
```

### 7.2 咨询师确认提交（完整字段）

```bash
#!/bin/bash
TOKEN="ec583f961bc04de7bff58cafe7595a10"
DETAIL_ID=17243

# 先获取当前明细数据
DETAIL=$(curl -s "http://jerrypsy.top:8105/admin-api/psm/month-record-detail/get?id=$DETAIL_ID" \
  -H "Authorization: Bearer $TOKEN" \
  -H 'tenant-id: 163')

# 提取数据并修改 counselorMeasure 字段后提交
echo "$DETAIL" | python3 -c "
import json, sys
d = json.load(sys.stdin)['data']
d['counselorMeasure'] = '经评估，该生目前情绪状态稳定，学业压力可控。建议：1.持续关注学生睡眠改善情况 2.定期安排心理咨询 3.辅导员保持日常沟通'
# 如果辅导员建议出库，咨询师需表态
if d.get('instructorRemoveStatus') == 'jianyi_yichu':
    d['counselorRemoveStatus'] = 'tongyi'  # 或 'butongyi'
print(json.dumps(d, ensure_ascii=False))
" | curl -X POST 'http://jerrypsy.top:8105/admin-api/psm/month-record-detail/updateByCounselor' \
  -H "Authorization: Bearer $TOKEN" \
  -H 'tenant-id: 163' \
  -H 'Content-Type: application/json' \
  -d @-
```

---

## API 端点汇总

| 方法 | 路径 | 说明 | 角色 |
|------|------|------|------|
| `POST` | `/system/auth/login` | 登录获取Token | 所有 |
| `GET` | `/psm/month-record/page` | 月报分页列表 | 管理员/咨询师 |
| `GET` | `/psm/month-record/get?id=` | 获取单个月报 | 管理员/咨询师 |
| `POST` | `/psm/month-record/create` | 创建月报 | 管理员 |
| `PUT` | `/psm/month-record/update` | 更新月报 | 管理员 |
| `DELETE` | `/psm/month-record/delete?id=` | 删除月报 | 管理员 |
| `POST` | `/psm/month-record/collectRecord?id=` | ⚠️ 收集完成整条月报，禁止自动调用 | 管理员 |
| `GET` | `/psm/month-record/export-excel` | 导出月报Excel | 管理员 |
| `GET` | `/psm/month-record-detail/page` | 明细分页列表 | 管理员/咨询师/辅导员 |
| `GET` | `/psm/month-record-detail/get?id=` | 获取单条明细 | 管理员/咨询师/辅导员 |
| `POST` | `/psm/month-record-detail/create` | 创建明细 | 管理员 |
| `POST` | `/psm/month-record-detail/updateByCounselor` | **咨询师确认** | 咨询师 |
| `POST` | `/psm/month-record-detail/updateByInstructor` | 辅导员确认 | 辅导员 |
| `POST` | `/psm/month-record-detail/reset?id=` | 重置明细状态 | 管理员 |
| `DELETE` | `/psm/month-record-detail/delete?id=` | 删除明细 | 管理员 |
| `GET` | `/psm/month-record-detail/export-excel` | 导出明细Excel | 管理员 |
| `PUT` | `/psm/month-record-detail/reject/{id}` | 驳回明细 | 未实现(404) |
| `GET` | `/system/dict-data/simple-list` | 获取字典数据 | 所有 |

---

*文档生成时间: 2026-07-05*  
*数据来源: JS Bundle 静态分析 + 实际 API 测试验证*
