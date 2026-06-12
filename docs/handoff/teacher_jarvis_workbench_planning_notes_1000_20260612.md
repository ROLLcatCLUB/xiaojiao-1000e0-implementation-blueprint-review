# Xiaojiao Teacher Jarvis Workbench Planning Notes 1000

Date: 2026-06-12

Status: planning note only. This file is a handoff and task-basis note, not an audit package, validator result, seal, or runtime apply.

Source materials recorded from:

- `C:\Users\Administrator\.codex\attachments\1aad84bd-4755-4d13-8643-73bdbea130c0\pasted-text.txt`
- `C:\Users\Administrator\.codex\attachments\c04246d0-ed88-4506-8b11-f230a23427a2\pasted-text.txt`
- `C:\Users\Administrator\.codex\attachments\c6eb2f0c-3019-4fd8-a43a-e67de3bcbef9\pasted-text.txt`
- `C:\Users\Administrator\.codex\attachments\8267bcc9-2c1d-4390-9980-15d08d1f6980\pasted-text.txt`
- `C:\Users\Administrator\.codex\attachments\03167607-bfef-47ac-b197-17b5ee9c1901\pasted-text.txt`

## Current Baseline

The current teaching-planning line has already moved past the narrow "generate a planning reply" shape.

Known recent baseline:

- `0998K_TEACHING_PLANNING_RESOURCE_CONTEXT_TO_PRECISION_CANDIDATE_READONLY_PILOT`
- `0998L_TEACHING_PLANNING_PRECISION_CANDIDATE_EDIT_AND_REPAIR_READONLY`
- `0998M_EDUCATION_WORK_PLAN_FAMILY_AND_VARIANT_REGISTRY_CONTRACT`

Important 0998M meaning:

```text
教学工作计划 is no longer treated as one fixed template.
It is part of an education_work_plan document family.
```

Supporting artifacts stay useful, but they do not replace the main document:

```text
教学工作计划 = role-scoped main document
单元课时分配 = supporting artifact
学期周历表 = supporting artifact
课务日程表 = supporting artifact
课表 = supporting artifact
```

## Product Direction

The next product direction is not "a better chat page" and not "a better fixed module page".

The target shape is:

```text
Unified Xiaojiao Agent
-> understands the teacher's current work
-> organizes work objects
-> composes dynamic work panels
-> exposes next actions only when useful
-> uses conversation as input and confirmation, not as the main content container
```

Product definition:

```text
小教智能体 is a Jarvis-like teacher workspace agent.
It is a work director, view director, and action coordinator.
It is not only a chat box, not a static page system, and not many fragmented business agents.
```

The teacher-facing workspace should show the current work state, not a long chat transcript.

The old product name `小备 / Xiaobei` is now treated as historical wording and a legacy internal namespace unless a later allowlisted migration changes it.

## Core Objects To Preserve

The next system-level design should define these objects before UI implementation:

- `Unified Xiaojiao Agent / 统一小教智能体`: one assistant identity across teaching planning, teaching design, classroom design, evaluation, and resources.
- `Agent-led Progressive Workspace / 小教主导的渐进式工作台`: the workspace is organized by task state, not by fixed page order.
- `Work Object`: the business object being worked on, such as a semester work plan, weekly work graph, evaluation rubric, or classroom preparation package.
- `Dynamic Work Panel`: a task-aware view container controlled by the Agent and renderer contract.
- `Work Action`: an available next action such as generate draft, revise section, derive weekly calendar, supplement textbook catalog, prepare export, or inspect gaps.
- `Work State`: the current known slots, missing information, generated candidates, linked artifacts, risks, and next actions.
- `Work View Composer`: the layer that converts work state into visible panels and layout priority.
- `Assistant Surface`: a lightweight suggestion, confirmation, or input surface, not a permanent large chat-history container.

Compressed relationship:

```text
Unified Xiaojiao Agent / 统一小教智能体
-> leads Agent-led Progressive Workspace / 小教主导的渐进式工作台
-> organizes Dynamic Work Panel / 动态工作面板
-> displays Work Object / 工作对象
-> advances through Work Action / 工作动作
-> updates Work State / 工作状态
```

