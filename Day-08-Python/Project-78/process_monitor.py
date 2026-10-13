import psutil

print("=== PROCESS MONITOR ===")

processes = []

for process in psutil.process_iter(["pid", "name", "memory_info"]):
    try:
        info = process.info
        memory = info["memory_info"]

        processes.append({
            "pid": info["pid"],
            "name": info["name"] or "unknown",
            "memory_mb": memory.rss / (1024 * 1024) if memory else 0,
        })
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        continue

processes.sort(key=lambda item: item["memory_mb"], reverse=True)

print(f"Running processes found: {len(processes)}")
print("\nTop 5 processes by memory usage:")
print(f"{'PID':>8} {'MEMORY (MB)':>12}  PROCESS")

for process in processes[:5]:
    print(
        f"{process['pid']:>8} "
        f"{process['memory_mb']:>12.2f}  "
        f"{process['name']}"
    )
