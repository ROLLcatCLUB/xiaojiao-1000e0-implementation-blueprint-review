# 1000A Xiaojiao Teacher Jarvis Workbench Execution Handoff

Date: 2026-06-12

Status: executable handoff for the next Codex session. This is not the 1000A audit result, not a seal, not a runtime apply, and not a UI implementation.

Primary source note:

- `docs/handoff/teacher_jarvis_workbench_planning_notes_1000_20260612.md`

Latest planning source:

- `C:\Users\Administrator\.codex\attachments\524084e7-581c-49ce-9a91-09d9f6834920\pasted-text.txt`

## Next Session Start Command

If a new Codex session needs to continue, use this exact instruction:

```text
Please execute:
1000_XIAOJIAO_TEACHER_JARVIS_WORKBENCH_PLANNING_PACKAGE_MILESTONE_1000A

Read first:
docs/handoff/xiaojiao_teacher_jarvis_workbench_1000A_execution_handoff_20260612.md
docs/handoff/teacher_jarvis_workbench_planning_notes_1000_20260612.md

Then generate the full 1000A concept contract review package.
Do not implement UI, do not connect runtime, do not run provider/model, do not write database/memory/Feishu, and do not perform blind repository rename.
```

## Task Identity

Planning package:

```text
1000_XIAOJIAO_TEACHER_JARVIS_WORKBENCH_PLANNING_PACKAGE
```

Executable milestone task:

```text
1000_XIAOJIAO_TEACHER_JARVIS_WORKBENCH_PLANNING_PACKAGE_MILESTONE_1000A
```

Current milestone:

```text
1000A_XIAOJIAO_TEACHER_JARVIS_WORKBENCH_CONCEPT_CONTRACT
```

Target final status:

```text
XIAOJIAO_TEACHER_JARVIS_WORKBENCH_CONCEPT_CONTRACT_PASS
```

Validator marker:

```text
ALL_1000A_XIAOJIAO_TEACHER_JARVIS_WORKBENCH_CONCEPT_CONTRACT_CHECKS_OK
```

## Goal

Generate the formal 1000A concept contract review package from the planning note.

This task is not:

- a small patch
- a UI implementation
- a teaching-planning page repair
- the narrow `0998N` follow-up
- a runtime integration
- a rename migration

This task is:

```text
concept-contract only
```

It should contract the system-level product shape:

```text
Xiaojiao Agent
+ teacher dynamic workspace
+ dynamic work panels
+ work objects
+ work actions
+ work state
+ work view composer
+ assistant surface
```

## Required Input Context

The next session must read:

```text
docs/handoff/teacher_jarvis_workbench_planning_notes_1000_20260612.md
```

It must absorb:

- `0998M` changed `教学工作计划` from one fixed template into part of an `education_work_plan` document family.
- `教学工作计划` is a role-scoped main document.
- `单元课时分配`, `学期周历表`, `课务日程表`, and `课表` are supporting artifacts and cannot replace the main document.
- The target is not a better chat page and not a better fixed module page.
- Conversation is input and confirmation, not the main content container.
- New product name is `小教智能体 / Xiaojiao Agent`.
- Old `小备 / Xiaobei` is legacy wording and a legacy internal namespace.
- Blind full-repository rename is forbidden.
- New teacher-facing copy must use `小教`.
- `Dynamic Work Panel` is not a fixed card.
- `周工作图谱` does not replace `学期周历表`.
- `学期周历表` is the semester progress supporting table.
- `周工作图谱` is a higher-level weekly work panel.

## Concepts Required In 1000A

Six primary concepts:

- `Unified Xiaojiao Agent / 统一小教智能体`
- `Agent-led Progressive Workspace / 小教主导的渐进式工作台`
- `Dynamic Work Panel / 动态工作面板`
- `Work Object / 工作对象`
- `Work Action / 工作动作`
- `Work State / 工作状态`

Two support concepts:

- `Work View Composer / 工作视图组合器`
- `Assistant Surface / 小教表层` or `Assistant Surface / 助手表层`

Concept relationship that must appear:

```text
Unified Xiaojiao Agent
-> leads Agent-led Progressive Workspace
-> organizes Dynamic Work Panel
-> displays Work Object
-> advances through Work Action
-> updates Work State
```

Product sentence that must be preserved in meaning:

```text
统一小教智能体根据工作状态，主导渐进式工作台，把教师的工作对象以动态工作面板呈现出来，并通过工作动作持续推进教师完成课前专业工作。
```

## Allowed Work

The next session may:

- add foundation docs
- add contract JSON
- add audit report/result/checklist
- add audit package manifest
- add ZIP package
- add validator
- optionally append handoff/README pointers to the created package
- self-run validator no-arg and `--root .`
- fix validator failures, maximum two rounds

## Forbidden Work

The next session must not:

- execute `0998N`
- implement UI
- modify real frontend pages
- modify old runtime
- connect provider/model
- connect classroom student runtime
- write database
- write memory
- write Feishu
- create formal export
- modify old sealed stages
- migrate old 0998N
- perform blind repository rename
- globally replace `小备` with `小教`
- put `Jarvis` into teacher-facing product copy
- make `Dynamic Work Panel` into fixed dead cards
- split Xiaojiao into multiple business agents
- return the system to a traditional module-menu page
- let chat history dominate the default primary workspace
- replace `学期周历表` with `周工作图谱`
- treat supporting tables as the teaching work plan main document

## Required Output Files

The next session must create:

```text
docs/foundation/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.md
docs/foundation/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.json
docs/audit/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A_report.md
docs/audit/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A_result.json
docs/audit/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A_checklist.json
docs/audit_packages/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A_manifest.json
docs/audit_packages/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.zip
scripts/validate_xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.py
```

Optional append-only updates:

```text
README.md
docs/handoff/teacher_jarvis_workbench_planning_notes_1000_20260612.md
```

If optional files are updated, only append created package location, final status, validator marker, ZIP path, and next stage. Do not rewrite old stage history.

## Contract Markdown Requirements

The markdown contract must contain at least:

1. `Stage Identity`
   - `stage_code`
   - `stage_name`
   - `final_status_target`
   - `stage_type=concept_contract_only`
   - `runtime_change_allowed=false`

2. `Background`
   - why not continue narrow `0998N` first
   - why `1000A` must lock product shape first
   - why this is not chat-page optimization or fixed-page optimization

3. `Product Identity`
   - `小教智能体 / Xiaojiao Agent`
   - `Jarvis` is internal metaphor only
   - teacher-facing copy must not use `Jarvis`

4. `Naming and Legacy Boundary`
   - new copy uses `小教`
   - old `xiaobei` is `legacy_internal_namespace`
   - blind full-repository rename is forbidden
   - rename is allowlist-based only

5. `Core Concepts`
   - define the six primary concepts in English and Chinese

6. `Supporting Concepts`
   - define `Work View Composer / 工作视图组合器`
   - define `Assistant Surface / 小教表层` or `助手表层`

7. `Concept Relationship`
   - include the relationship chain from Unified Xiaojiao Agent to Work State

8. `Assistant Surface Policy`
   - `collapsed`
   - `suggestion_bar`
   - `mini_chat_overlay`
   - `work_record_drawer`
   - default teacher experience is not full chat history
   - conversation is input and confirmation, not main content

9. `Dynamic Work Panel Contract`
   - stable envelope fields:
     - `panel_id`
     - `panel_type`
     - `artifact_type`
     - `title`
     - `status`
     - `mode`
     - `priority`
     - `context`
     - `visible_fields`
     - `hidden_fields`
     - `missing_info`
     - `available_actions`
     - `linked_objects`
     - `layout_region`
   - panel modes:
     - `empty`
     - `intake`
     - `draft`
     - `working`
     - `review`

10. `Teacher Workbench Positioning`
    - teaching planning upgrades to teacher daily workbench / teacher home
    - current focus is pre-class professional work
    - classroom design, classroom execution, and evaluation are later submodules
    - current stage does not connect student-side classroom runtime