One-sentence definition:

```text
统一小教智能体根据工作状态，主导渐进式工作台，把教师的工作对象以动态工作面板呈现出来，并通过工作动作持续推进教师完成课前专业工作。
```

## Naming and Legacy Boundary

From 1000A forward, the product agent name is:

```text
Chinese: 小教智能体
English: Xiaojiao Agent
```

Required new wording:

- `小教`
- `小教智能体`
- `统一小教智能体`
- `Xiaojiao Agent`
- `xiaojiao_agent`
- `小教主导的渐进式工作台`
- `小教建议条`
- `小教工作记录`

Legacy wording:

- `小备`
- `小备 Agent`
- `统一小备智能体`
- `Xiaobei Agent`
- `xiaobei_agent`
- `小备主导的渐进式工作台`
- `小备建议条`
- `小备工作记录`

Must use new naming in:

- new planning package titles
- new concept contracts
- new schemas
- new teacher-facing frontend copy
- new UI component display names
- new audit, report, result, checklist, and manifest concept descriptions

Do not force rename yet:

- `xiaobei-core` repository name
- old stage file names
- old validator markers
- old audit packages
- old sealed contracts
- existing import paths
- historical README stage records

Hard naming rules:

- Teacher-facing primary experience must not show `小备` in new work.
- New teacher-facing copy must use `小教`.
- New system concepts must use `Xiaojiao`.
- If an internal module still references the `xiaobei` namespace, new docs must mark `legacy_internal_namespace=true`.
- Blind full-repository find/replace is forbidden.
- Renaming must be allowlist-based.
- 1000A defines the naming boundary; it does not perform a broad rename migration.

## Dynamic Work Panel Meaning

Do not treat "card" as a fixed UI card.

Use:

```text
Dynamic Work Panel
动态工作面板
```

A panel has a stable envelope:

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

But the visible fields and actions are dynamic. They depend on:

- teacher role
- work scope
- current task
- known slots
- missing information
- generated candidates
- linked supporting artifacts
- review/export readiness

Panel modes should include at least:

- `empty`: show what this work object can do.
- `intake`: show known slots, missing information, and recommended next action.
- `draft`: show generated summary, section state, and linked artifacts.
- `working`: show current tasks, pending actions, and work graph.
- `review`: show full content, gaps, revision actions, and export readiness.

## Teaching Planning Implication

The previous teaching-planning UI should not become the final mental model.

The tab row remains important for the current teacher experience and must not be casually removed:

```text
教学工作计划 / 课务日程表 / 单元课时分配 / 学期周历表 / 课表
```

But in the next workspace design, these should become linked work panels and supporting artifacts under the teacher's current task, rather than isolated fixed pages.

Teaching planning becomes the first deep sample room, not a permanent island:

```text
general Agent semantic foundation
+ teacher work objects
+ dynamic panels
+ teaching planning as the first deep pilot
```

## Proposed Planning Package

Recommended new planning package:

```text
1000_XIAOJIAO_TEACHER_JARVIS_WORKBENCH_PLANNING_PACKAGE
```

Chinese name:

```text
小教教师 Jarvis 式动态工作台规划包
```

Overall goal:

```text
Upgrade the legacy "left-side large chat + right-side business page"
to a unified Xiaojiao Agent-led teacher dynamic workspace.
```

## Proposed Milestones

### 1000A_XIAOJIAO_TEACHER_JARVIS_WORKBENCH_CONCEPT_CONTRACT

Goal: lock the product concept and boundary before implementation.

Expected deliverables:

- `docs/foundation/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.md`
- `docs/foundation/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.json`
- `docs/audit/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A_report.md`
- `docs/audit/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A_result.json`
- `docs/audit/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A_checklist.json`
- `docs/audit_packages/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A_manifest.json`
- `docs/audit_packages/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.zip`
- `scripts/validate_xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.py`

Expected final status:

```text
XIAOJIAO_TEACHER_JARVIS_WORKBENCH_CONCEPT_CONTRACT_PASS
```

### 1000B_PRE_CLASS_WORK_SAMPLE_ROOM_BUSINESS_STRUCTURE

