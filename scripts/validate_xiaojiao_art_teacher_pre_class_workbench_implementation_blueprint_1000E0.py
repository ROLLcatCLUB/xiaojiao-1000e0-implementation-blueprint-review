from __future__ import annotations

import argparse
import json
import sys
import zipfile
from pathlib import Path


STAGE_CODE = '1000E0_ART_TEACHER_PRE_CLASS_WORKBENCH_IMPLEMENTATION_BLUEPRINT'
FINAL_STATUS = 'XIAOJIAO_ART_TEACHER_PRE_CLASS_WORKBENCH_IMPLEMENTATION_BLUEPRINT_PASS'
SLUG = 'xiaojiao_art_teacher_pre_class_workbench_implementation_blueprint_1000E0'
MARKER = 'ALL_1000E0_ART_TEACHER_PRE_CLASS_WORKBENCH_IMPLEMENTATION_BLUEPRINT_CHECKS_OK'
NEXT_STAGE = '1000E_ART_TEACHER_PRE_CLASS_WORKBENCH_PILOT_PENDING_REVIEW'
REQUIRED_FILES = ['docs/handoff/xiaojiao_teacher_jarvis_workbench_1000A_execution_handoff_20260612.md', 'docs/handoff/teacher_jarvis_workbench_planning_notes_1000_20260612.md', 'docs/foundation/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.json', 'docs/foundation/xiaojiao_education_pre_class_work_sample_room_business_structure_1000B.json', 'docs/foundation/xiaojiao_dynamic_work_panel_contract_1000C.json', 'docs/foundation/xiaojiao_agent_action_policy_and_work_state_contract_1000D.json', 'docs/foundation/xiaojiao_art_teacher_pre_class_workbench_implementation_blueprint_1000E0.md', 'docs/foundation/xiaojiao_art_teacher_pre_class_workbench_implementation_blueprint_1000E0.json', 'docs/audit/xiaojiao_art_teacher_pre_class_workbench_implementation_blueprint_1000E0_report.md', 'docs/audit/xiaojiao_art_teacher_pre_class_workbench_implementation_blueprint_1000E0_result.json', 'docs/audit/xiaojiao_art_teacher_pre_class_workbench_implementation_blueprint_1000E0_checklist.json', 'docs/audit_packages/xiaojiao_art_teacher_pre_class_workbench_implementation_blueprint_1000E0_manifest.json', 'scripts/validate_xiaojiao_art_teacher_pre_class_workbench_implementation_blueprint_1000E0.py']
BOUNDARY_FALSE_KEYS = ['database_written', 'memory_written', 'feishu_written', 'formal_export_created', 'classroom_student_runtime_connected', 'provider_called', 'frontend_runtime_modified', 'backend_runtime_modified', 'old_sealed_stage_modified', 'full_repo_blind_rename_performed', 'teacher_facing_jarvis_wording_introduced', 'teacher_facing_xiaobei_wording_introduced', 'entered_1000E_runtime_pilot']
FORBIDDEN_PARTS = [".env", "token", "secret", "node_modules", "__pycache__", ".db", ".sqlite", "student_data", "provider_raw"]


