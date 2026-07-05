# 华心云 - 数据字典完整参考

> 通过 `GET /system/dict-data/simple-list` 接口获取

## 1. 月报状态 (`psm_month_record_status`)
| 值 | 标签 | 说明 |
|-----|------|------|
| `collecting` | 收集中 | 月报正在收集 |
| `done` | 完成 | 月报已收集完成 |

## 2. 月报明细状态 (`psm_month_record_detail_status`)
| 值 | 标签 | 说明 |
|-----|------|------|
| `instructor_collect` | 待辅导员确认 | 辅导员需填写 |
| `counselor_collect` | 待咨询师确认 | 辅导员已填完 |
| `done` | 完成 | 流程结束 |

## 3. 关注原因 (`psm_focus_reason_type`)
| 值 | 标签 |
|-----|------|
| `qingxu` | 情绪异常 |
| `xueye` | 学业困难 |
| `xingwei` | 行为异常 |
| `weiji` | 危机干预 |
| `ceping` | 测评预警 |
| `fangtan` | 新生访谈 |
| `qita` | 其他 |
| `todo` | 待完善 |

## 4. 身体状态 (`psm_health_type`)
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
| `others` | 其他 |
| `todo` | 待完善 |

## 5. 学习状况 (`psm_learning_status`)
| 值 | 标签 |
|-----|------|
| `lianghao` | 成绩良好 |
| `zhongdeng` | 成绩中等 |
| `jiaocha` | 成绩较差 |
| `guake` | 多次挂科 |
| `jinggao` | 学业警告 |
| `quexaxingqu` | 缺乏学习兴趣 |
| `zhiyemimang` | 职业生涯迷茫 |
| `others` | 其他 |
| `todo` | 待完善 |

## 6. 舍友关系 (`psm_roommate_status`)
| 值 | 标签 |
|-----|------|
| `rongqia` | 关系融洽 |
| `lianghao` | 关系良好 |
| `yiban` | 关系一般 |
| `shuyuan` | 关系疏远 |
| `chongtu` | 关系紧张 |
| `gudu` | 缺乏同伴，感到孤独 |
| `fuza` | 同伴关系复杂 |
| `others` | 其他 |
| `todo` | 待完善 |

## 7. 家庭情况 (`psm_home_status`)
| 值 | 标签 |
|-----|------|
| `hexie` | 家庭关系和谐 |
| `jinzhang` | 父母经常争吵 |
| `damo` | 家庭关系淡漠 |
| `baoli` | 家庭暴力环境 |
| `others` | 其他 |
| `todo` | 待完善 |

## 8. 成长情况 (`psm_growth_status`)
| 值 | 标签 |
|-----|------|
| `fumu` | 跟随父母长大 |
| `danqin` | 单亲养育 |
| `liushou` | 留守养育 |
| `jiyang` | 寄养或领养 |
| `others` | 其他 |
| `todo` | 待完善 |

## 9. 家庭经济 (`psm_home_economy_status`)
| 值 | 标签 |
|-----|------|
| `fuyu` | 较为富裕 |
| `zhongdeng` | 中等收入 |
| `kunnan` | 有些困难 |
| `feichangkunnan` | 非常困难 |
| `others` | 其他 |
| `todo` | 待完善 |

## 10. 自杀/伤人风险 (`psm_suicide_injury_risk_type`)
| 值 | 标签 |
|-----|------|
| `none` | 无自伤或伤人想法 |
| `notnow` | 现在没有，但曾有尝试 |
| `recentidea` | 近期有自伤想法，一闪而过 |
| `recentthought` | 近期常有自杀观念，无计划 |
| `recentplan` | 近期有自杀计划，未尝试 |
| `harm` | 近期有自伤行为(非自杀目的) |
| `changshi` | 近期有自杀尝试 |
| `harmothers` | 有伤人观念，无明确计划 |
| `harmplan` | 有伤人计划，未实施 |
| `harmaction` | 已实施伤人行为 |

## 11. 危机等级 (`psm_crisis_level`)
| 值 | 标签 |
|-----|------|
| `none` | 无风险 |
| `low` | 低风险 |
| `mid` | 中风险 |
| `high` | 高风险 |

## 12. 精神科诊断 (`psm_psychiatric_diagnosis`)
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

## 13. 服药情况 (`psm_medication_status`)
| 值 | 标签 |
|-----|------|
| `none` | 未服药 |
| `under` | 正在服药 |
| `tingyao` | 自行停药 |
| `yizhu` | 遵医嘱停药 |
| `others` | 其他 |
| `todo` | 待完善 |

## 14. 家庭结构 (`psm_family_structure`)
| 值 | 标签 |
|-----|------|
| `wanzheng` | 完整家庭 |
| `chongzu` | 重组家庭 |
| `qushi` | 单亲或双亲去世 |
| `liyi` | 父母离异或分居 |
| `others` | 其他 |
| `todo` | 待完善 |

## 15. 危机预案等级 (`psm_danger_measure_level`)
| 值 | 标签 | 说明 |
|-----|------|------|
| `three` | 三级预案 | 无风险，非突破保密情形 |
| `two` | 二级预案 | 有风险，辅导员关注 |
| `one` | 一级预案 | 已实施行为，各部门协同 |

## 16. 辅导员移除建议 (`psm_instructor_remove_status`)
| 值 | 标签 |
|-----|------|
| `putong` | 普通确认（继续关注） |
| `jianyi_yichu` | 建议出库 |

## 17. 移除原因 (`psm_remove_reason`)
| 值 | 标签 |
|-----|------|
| `stable` | 情况稳定 |
| `graduate` | 毕业 |
| `dropout` | 退学 |
| `others` | 其他 |
| `todo` | 待完善 |

## 18. 辅导员处理方式 (`psm_instructor_handling_method`)
| 值 | 标签 | 说明 |
|-----|------|------|
| `level1` | 1级 | 通知家长+学校，24小时防控/送医，启动危机干预 |
| `level2` | 2级 | 通知家长+学校，告知风险，给予建议 |
| `level3` | 3级 | 辅导员持续关注追踪 |
| `level4` | 4级 | 保持关注，正常自我成长 |
| `level5` | 5级 | 正常范围，无需特殊处理 |
| `others` | 其他 | - |
| `todo` | 待完善 | - |

---

## 咨询相关字典

### 咨询问题类型 (`psa_consulting_question_type`)
| 值 | 标签 |
|-----|------|
| `xinli` | 心理 |
| `qingxu` | 情绪 |
| `renji` | 人际 |
| `xueye` | 学业 |
| `lianai` | 恋爱 |
| `jiating` | 家庭 |
| `shengya` | 生涯 |
| `qita` | 其他 |

### 风险类型 (`psa_risk_type`)
| 值 | 标签 |
|-----|------|
| `wufengxian` | 无风险 |
| `difengxian` | 低风险 |
| `zhongfengxian` | 中风险 |
| `gaofengxian` | 高风险 |

### 咨询类型 (`psa_consulting_type`)
| 值 | 标签 |
|-----|------|
| `geti` | 个体 |
| `tuanti` | 团体 |

### 咨询记录状态 (`psa_consult_record_status`)
| 值 | 标签 |
|-----|------|
| `wancheng` | 完成 |
| `weibao` | 未报到 |

### 性别 (`system_user_sex`)
| 值 | 标签 |
|-----|------|
| `1` | 男 |
| `2` | 女 |