Goal: define the art teacher pre-class work sample room.

Expected scope:

- teacher role profile
- work scopes
- pre-class artifact map
- teaching work plan main document
- supporting artifact graph
- weekly work graph
- today work items
- classroom preparation package chain

### 1000C_DYNAMIC_WORK_PANEL_CONTRACT

Goal: define Dynamic Work Panel as a renderer contract, not a fixed card component.

Expected scope:

- panel schema
- panel modes
- visible and hidden field rules
- available actions
- linked objects
- display rules
- layout rules
- teacher-facing state rules

### 1000D_AGENT_ACTION_POLICY_AND_WORK_STATE_CONTRACT

Goal: define how the Agent decides what to show, generate, ask, repair, sync, or confirm.

Expected scope:

- work state schema
- turn detection
- action policy
- sufficiency gate
- renderer mapping gate
- confirmation gate
- token-saving state summary
- audit trace separated from teacher-facing UI

### 1000E_ART_TEACHER_PRE_CLASS_WORKBENCH_PILOT

Goal: implement the first usable sample room.

Expected scope:

- art teacher pre-class workbench home
- teaching work plan dynamic panel
- weekly work graph panel
- today work items panel
- Xiaojiao suggestion bar
- mini conversation surface
- work record drawer

## 1000A Contract Snapshot

1000A is concept-contract only. It must not implement UI or connect runtime.

Contract JSON should include at least:

- `stage_code`
- `stage_name`
- `final_status_target`
- `product_identity`
- `naming_policy`
- `legacy_namespace_policy`
- `core_concepts`
- `page_principles`
- `assistant_surface_states`
- `workbench_positioning`
- `pre_class_work_chain`
- `weekly_work_graph_definition`
- `today_work_item_definition`
- `quickclass_boundary`
- `prohibited_patterns`
- `future_milestones`
- `validation_requirements`

Validator commands:

```text
python scripts/validate_xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.py
python scripts/validate_xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.py --root .
```

Validator marker:

```text
ALL_1000A_XIAOJIAO_TEACHER_JARVIS_WORKBENCH_CONCEPT_CONTRACT_CHECKS_OK
```

Required primary English concepts:

- `Unified Xiaojiao Agent`
- `Agent-led Progressive Workspace`
- `Dynamic Work Panel`
- `Work Object`
- `Work Action`
- `Work State`

Required primary Chinese concepts:

- `统一小教智能体`
- `小教主导的渐进式工作台`
- `动态工作面板`
- `工作对象`
- `工作动作`
- `工作状态`

Required support concepts:

- `Work View Composer`
- `Assistant Surface`

Recommended wording for validation:

```text
Six primary concepts + two support concepts
```

The support concepts should be validated so later contracts do not collapse back into a simple Agent + panel + state model.

1000A result boundary flags must stay safe:

- `database_written=false`
- `memory_written=false`
- `feishu_written=false`
- `formal_export_created=false`
- `classroom_student_runtime_connected=false`
- `old_sealed_stage_modified=false`
- `full_repo_blind_rename_performed=false`

## Execution Discipline

The next line should use "planning package driven + stage self-progression + milestone audit".

Default execution model:

```text
Set one planning package
-> Codex can advance several sub-stages inside the milestone
-> each sub-stage has validator, report, result, checklist, manifest, ZIP where appropriate
-> stop only on blocker or scope boundary
-> submit milestone package for review after the milestone, not after every tiny patch
```

Hard rules for future tasks:

- Do not split Xiaojiao into many business-specific Agents.
- Do not rebuild the target as a traditional module-menu page.
- Do not let default main workspace be dominated by chat history.
- Do not make Dynamic Work Panel into fixed dead cards.
- Do not use fake action buttons such as accept/follow-up as the main teacher workflow.
- Do not remove the existing teaching-planning tab row unless a later UI stage explicitly replaces it.
- Do not connect classroom student-side runtime in this package.
- Do not write database, memory, Feishu, or formal export.
- Do not call provider/model unless a later stage explicitly opens that boundary.
- Do not show engineering terms such as dry-run, readonly, fixture, stage, validator, or boundary flags in the teacher-facing primary experience.
- Do not allow `小备` in new teacher-facing primary copy.
- Do not perform blind full-repository rename.
- Mark continued internal `xiaobei` references as `legacy_internal_namespace=true` in new contracts when relevant.
- Keep review-package habits: relative paths, manifest alignment, no `.env`, no tokens, no secrets, no student data.

