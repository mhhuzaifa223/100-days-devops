from pathlib import Path

log_file = Path("kubernetes.log")
text = log_file.read_text(encoding="utf-8")
log_lower = text.lower()

issues = []

if "crashloopbackoff" in log_lower:
    issues.append({
        "status": "CrashLoopBackOff",
        "cause": "The container is repeatedly starting and crashing.",
        "commands": [
            "kubectl describe pod <pod-name>",
            "kubectl logs <pod-name> --previous",
            "kubectl get events --sort-by=.lastTimestamp",
        ],
    })

if "imagepullbackoff" in log_lower or "failed to pull image" in log_lower:
    issues.append({
        "status": "ImagePullBackOff",
        "cause": "Kubernetes cannot successfully pull the container image.",
        "commands": [
            "kubectl describe pod <pod-name>",
            "kubectl get pod <pod-name> -o yaml",
            "Check the image name, tag, registry access, and imagePullSecrets.",
        ],
    })

print("=== Kubernetes Troubleshooting Assistant ===")

if not issues:
    print("No recognized Kubernetes failures found.")
else:
    print(f"Recognized issues: {len(issues)}")

    for issue in issues:
        print(f"\n[{issue['status']}]")
        print(f"Likely explanation: {issue['cause']}")
        print("Recommended next steps:")

        for command in issue["commands"]:
            print(f"- {command}")

print("\nNote: Recommendations are based on log-pattern matching.")
print("Verify the actual cause using live cluster evidence.")
