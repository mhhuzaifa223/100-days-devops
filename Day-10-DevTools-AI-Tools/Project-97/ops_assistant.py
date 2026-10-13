import json
import shutil
from pathlib import Path

BASE_DIR = Path(__file__).parent
TASKS_FILE = BASE_DIR / "tasks.json"
INCIDENT_FILE = BASE_DIR / "incident.log"


def disk_status():
    usage = shutil.disk_usage("/")
    percent = round(usage.used / usage.total * 100, 1)

    return {
        "path": "/",
        "used_percent": percent,
        "free_gb": round(usage.free / (1024 ** 3), 2),
    }


def incident_summary():
    lines = INCIDENT_FILE.read_text(encoding="utf-8").splitlines()
    errors = [line for line in lines if "ERROR" in line]
    warnings = [line for line in lines if "WARNING" in line]

    return {
        "total_lines": len(lines),
        "errors": errors,
        "warnings": warnings,
        "suggestion": (
            "Inspect API logs, dependencies, and recent deployments."
            if errors else "No errors detected in the sample log."
        ),
    }


def show_help(tasks):
    return {
        name: details["description"]
        for name, details in tasks.items()
    }


TOOLS = {
    "disk_status": disk_status,
    "incident_summary": incident_summary,
    "help": None,
}


def run_task(task_name):
    tasks = json.loads(TASKS_FILE.read_text(encoding="utf-8"))

    if task_name not in tasks:
        return {"error": "Task not approved", "available_tasks": list(tasks)}

    tool_name = tasks[task_name]["tool"]

    if tool_name == "help":
        return show_help(tasks)

    tool = TOOLS.get(tool_name)
    if tool is None:
        return {"error": "Configured tool is unavailable"}

    return tool()


if __name__ == "__main__":
    print("=== DevOps Operations Assistant ===")
    print("\nApproved tasks:")
    print(json.dumps(run_task("show_help"), indent=2))

    print("\nDisk status:")
    print(json.dumps(run_task("check_disk"), indent=2))

    print("\nIncident summary:")
    print(json.dumps(run_task("check_incident"), indent=2))

    print("\nSafety: only predefined read-only functions are allowed.")
