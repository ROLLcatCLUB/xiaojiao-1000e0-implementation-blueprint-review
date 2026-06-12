# 1000E0_ART_TEACHER_PRE_CLASS_WORKBENCH_IMPLEMENTATION_BLUEPRINT

Date: 2026-06-12

## Stage Identity

```text
package_code=1000_XIAOJIAO_TEACHER_JARVIS_WORKBENCH_PLANNING_PACKAGE
stage_code=1000E0_ART_TEACHER_PRE_CLASS_WORKBENCH_IMPLEMENTATION_BLUEPRINT
stage_name=Art Teacher Pre-Class Workbench Implementation Blueprint
stage_type=implementation_blueprint_only
final_status_target=XIAOJIAO_ART_TEACHER_PRE_CLASS_WORKBENCH_IMPLEMENTATION_BLUEPRINT_PASS
next_stage=1000E_ART_TEACHER_PRE_CLASS_WORKBENCH_PILOT_PENDING_REVIEW
```

## Purpose

1000E0 is an implementation blueprint hardening stage before 1000E. It accepts 1000A-1000D as a contract baseline, but explicitly does not treat them as full implementation design.

This stage fills the depth caveat found in review:

- artifact field structures for the art-teacher pre-class sample room
- three core Dynamic Work Panel examples
- real input scenario decisions
- Work State -> Panel -> Action transition table
- mode changes and available action rules

## Hard Boundaries

This package does not implement UI, modify real frontend pages, connect runtime, call provider/model, write database, write memory, write Feishu, create formal export, connect classroom student runtime, modify old sealed stages, or perform blind rename.

`Jarvis` remains an internal planning metaphor only. Teacher-facing product copy remains `小教 / Xiaojiao`.

## Artifact Schemas

```json
{
  "teaching_work_plan": {
    "role": "main_document",
    "zh": "教学工作计划",
    "required_fields": [
      "plan_id",
      "teacher_role_profile_ref",
      "semester",
      "grade_band",
      "subject",
      "textbook_catalog_ref",
      "teaching_goals",
      "unit_sequence",
      "key_competencies",
      "assessment_plan",
      "resource_plan",
      "risk_notes",
      "linked_artifacts",
      "review_status"
    ],
    "cannot_be_replaced_by": [
      "unit_lesson_allocation",
      "semester_weekly_calendar",
      "weekly_work_graph",
      "today_work_items"
    ]
  },
  "unit_lesson_allocation": {
    "role": "supporting_artifact",
    "zh": "单元课时分配",
    "required_fields": [
      "unit_id",
      "unit_title",
      "lesson_count",
      "periods",
      "lesson_focus",
      "linked_calendar_weeks",
      "linked_work_plan_sections"
    ]
  },
  "semester_weekly_calendar": {
    "role": "supporting_artifact",
    "zh": "学期周历表",
    "definition": "semester progress supporting table; answers which week teaches what",
    "required_fields": [
      "week_index",
      "date_range",
      "unit_or_topic",
      "lesson_periods",
      "progress_goal",
      "school_events",
      "linked_unit_allocation"
    ]
  },
  "weekly_work_graph": {
    "role": "higher_level_weekly_work_panel",
    "zh": "周工作图谱",
    "definition": "higher-level weekly work panel; organizes what to teach, prepare, evaluate, adjust, submit, handle, and carry over this week",
    "replaces_semester_weekly_calendar": false,
    "required_fields": [
      "week_index",
      "teaching_focus",
      "preparation_tasks",
      "evaluation_tasks",
      "adjustment_tasks",
      "submission_tasks",
      "issues_to_handle",
      "carry_over_items",
      "linked_calendar_rows"
    ]
  },
  "today_work_items": {
    "role": "daily_action_artifact",
    "zh": "今日工作项",
    "required_fields": [
      "item_id",
      "date",
      "work_scope",
      "work_object_ref",
      "action_type",
      "priority",
      "due_hint",
      "blocked_by",
      "teacher_visible_reason",
      "next_action"
    ]
  },
  "lesson_design": {
    "role": "supporting_artifact",
    "zh": "课时设计",
    "required_fields": [
      "lesson_id",
      "lesson_title",
      "learning_objectives",
      "activity_flow",
      "materials_needed",
      "assessment_points",
      "linked_work_plan",
      "linked_weekly_work_graph"
    ]
  },
  "learning_task_sheet": {
    "role": "supporting_artifact",
    "zh": "学习单",
    "required_fields": [
      "task_sheet_id",
      "lesson_ref",
      "student_task",
      "process_prompt",
      "submission_format",
      "evaluation_hint"
    ]
  },
  "evaluation_rubric": {
    "role": "supporting_artifact",
    "zh": "评价量规",
    "required_fields": [
      "rubric_id",
      "artifact_ref",
      "criteria",
      "levels",
      "teacher_feedback_guidance",
      "student_self_review_hint"
    ]
  },
  "classroom_preparation_package": {
    "role": "package_chain_output",
    "zh": "课堂准备包",
    "required_fields": [
      "package_id",
      "lesson_design_ref",
      "learning_task_sheet_ref",
      "evaluation_rubric_ref",
      "resource_list",
      "classroom_setup_notes",
      "teacher_checklist",
      "not_formal_export"
    ]
  }
}
```

