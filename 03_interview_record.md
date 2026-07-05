# 华心云 - 访谈记录 API (psy/interview-record)

## 概述
访谈记录是咨询师对学生的面谈记录，通常用于新生测评后访谈等场景。每条记录关联一个访谈模板。

## API 端点列表

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/psy/interview-record/page` | 分页查询访谈记录列表 |
| GET | `/psy/interview-record/page_my` | 查询我的访谈记录 |
| GET | `/psy/interview-record/get?id=` | 获取单条访谈记录 |
| POST | `/psy/interview-record/create` | 创建访谈记录 |
| POST | `/psy/interview-record/update` | 更新访谈记录 |
| GET | `/psy/interview-record/delete?id=` | 删除访谈记录 |
| GET | `/psy/interview-record/export-excel` | 导出Excel |

### 访谈模板 (interview-template)
| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/psy/interview-template/page` | 分页查询访谈模板 |
| GET | `/psy/interview-template/get?id=` | 获取单条模板 |
| POST | `/psy/interview-template/create` | 创建模板 |
| POST | `/psy/interview-template/update` | 更新模板 |
| GET | `/psy/interview-template/delete?id=` | 删除模板 |
| GET | `/psy/interview-template/export-excel` | 导出Excel |

---

## 1. 分页查询访谈记录

```bash
curl -s 'http://jerrypsy.top:8105/admin-api/psy/interview-record/page?pageNo=1&pageSize=10' \
  -H 'Authorization: Bearer <token>' \
  -H 'tenant-id: 163'
```

### 返回数据结构
```json
{
  "code": 0,
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
        "interviewResultDetails": "<p>请简要描述学生基本情况：</p><p>不太喜欢社交...</p>",
        "remark": null
      }
    ]
  }
}
```

### 字段说明
| 字段 | 类型 | 说明 |
|------|------|------|
| id | int | 记录ID |
| creatorName | string | 创建人姓名 |
| createTime | long | 创建时间(时间戳) |
| studentId | int | 学生ID |
| studentName | string | 学生姓名 |
| studentCode | string | 学号 |
| studentDeptName | string | 学院 |
| studentMajorName | string | 专业 |
| studentClassName | string | 班级 |
| studentGender | string | 性别 (`1`=男, `2`=女) |
| interviewTemplateName | string | 访谈模板名称 |
| interviewTemplateId | int | 访谈模板ID |
| interviewTime | string | 访谈时间 |
| interviewResultDetails | string | 访谈结果详情 (HTML格式) |

---

## 2. 创建/更新访谈记录

```bash
# 创建
curl -s -X POST 'http://jerrypsy.top:8105/admin-api/psy/interview-record/create' \
  -H 'Authorization: Bearer <token>' \
  -H 'tenant-id: 163' \
  -H 'Content-Type: application/json' \
  -d '{
    "studentId": 119521,
    "interviewTemplateId": 11,
    "interviewTime": "2025-12-11 13:00:00",
    "interviewResultDetails": "<p>访谈内容...</p>"
  }'
```

---

## 3. 访谈模板

当前系统只有1个模板：
- **ID:** 11
- **名称:** 2025新生测评后访谈
- **人员范围:** 全校新生

模板内容（HTML格式）：
```html
<p>请简要描述学生基本情况：</p><p><br></p><br></p>
<p>该学生的风险等级为：</p><p><br></p><br></p>
<p>该学生的评估结论与建议为：</p><p><br></p><br></p>
```

---

## interviewResultDetails 访谈结果格式
访谈结果为HTML富文本，通常包含三段：
1. **学生基本情况描述** - 社交、学业、家庭等
2. **风险等级** - 高/中/低/无风险
3. **评估结论与建议** - 后续处理建议