11. `Pre-Class Work Chain`
    - `teacher role profile`
    - `semester teaching work plan`
    - `unit lesson allocation`
    - `semester weekly calendar`
    - `weekly work graph`
    - `today work items`
    - `lesson design`
    - `learning task sheet`
    - `evaluation rubric`
    - `classroom preparation package`

12. `Weekly Work Graph Definition`
    - weekly work graph does not replace semester weekly calendar
    - semester weekly calendar is a progress supporting table
    - weekly work graph is a higher-level weekly task panel

13. `Today Work Item Definition`
    - `prepare_lesson`
    - `design_learning_task`
    - `prepare_resource`
    - `evaluate_student_work`
    - `adjust_plan`
    - `submit_material`
    - `review_progress`
    - `handle_issue`
    - `plan_activity`
    - `generate_document`
    - `reflect_and_summarize`

14. `QuickClass Boundary`
    - QuickClass focuses on classroom execution and learning analytics
    - Xiaojiao currently focuses on pre-class teacher professional work
    - no QuickClass-like classroom execution system in this stage

15. `Prohibited Patterns`
    - at least 20 entries

16. `Future Milestones`
    - `1000B_EDUCATION_PRE_CLASS_WORK_SAMPLE_ROOM_BUSINESS_STRUCTURE`
    - `1000C_DYNAMIC_WORK_PANEL_CONTRACT`
    - `1000D_AGENT_ACTION_POLICY_AND_WORK_STATE_CONTRACT`
    - `1000E_ART_TEACHER_PRE_CLASS_WORKBENCH_PILOT`

17. `Validation Requirements`
    - list validator checks clearly

## Contract JSON Requirements

The JSON contract must include at least:

- `stage_code`
- `stage_name`
- `stage_type`
- `final_status_target`
- `source_handoff`
- `product_identity`
- `naming_policy`
- `legacy_namespace_policy`
- `internal_metaphor_policy`
- `core_concepts`
- `supporting_concepts`
- `concept_relationship`
- `assistant_surface_states`
- `dynamic_work_panel_contract`
- `panel_modes`
- `work_object_contract`
- `work_action_contract`
- `work_state_contract`
- `workbench_positioning`
- `pre_class_work_chain`
- `weekly_work_graph_definition`
- `today_work_item_definition`
- `quickclass_boundary`
- `prohibited_patterns`
- `future_milestones`
- `boundary_flags_required`
- `validation_requirements`

Required values:

```text
stage_code=1000A_XIAOJIAO_TEACHER_JARVIS_WORKBENCH_CONCEPT_CONTRACT
final_status_target=XIAOJIAO_TEACHER_JARVIS_WORKBENCH_CONCEPT_CONTRACT_PASS
stage_type=concept_contract_only
runtime_change_allowed=false
ui_implementation_allowed=false
provider_call_allowed=false
database_write_allowed=false
memory_write_allowed=false
feishu_write_allowed=false
formal_export_allowed=false
classroom_student_runtime_allowed=false
full_repo_blind_rename_allowed=false
```

## Checklist Requirements

`checklist.json` must check:

- stage identity
- product identity
- naming policy
- legacy namespace policy
- internal Jarvis metaphor policy
- six core concepts
- two supporting concepts
- assistant surface states
- dynamic work panel envelope
- panel modes
- work object contract
- work action contract
- work state contract
- teacher workbench positioning
- pre-class work chain
- weekly work graph relation
- today work item definition
- QuickClass boundary
- prohibited patterns
- future milestones
- no UI implementation
- no runtime change
- no provider call
- no database write
- no memory write
- no Feishu write
- no formal export
- no classroom student runtime
- no blind rename
- manifest / ZIP alignment

## Result JSON Requirements

`result.json` must include:

- `stage_code`
- `final_status`
- `pass`
- `concept_contract_created`
- `json_contract_created`
- `checklist_created`
- `report_created`
- `manifest_created`
- `zip_created`
- `validator_created`
- `naming_policy_pass`
- `legacy_namespace_policy_pass`
- `internal_metaphor_policy_pass`
- `core_concepts_pass`
- `supporting_concepts_pass`
- `assistant_surface_pass`
- `dynamic_work_panel_pass`
- `workbench_positioning_pass`
- `pre_class_work_chain_pass`
- `weekly_work_graph_pass`
- `today_work_items_pass`
- `quickclass_boundary_pass`
- `prohibited_patterns_pass`
- `future_milestones_pass`
- `validator_no_arg_pass`
- `validator_root_pass`
- `manifest_zip_alignment_pass`
- `forbidden_files_pass`
- `boundary_flags`

