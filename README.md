# Xiaojiao 1000E0 Implementation Blueprint Review

This repository is a dedicated GitHub review area for:

1000E0_ART_TEACHER_PRE_CLASS_WORKBENCH_IMPLEMENTATION_BLUEPRINT

It is not the full xiaobei-core source repository.

## Stage

| Stage | final_status | Validator marker |
| --- | --- | --- |
| 1000E0_ART_TEACHER_PRE_CLASS_WORKBENCH_IMPLEMENTATION_BLUEPRINT | XIAOJIAO_ART_TEACHER_PRE_CLASS_WORKBENCH_IMPLEMENTATION_BLUEPRINT_PASS | ALL_1000E0_ART_TEACHER_PRE_CLASS_WORKBENCH_IMPLEMENTATION_BLUEPRINT_CHECKS_OK |

## Validator commands

`powershell
python scripts/validate_xiaojiao_art_teacher_pre_class_workbench_implementation_blueprint_1000E0.py
python scripts/validate_xiaojiao_art_teacher_pre_class_workbench_implementation_blueprint_1000E0.py --root .
`

## ZIP artifact

docs/audit_packages/xiaojiao_art_teacher_pre_class_workbench_implementation_blueprint_1000E0.zip

SHA256:

`	ext
4B7E6AF66039B6C39A65D706139773FB0DD077B2F838ADBBFCFE6BCBCF0469F9
`

## Review focus

请审核 1000E0 是否足够作为 1000E1 静态工作台布局 mock 前的 implementation blueprint：

- artifact schemas 是否补足教学工作计划、单元课时分配、学期周历表、周工作图谱、今日工作项、课时设计、学习单、评价量规、课堂准备包
- 三个核心面板样例是否足够：教学工作计划动态面板、周工作图谱动态面板、今日工作项面板
- 三类真实输入场景是否覆盖：生成教学工作计划、拆成周工作图谱、生成今日工作项
- Work State -> Panel -> Action 状态转移表是否能指导 1000E1/1000E2
- panel mode 变化规则和 available_actions 规则是否合理
- 是否继续守住硬边界：不写 UI、不接 runtime/provider/model/database/memory/Feishu/formal export/课堂学生端、不 blind rename
- 是否可以进入 1000E1_ART_TEACHER_PRE_CLASS_WORKBENCH_STATIC_LAYOUT_MOCK_PENDING_REVIEW

注意：这里是 review area，不是完整源码仓库。1000E0 是 implementation blueprint，不是 UI/runtime apply。