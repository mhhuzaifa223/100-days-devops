import tempfile
from pathlib import Path

def run_demo():
    print("DevSecOps SAST training")

def create_temp_file():
    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        delete=False
    ) as file:
        file.write("training data")
        temp_path = Path(file.name)

    print(f"Temporary file created: {temp_path}")
    temp_path.unlink()

if __name__ == "__main__":
    run_demo()
    create_temp_file()
