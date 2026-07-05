# 华心云 - 全量 API 接口地图

## 系统模块 (/system/)

### 认证相关
| 方法 | 路径 | 说明 |
|------|------|------|
| POST | `/system/auth/login` | 登录 |
| GET | `/system/auth/get-permission-info` | 获取用户权限信息 |
| POST | `/system/auth/logout` | 登出 |
| GET | `/system/auth/refresh-token?refreshToken=` | 刷新Token |
| POST | `/system/auth/register` | 注册 |
| POST | `/system/auth/reset-password` | 重置密码 |
| POST | `/system/auth/send-sms-code` | 发送短信验证码 |
| POST | `/system/auth/sms-login` | 短信登录 |
| POST | `/system/auth/social-login` | 社交登录 |

### 租户相关
| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/system/tenant/get-id-by-name?name=` | 根据名称获取租户ID |
| GET | `/system/tenant/get-by-website?website=` | 根据网站获取租户 |

### 验证码
| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/system/captcha/get` | 获取验证码（需登录） |
| POST | `/system/captcha/check` | 验证码校验 |

---

## 预约排班模块 (/psa/)

### 排班管理
| 方法 | 路径 | 说明 | 权限 |
|------|------|------|------|
| GET | `/psa/schedule-standard/page` | 排班标准列表 | psa:schedule-standard:query |
| POST | `/psa/schedule-standard/create` | 创建排班 | psa:schedule-standard:create |
| POST | `/psa/schedule-standard/update` | 更新排班 | psa:schedule-standard:update |
| GET | `/psa/schedule-standard/delete?id=` | 删除排班 | psa:schedule-standard:delete |
| GET | `/psa/schedule-standard/export-excel` | 导出排班 | psa:schedule-standard:export |

### 咨询记录（consult-record）
| 方法 | 路径 | 说明 | 权限 |
|------|------|------|------|
| GET | `/psa/consult-record/page` | 咨询记录列表 | - |
| GET | `/psa/consult-record/get?id=` | 获取单条 | - |
| GET | `/psa/consult-record/getConsultRecordByAppointId?appointRecordId=` | 按预约查 | - |
| POST | `/psa/consult-record/create` | 创建记录 | - |
| POST | `/psa/consult-record/createEmergencyConsultRecord` | 创建紧急记录 | - |
| POST | `/psa/consult-record/update` | 更新记录 | - |
| GET | `/psa/consult-record/delete?id=` | 删除记录 | - |
| GET | `/psa/consult-record/export-excel` | 导出 | - |