Boundary flags must be safe:

```text
database_written=false
memory_written=false
feishu_written=false
formal_export_created=false
classroom_student_runtime_connected=false
provider_called=false
frontend_runtime_modified=false
backend_runtime_modified=false
old_sealed_stage_modified=false
full_repo_blind_rename_performed=false
teacher_facing_jarvis_wording_introduced=false
teacher_facing_xiaobei_wording_introduced=false
```

## Validator Requirements

Validator path:

```text
scripts/validate_xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.py
```

Must support:

```text
python scripts/validate_xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.py
python scripts/validate_xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.py --root .
```

Validator must check:

- required files exist
- contract markdown exists
- contract JSON exists
- checklist JSON exists
- result JSON exists
- report markdown exists
- manifest JSON exists
- ZIP exists
- `stage_code` consistency
- `final_status_target` correctness
- `stage_type=concept_contract_only`
- UI implementation is not allowed
- runtime change is not allowed
- provider call is not allowed
- database write is not allowed
- memory write is not allowed
- Feishu write is not allowed
- formal export is not allowed
- classroom student runtime is not allowed
- blind full repository rename is not allowed
- all six primary English concepts exist
- all six primary Chinese concepts exist
- both support English concepts exist
- both support Chinese concepts exist
- assistant surface states include `collapsed`, `suggestion_bar`, `mini_chat_overlay`, `work_record_drawer`
- dynamic work panel envelope fields exist
- panel modes include `empty`, `intake`, `draft`, `working`, `review`
- pre-class work chain exists
- weekly work graph definition exists and explicitly does not replace `semester_weekly_calendar`
- today work item definition exists
- QuickClass boundary exists
- prohibited patterns count is at least 20
- future milestones include `1000B`, `1000C`, `1000D`, `1000E`
- result boundary flags are safe
- no `.env`, token, or secret files
- ZIP contains no absolute paths
- `manifest_minus_zip=[]`
- `zip_minus_manifest=[]`
- marker output exactly:

```text
ALL_1000A_XIAOJIAO_TEACHER_JARVIS_WORKBENCH_CONCEPT_CONTRACT_CHECKS_OK
```

## Manifest And ZIP Requirements

Manifest must record:

- `package_name`
- `stage_code`
- `generated_at`
- `entries`
- file size
- SHA256
- `zip_entry_count`
- `manifest_minus_zip`
- `zip_minus_manifest`

ZIP requirements:

- relative paths only
- use `/` path separators
- no absolute paths
- no `.env`
- no token or secret files
- no database files
- no real student data
- can be opened directly in Windows Explorer

## Report Requirements

The report must explain:

- what 1000A completed
- what 1000A did not do
- why 1000A must come before narrow `0998N`
- Xiaojiao naming boundary
- `Jarvis` as internal metaphor only
- six primary concepts and two support concepts
- relationship between weekly work graph and semester weekly calendar
- QuickClass boundary
- validator results
- manifest / ZIP alignment
- next recommended stage

Next recommended stage must be:

```text
1000B_EDUCATION_PRE_CLASS_WORK_SAMPLE_ROOM_BUSINESS_STRUCTURE
```

## Completion Reply Format

After finishing 1000A, the next session should report only:

- `final_status`
- validator no-arg result
- validator `--root` result
- ZIP path
- `ZIP_ENTRY_COUNT`
- `manifest_minus_zip`
- `zip_minus_manifest`
- marker
- changed files count
- whether README / handoff was updated
- `next_stage=1000B_EDUCATION_PRE_CLASS_WORK_SAMPLE_ROOM_BUSINESS_STRUCTURE`

Do not enter 1000B in the same milestone report unless explicitly instructed.

