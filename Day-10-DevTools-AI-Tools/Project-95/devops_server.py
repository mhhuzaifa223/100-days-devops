import json
import shutil
import time
from datetime import datetime, timezone


def get_disk_usage(path="/"):
    usage = shutil.disk_usage(path)
    return {
        "path": path,
        "total_gb": round(usage.total / (1024 ** 3), 2),
        "used_gb": round(usage.used / (1024 ** 3), 2),
        "free_gb": round(usage.free / (1024 ** 3), 2),
        "used_percent": round(usage.used / usage.total * 100, 1),
    }


def get_system_status():
    return {
        "status": "ok",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "uptime_seconds": int(time.time() - START_TIME),
        "disk": get_disk_usage("/"),
    }


START_TIME = time.time()

TOOLS = {
    "get_system_status": get_system_status,
    "get_disk_usage": get_disk_usage,
}

if __name__ == "__main__":
    print("DevOps Diagnostics Prototype")
    print(json.dumps({
        "available_tools": list(TOOLS.keys()),
        "system_status": get_system_status(),
    }, indent=2))