## Core Panel Examples

### 教学工作计划动态面板

- `panel_id`: `panel_teaching_work_plan`
- `artifact_type`: `teaching_work_plan`
- `purpose`: Help the teacher create, inspect, revise, and connect the semester teaching work plan as the main document.
- `empty` visible_fields: `what_this_panel_can_do, required_profile_slots, start_action`
  available_actions: `ASK`
- `intake` visible_fields: `known_slots, missing_slots, recommended_next_question, linked_profile`
  available_actions: `ASK, INSPECT_GAP`
- `draft` visible_fields: `draft_outline, section_status, linked_artifacts, missing_info`
  available_actions: `REVISE, DERIVE_SUPPORTING_ARTIFACT, INSPECT_GAP`
- `working` visible_fields: `current_section, pending_revisions, derived_artifact_readiness, risks`
  available_actions: `REVISE, LINK_ARTIFACT, DERIVE_SUPPORTING_ARTIFACT`
- `review` visible_fields: `full_plan_summary, gap_check, consistency_check, review_actions`
  available_actions: `REVISE, PREPARE_EXPORT_REVIEW_ONLY, CONFIRM`
### 周工作图谱动态面板

- `panel_id`: `panel_weekly_work_graph`
- `artifact_type`: `weekly_work_graph`
- `purpose`: Turn semester progress and current work state into a weekly work panel without replacing semester weekly calendar.
- `empty` visible_fields: `week_selector, calendar_dependency, graph_definition`
  available_actions: `ASK, INSPECT_GAP`
- `intake` visible_fields: `selected_week, linked_calendar_row, missing_week_context, recommended_action`
  available_actions: `ASK, LINK_ARTIFACT`
- `draft` visible_fields: `teaching_focus, preparation_tasks, evaluation_tasks, submission_tasks, carry_over_items`
  available_actions: `REVISE, DERIVE_SUPPORTING_ARTIFACT, INSPECT_GAP`
- `working` visible_fields: `task_clusters, priority_order, blocked_items, linked_today_items`
  available_actions: `REVISE, LINK_ARTIFACT, DERIVE_SUPPORTING_ARTIFACT`
- `review` visible_fields: `weekly_summary, calendar_alignment, main_plan_alignment, review_actions`
  available_actions: `REVISE, CONFIRM`
### 今日工作项面板

- `panel_id`: `panel_today_work_items`
- `artifact_type`: `today_work_items`
- `purpose`: Prioritize today's actionable teacher work from Work State and linked weekly graph.
- `empty` visible_fields: `date, available_sources, start_action`
  available_actions: `ASK`
- `intake` visible_fields: `known_sources, missing_sources, candidate_tasks`
  available_actions: `ASK, INSPECT_GAP`
- `draft` visible_fields: `ordered_items, priority_reason, blocked_by, next_action`
  available_actions: `REVISE, LINK_ARTIFACT`
- `working` visible_fields: `active_item, done_items, deferred_items, issue_items`
  available_actions: `REVISE, CONFIRM, DEFER, BLOCK`
- `review` visible_fields: `completed_summary, remaining_items, carry_over_suggestion`
  available_actions: `CONFIRM, RECORD_TRACE`

## Real Input Scenarios

### scenario_generate_teaching_work_plan

- teacher_input: `帮我做教学工作计划`
- expected_decision: `ASK_OR_GENERATE_DRAFT_BY_SUFFICIENCY`
- sufficiency_rule: If grade, subject, semester, textbook catalog, class count, and weekly periods are known, choose GENERATE_DRAFT; otherwise choose ASK.
### scenario_derive_weekly_work_graph

- teacher_input: `把这个计划拆成本周要做什么`
- expected_decision: `DERIVE_SUPPORTING_ARTIFACT`
- sufficiency_rule: Teaching work plan and semester weekly calendar must both be linked; if weekly calendar is missing, choose ASK or INSPECT_GAP.
### scenario_generate_today_work_items

