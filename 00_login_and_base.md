# 华心云 (HXCloud) - 登录与基础信息

## 系统信息
- **前端地址:** http://jerrypsy.top:8105/
- **API基础路径:** `http://jerrypsy.top:8105/admin-api`
- **前端框架:** Vue.js (Vite构建，SPA)
- **后端框架:** 类似 ruoyi-vue-pro (芋道框架)

## 登录凭据
| 项目 | 值 |
|------|-----|
| 租户名称 | 西华大学 |
| 租户ID | 163 |
| 用户名 | 0720200029 |
| 密码 | Admin.123456 |
| 用户ID | 155 |
| 姓名 | 王中瑞 |
| 角色 | zixunshi (咨询师) |

## 一键登录 API

### Step 1: 获取租户ID
```bash
curl -s 'http://jerrypsy.top:8105/admin-api/system/tenant/get-id-by-name?name=%E8%A5%BF%E5%8D%8E%E5%A4%A7%E5%AD%A6'
# 返回: {"code":0,"msg":"","data":163}
```

### Step 2: 登录获取Token
```bash
curl -s -X POST 'http://jerrypsy.top:8105/admin-api/system/auth/login' \
  -H 'Content-Type: application/json' \
  -H 'tenant-id: 163' \
  -d '{"username":"0720200029","password":"Admin.123456"}'
# 返回:
# {
#   "code": 0,
#   "data": {
#     "userId": 155,
#     "accessToken": "xxx",
#     "refreshToken": "xxx",
#     "expiresTime": 1783257372252
#   }
# }
```

### Step 3: 获取用户权限
```bash
curl -s 'http://jerrypsy.top:8105/admin-api/system/auth/get-permission-info' \
  -H 'Authorization: Bearer <accessToken>' \
  -H 'tenant-id: 163'
```

## 通用请求头
所有需要认证的接口都需要携带:
```
Authorization: Bearer <accessToken>
tenant-id: 163
Content-Type: application/json
```

## 系统模块一览
| 模块前缀 | 说明 |
|----------|------|
| `/system/` | 系统管理（用户、租户、角色、权限） |
| `/psa/` | 预约排班模块（排班、预约、咨询记录） |
| `/psy/` | 心理咨询模块（访谈模板、访谈记录、来访者、危机干预） |
| `/psc/` | 学生管理模块（学生信息、咨询师管理） |
| `/pss/` | 心理测评模块（测评计划、测评查询） |
| `/psm/` | 月报管理模块（月报记录、月报详情、关注名单） |
| `/infra/` | 基础设施（文件上传等） |

## 枚举值速查

### 状态类
- `monthRecordDetailStatus`: `counselor_collect`(待咨询师确认) → `instructor_collect`(待辅导员确认) → `done`(完成)
- `psmMonthRecordStatus`: `collecting`(采集中), `done`(已完成)
- `consultRecordStatus`: `wancheng`(完成)
- `appointRecordStatus`: `wancheng`(完成)

### 风险等级
- `crisisLevel`: `none`, `low`, `medium`, `high`
- `suicideInjuryRiskType`: `none`(无), 其他等级
- `riskType`: `wufengxian`(无风险), 其他

### 学生信息
- `focusReasonType`: `xueye`(学业), `ceping`(测评), 其他
- `healthType`: `lianghao`(良好), 其他
- `learningStatus`: `zhongdeng`(中等), 其他
- `roommateStatus`: `rongqia`(融洽), `lianghao`(良好), 其他
- `homeStatus`: `hexie`(和谐), `todo`(待填), 其他
- `growthStatus`: `fumu`(父母), 其他
- `homeEconomyStatus`: `zhongdeng`(中等), `kunnan`(困难), 其他
- `psychiatricDiagnosis`: `sleep`(睡眠), `none`(无), 其他
- `medicationStatus`: `under`(服药中), `none`(无), 其他
- `familyStructure`: `wanzheng`(完整), 其他
- `crisisPlanLevel`: `three`(三级), 其他
- `instructorHandlingMethod`: `level5`(五级), 其他
- `instructorRemoveStatus`: `putong`(普通), 其他

### 区域/年级
- `districtCode`: `pidu`(郫都), 其他
- `gradeCode`: `2024`, `2025` 等
- `cultivationLevel`: `benke`(本科), `yuke`(预科), 其他