## Relationship With 0998N

Before these notes, the next recommended stage after 0998M was:

```text
0998N_SUBJECT_TEACHER_SEMESTER_WORK_PLAN_PILOT_READONLY
```

This remains technically valid as a narrow teaching-planning follow-up.

However, after the Jarvis-style workspace discussion, the stronger recommendation is:

```text
Pause narrow 0998N implementation unless explicitly requested.
Start 1000A first to lock the system-level workspace concept.
```

Reason:

```text
If 0998N starts immediately, it may deepen the current teaching-planning page shape before the new workspace model is contracted.
1000A reduces the risk of returning to fixed pages, fixed cards, and chat-led interaction.
```

## Reviewer Notes / Planning Hardening

Latest reviewer judgment:

```text
handoff note: acceptable
usable as 1000A task basis: yes
formal 1000A audit package: not yet
```

This note is therefore a planning basis. The next implementation task should convert it into a formal 1000A concept contract package, not treat this file as already completing 1000A.

Hardening notes for 1000A:

- `Jarvis` should remain an internal planning metaphor unless a later branding stage explicitly approves teacher-facing use.
- Teacher-facing product wording should prefer `小教主导的渐进式工作台`, `教师动态工作台`, or other education-native wording instead of `Jarvis`.
- `Work View Composer` and `Assistant Surface` should be included as required support concepts in 1000A validation.
- Keep the six primary concepts stable, but validate the two support concepts so the renderer composition layer and lightweight assistant surface are not dropped.
- `周工作图谱` must not simply replace `学期周历表`.
- `学期周历表` should remain the semester progress supporting table: which week teaches what.
- `周工作图谱` should be a higher-level weekly work panel: what to teach, prepare, evaluate, adjust, submit, and carry over this week.
- 1000B should define the education pre-class sample room, using primary art teacher as the first sample role without hardcoding art-teacher logic as a system-wide rule.
- The 1000B stage name can be reconsidered as `1000B_EDUCATION_PRE_CLASS_WORK_SAMPLE_ROOM_BUSINESS_STRUCTURE`.

Recommended next instruction:

```text
基于 docs/handoff/teacher_jarvis_workbench_planning_notes_1000_20260612.md
生成正式 1000A concept contract review package.
```

Required output for that next task:

- contract markdown
- contract JSON
- checklist JSON
- result JSON
- report markdown
- manifest JSON
- validator
- ZIP package

Still forbidden in that next task:

- UI implementation
- runtime connection
- provider/model call
- database write
- memory write
- Feishu write
- formal export
- old sealed-stage modification
- blind repository rename

## Default Next Task Candidate

If the next user command is "开始" or "继续推进" without more detail, the default recommended task is:

```text
1000A_XIAOJIAO_TEACHER_JARVIS_WORKBENCH_CONCEPT_CONTRACT
```

Executable handoff for the next session:

```text
docs/handoff/xiaojiao_teacher_jarvis_workbench_1000A_execution_handoff_20260612.md
```

Scope for that task:

- documentation and schema only
- no frontend implementation
- no runtime behavior change
- no provider call
- no database write
- no memory write
- no Feishu write
- no formal export
- validator and review package required

## Open Questions For Later Task Assignment

These do not block this note, but should be resolved when implementing 1000A or 1000B:

- Should the term "Jarvis" stay only as internal metaphor, or appear in product docs?
- Should the teacher-facing Chinese term be "动态工作面板", "工作面板", or another term?
- Should `教学规划` be renamed in UI to a broader teacher workbench entry, or only reinterpreted internally first?
- Should `周工作图谱` replace `学期周历表` in the final teacher-facing language, or be an additional higher-level panel?
- Should 0998N be skipped, renamed, or absorbed into 1000E after 1000A-1000D?