### 咨询视图 (consult-view) — 只读联合查询
| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/psa/consult-view/page` | 咨询记录+预约+学生 联合查询 |

---

## 心理咨询模块 (/psy/)

### 访谈模板 (interview-template)
| 方法 | 路径 | 说明 | 权限 |
|------|------|------|------|
| GET | `/psy/interview-template/page` | 模板列表 | psy:interview-template:query |
| GET | `/psy/interview-template/get?id=` | 获取模板 | - |
| POST | `/psy/interview-template/create` | 创建模板 | psy:interview-template:create |
| POST | `/psy/interview-template/update` | 更新模板 | psy:interview-template:update |
| GET | `/psy/interview-template/delete?id=` | 删除模板 | psy:interview-template:delete |
| GET | `/psy/interview-template/export-excel` | 导出 | psy:interview-template:export |

### 访谈记录 (interview-record)
| 方法 | 路径 | 说明 | 权限 |
|------|------|------|------|
| GET | `/psy/interview-record/page` | 记录列表 | psy:interview-record:query |
| GET | `/psy/interview-record/page_my` | 我的记录 | - |
| GET | `/psy/interview-record/get?id=` | 获取记录 | - |
| POST | `/psy/interview-record/create` | 创建记录 | psy:interview-record:create |
| POST | `/psy/interview-record/update` | 更新记录 | psy:interview-record:update |
| GET | `/psy/interview-record/delete?id=` | 删除记录 | psy:interview-record:delete |
| GET | `/psy/interview-record/export-excel` | 导出 | psy:interview-record:export |

### 来访者管理 (my-visitor)
| 方法 | 路径 | 说明 | 权限 |
|------|------|------|------|
| GET | `/psy/my-visitor/page` | 来访者列表 | psy:my-visitor:query |
| POST | `/psy/my-visitor/create` | 创建 | psy:my-visitor:create |
| POST | `/psy/my-visitor/update` | 更新 | psy:my-visitor:update |
| GET | `/psy/my-visitor/delete?id=` | 删除 | psy:my-visitor:delete |
| GET | `/psy/my-visitor/export-excel` | 导出 | psy:my-visitor:export |

### 危机干预 (crisis-intervention)
| 方法 | 路径 | 说明 | 权限 |
|------|------|------|------|
| GET | `/psy/crisis-intervention/page` | 列表 | psy:crisis-intervention:all |
| POST | `/psy/crisis-intervention/create` | 创建 | psy:crisis-intervention:create |
| POST | `/psy/crisis-intervention/update` | 更新 | psy:crisis-intervention:update |
| GET | `/psy/crisis-intervention/export-excel` | 导出 | psy:crisis-intervention:export |

---

## 学生管理模块 (/psc/)

### 学生信息 (student)
| 方法 | 路径 | 说明 | 权限 |
|------|------|------|------|
| GET | `/psc/student/page` | 学生列表 | psc:student:query |
| POST | `/psc/student/create` | 创建 | psc:student:create |
| POST | `/psc/student/update` | 更新 | psc:student:update |
| GET | `/psc/student/export-excel` | 导出 | psc:student:export |

---

## 心理测评模块 (/pss/)

### 测评计划 (survey-distributions-admin)
| 方法 | 路径 | 说明 | 权限 |
|------|------|------|------|
| GET | `/pss/survey-distributions-admin/page` | 测评计划列表 | pss:survey-distributions-admin:query |
| POST | `/pss/survey-distributions-admin/start-test` | 启动测评 | pss:survey-distributions:start-test |
| GET | `/pss/survey-distributions-admin/export-finished` | 导出已完成 | pss:survey-distributions:export-finished |

---

## 月报管理模块 (/psm/) ⭐

### 月报记录 (month-record)
| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/psm/month-record/page` | 月报列表 |
| GET | `/psm/month-record/get?id=` | 月报详情 |

### 月报详情 (month-record-detail) — ⭐ 核心
| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/psm/month-record-detail/page` | 详情列表（支持多种过滤） |
| GET | `/psm/month-record-detail/get?id=` | 单条详情 |
| POST | `/psm/month-record-detail/create` | 创建 |
| POST | `/psm/month-record-detail/updateByCounselor` | ⭐ **咨询师确认** |
| POST | `/psm/month-record-detail/updateByInstructor` | 辅导员填写 |
| GET | `/psm/month-record-detail/reset?id=` | 重置 |
| GET | `/psm/month-record-detail/delete?id=` | 删除 |
| GET | `/psm/month-record-detail/export-excel` | 导出 |

---

## 基础设施 (/infra/)
| 方法 | 路径 | 说明 |
|------|------|------|
| POST | `/infra/file/upload` | 文件上传 |

---

## 数据字典 (系统内置)
| 字典类型 | 说明 |
|----------|------|
| `psa_consult_record_status` | 咨询记录状态 |
| `psa_consulting_question_type` | 咨询问题类型 |
| `psa_consulting_type` | 咨询类型 |
| `psa_risk_type` | 风险类型 |
| `psm_crisis_level` | 危机等级 |
| `psm_focus_reason_type` | 关注原因类型 |
| `psm_health_type` | 健康类型 |
| `psm_learning_status` | 学习状态 |
| `psm_roommate_status` | 室友状态 |
| `psm_home_status` | 家庭状态 |
| `psm_growth_status` | 成长状态 |
| `psm_home_economy_status` | 家庭经济状况 |
| `psm_family_structure` | 家庭结构 |
| `psm_focus_status` | 关注状态 |
| `psm_focus_type` | 关注类型 |
| `psm_instructor_handling_method` | 辅导员处理方式 |
| `psm_danger_measure_level` | 危险措施等级 |
| `psm_crisis_reporting_method` | 危机报告方式 |
| `common_status` | 通用状态 |
| `system_user_sex` | 性别 |
