from pathlib import Path

LOG_FILE = Path(__file__).parent / "incident.log"


def analyze_incident():
    lines = LOG_FILE.read_text(encoding="utf-8").splitlines()
    errors = [line for line in lines if "ERROR" in line]
    warnings = [line for line in lines if "WARNING" in line]

    return (
        f"Incident summary: {len(errors)} error(s), "
        f"{len(warnings)} warning(s).\n"
        + "\n".join(errors + warnings)
    )


def get_response(message):
    request = message.strip().lower()

    if request in ("help", "what can you do?"):
        return (
            "Supported requests:\n"
            "- status: summarize the sample incident log\n"
            "- help: show supported requests\n"
            "- exit: quit the chat"
        )

    if request in ("status", "check incident", "summarize incident"):
        return analyze_incident()

    return (
        "Request not supported. No action was taken. "
        "Type 'help' to see supported requests."
    )


def main():
    print("DevOps ChatOps Assistant")
    print("Type 'help' for options or 'exit' to quit.")

    while True:
        try:
            message = input("\nYou: ")
        except (EOFError, KeyboardInterrupt):
            print("\nChat ended.")
            break

        if message.strip().lower() == "exit":
            print("Assistant: Goodbye.")
            break

        print(f"Assistant: {get_response(message)}")


if __name__ == "__main__":
    main()