- teacher_input: `今天我要做什么`
- expected_decision: `DERIVE_SUPPORTING_ARTIFACT_OR_ASK`
- sufficiency_rule: Weekly work graph or current active teaching work plan context is required; if absent, ask for scope.
### scenario_prepare_export_review_only

- teacher_input: `导出正式表`
- expected_decision: `PREPARE_EXPORT_REVIEW_ONLY_PLUS_CONFIRM`
- sufficiency_rule: 1000E0 can only define the confirmation path; it cannot create formal export.

## Work State To Panel To Action Transition Table

| From State | Teacher Input | Decision | Work State Change | Panel Patch |
| --- | --- | --- | --- | --- |
| `empty_context` | `帮我做教学工作计划` | `ASK when required slots are missing; GENERATE_DRAFT when sufficient` | `set active_work_object=teaching_work_plan; collect or use profile slots` | `panel_teaching_work_plan -> intake or draft` |
| `teaching_work_plan_draft_ready` | `拆成周历表` | `DERIVE_SUPPORTING_ARTIFACT for semester_weekly_calendar; never replace teaching_work_plan` | `link semester_weekly_calendar as supporting artifact` | `panel_teaching_work_plan remains primary; weekly calendar appears as linked support` |
| `weekly_calendar_linked` | `拆成本周工作图谱` | `DERIVE_SUPPORTING_ARTIFACT for weekly_work_graph` | `set active_work_object=weekly_work_graph; keep semester_weekly_calendar linked` | `panel_weekly_work_graph -> draft; calendar stays linked context` |
| `weekly_work_graph_draft_ready` | `今天我要做什么` | `DERIVE_SUPPORTING_ARTIFACT for today_work_items` | `set active_work_object=today_work_items; order tasks by priority, due hint, and blockers` | `panel_today_work_items -> draft` |
| `review_ready` | `导出正式表` | `PREPARE_EXPORT_REVIEW_ONLY then BLOCK formal export in 1000E0` | `set confirmation_required=true; record formal_export_created=false` | `panel_teaching_work_plan -> review with export readiness warning` |

## Mode Change Rules

```json
{
  "empty_to_intake": "Teacher expresses intent but required slots or linked artifacts are missing.",
  "intake_to_draft": "Sufficiency gate passes and draft or derived artifact can be prepared.",
  "draft_to_working": "Teacher starts revising, linking, deriving, or resolving gaps.",
  "working_to_review": "Required fields are filled and alignment checks can be shown.",
  "review_to_ready_to_confirm": "Teacher has reviewed a safe non-runtime action; irreversible write/export remains blocked in 1000E0.",
  "any_to_blocked": "Boundary gate or missing prerequisite prevents the requested action."
}
```

## Available Action Rules

- `ask_before_generate_when_slots_missing`: when required profile or artifact slots are missing; allow `ASK, INSPECT_GAP`; block `GENERATE_DRAFT, DERIVE_SUPPORTING_ARTIFACT`.
- `generate_draft_when_main_document_sufficient`: when teaching_work_plan required slots are sufficient; allow `GENERATE_DRAFT, REVISE, INSPECT_GAP`; block `FORMAL_EXPORT, WRITE_DATABASE`.
- `derive_weekly_graph_only_from_plan_and_calendar`: when teaching_work_plan and semester_weekly_calendar are linked; allow `DERIVE_SUPPORTING_ARTIFACT, LINK_ARTIFACT, REVISE`; block `REPLACE_SEMESTER_WEEKLY_CALENDAR`.
- `today_items_prioritize_actionability`: when weekly_work_graph or active week context is available; allow `DERIVE_SUPPORTING_ARTIFACT, CONFIRM, DEFER, BLOCK`; block `WRITE_MEMORY, WRITE_FEISHU`.
- `export_requires_review_and_is_blocked_in_1000e0`: when teacher asks for formal export; allow `PREPARE_EXPORT_REVIEW_ONLY, CONFIRM, BLOCK`; block `FORMAL_EXPORT_CREATED`.

## Weekly Work Graph Boundary

`周工作图谱 / weekly_work_graph` does not replace `学期周历表 / semester_weekly_calendar`.

- `学期周历表`: progress supporting table; answers which week teaches what.
- `周工作图谱`: higher-level weekly work panel; organizes what to teach, prepare, evaluate, adjust, submit, handle, and carry over this week.

## Readiness Output

```text
ready_for_1000E=false
requires_review_before_1000E=true
next_stage=1000E_ART_TEACHER_PRE_CLASS_WORKBENCH_PILOT_PENDING_REVIEW
```