def fail(message: str) -> None:
    raise SystemExit(f"VALIDATION_FAILED: {message}")


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"cannot read JSON {path}: {exc}")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=None)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve() if args.root else Path(__file__).resolve().parents[1]
    for rel in REQUIRED_FILES:
        if not (root / rel).exists():
            fail(f"missing required file: {rel}")

    contract = load_json(root / f"docs/foundation/{SLUG}.json")
    checklist = load_json(root / f"docs/audit/{SLUG}_checklist.json")
    result = load_json(root / f"docs/audit/{SLUG}_result.json")
    manifest = load_json(root / f"docs/audit_packages/{SLUG}_manifest.json")
    contract_text = (root / f"docs/foundation/{SLUG}.md").read_text(encoding="utf-8")
    report_text = (root / f"docs/audit/{SLUG}_report.md").read_text(encoding="utf-8")

    if contract.get("stage_code") != STAGE_CODE:
        fail("contract stage_code mismatch")
    if contract.get("stage_type") != "implementation_blueprint_only":
        fail("stage_type mismatch")
    if contract.get("final_status_target") != FINAL_STATUS:
        fail("final_status_target mismatch")
    if result.get("stage_code") != STAGE_CODE or result.get("final_status") != FINAL_STATUS or result.get("pass") is not True:
        fail("result mismatch")
    if result.get("marker") != MARKER:
        fail("marker mismatch")
    if checklist.get("stage_code") != STAGE_CODE:
        fail("checklist mismatch")
    if manifest.get("stage_code") != STAGE_CODE:
        fail("manifest mismatch")
    if contract.get("implementation_readiness_output", {}).get("next_stage") != NEXT_STAGE:
        fail("next_stage mismatch")
    if contract.get("implementation_readiness_output", {}).get("ready_for_1000E") is not False:
        fail("ready_for_1000E must remain false")

    for key, value in contract.get("hard_boundaries", {}).items():
        if value is not False:
            fail(f"hard boundary not false: {key}")
    for key in BOUNDARY_FALSE_KEYS:
        if result.get("boundary_flags", {}).get(key) is not False:
            fail(f"unsafe boundary flag: {key}")

    schemas = contract.get("artifact_schemas", {})
    for artifact in [
        "teaching_work_plan",
        "unit_lesson_allocation",
        "semester_weekly_calendar",
        "weekly_work_graph",
        "today_work_items",
        "lesson_design",
        "learning_task_sheet",
        "evaluation_rubric",
        "classroom_preparation_package",
    ]:
        if artifact not in schemas:
            fail(f"missing artifact schema: {artifact}")
        if len(schemas[artifact].get("required_fields", [])) < 5:
            fail(f"artifact schema too thin: {artifact}")
    if schemas["teaching_work_plan"].get("role") != "main_document":
        fail("teaching_work_plan must be main_document")
    if schemas["weekly_work_graph"].get("replaces_semester_weekly_calendar") is not False:
        fail("weekly_work_graph replacement boundary missing")

    panels = contract.get("panel_examples", [])
    if len(panels) < 3:
        fail("need at least three panel examples")
    required_panels = {
        "panel_teaching_work_plan",
        "panel_weekly_work_graph",
        "panel_today_work_items",
    }
    panel_ids = {panel.get("panel_id") for panel in panels}
    if not required_panels.issubset(panel_ids):
        fail("missing required panel examples")
    for panel in panels:
        modes = panel.get("mode_examples", {})
        for mode in ["empty", "intake", "draft", "working", "review"]:
            if mode not in modes:
                fail(f"missing mode {mode} in {panel.get('panel_id')}")
            if not modes[mode].get("available_actions"):
                fail(f"missing available actions in {panel.get('panel_id')} {mode}")

    scenarios = contract.get("input_scenarios", [])
    required_scenarios = {
        "scenario_generate_teaching_work_plan",
        "scenario_derive_weekly_work_graph",
        "scenario_generate_today_work_items",
    }
    if not required_scenarios.issubset({item.get("scenario_id") for item in scenarios}):
        fail("missing required input scenarios")

    transitions = contract.get("state_transition_table", [])
    if len(transitions) < 5:
        fail("state transition table too thin")
    for row in transitions:
        for key in ["from_state", "teacher_input_pattern", "decision", "work_state_change", "panel_patch", "safe_next_actions"]:
            if key not in row:
                fail(f"transition missing {key}")

    if len(contract.get("available_action_rules", [])) < 5:
        fail("available action rules too thin")
    for key in ["empty_to_intake", "intake_to_draft", "draft_to_working", "working_to_review", "review_to_ready_to_confirm", "any_to_blocked"]:
        if key not in contract.get("mode_change_rules", {}):
            fail(f"missing mode change rule {key}")

    combined = contract_text + "\n" + report_text + "\n" + json.dumps(contract, ensure_ascii=False)
    for term in [
        "implementation blueprint",
        "小教智能体",
        "Xiaojiao Agent",
        "Jarvis",
        "internal planning metaphor",
        "教学工作计划",
        "周工作图谱",
        "学期周历表",
        "does not replace",
        "Work State -> Panel -> Action",
    ]:
        if term not in combined:
            fail(f"missing term: {term}")

    zip_path = root / f"docs/audit_packages/{SLUG}.zip"
    with zipfile.ZipFile(zip_path, "r") as zf:
        zip_entries = zf.namelist()
    for entry in zip_entries:
        normalized = entry.replace("\\", "/")
        if normalized.startswith("/") or ":" in normalized:
            fail(f"unsafe ZIP path: {entry}")
        if any(part in normalized.lower() for part in FORBIDDEN_PARTS):
            fail(f"forbidden ZIP entry: {entry}")
    if manifest.get("manifest_minus_zip") != [] or manifest.get("zip_minus_manifest") != []:
        fail("manifest alignment fields are not empty")
    if sorted(manifest.get("zip_entries", [])) != sorted(zip_entries):
        fail("manifest entries do not match ZIP")
    if manifest.get("zip_entry_count") != len(zip_entries):
        fail("zip_entry_count mismatch")

    print(MARKER)
    return 0


if __name__ == "__main__":
    sys.exit(main())
