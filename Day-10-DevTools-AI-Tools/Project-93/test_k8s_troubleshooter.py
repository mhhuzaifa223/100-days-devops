import subprocess
import sys

result = subprocess.run(
    [sys.executable, "k8s_troubleshooter.py"],
    capture_output=True,
    text=True,
    check=True,
)

output = result.stdout

checks = [
    "Recognized issues: 2",
    "[CrashLoopBackOff]",
    "[ImagePullBackOff]",
    "kubectl describe pod <pod-name>",
    "kubectl logs <pod-name> --previous",
    "Check the image name, tag, registry access, and imagePullSecrets.",
]

for expected in checks:
    assert expected in output, f"Missing expected result: {expected}"

print(f"All {len(checks)} checks passed.")
