from pathlib import Path
from datetime import datetime
import zipfile

SOURCE = Path("source_data")
BACKUP_DIR = Path("backups")

if not SOURCE.is_dir():
    print(f"ERROR: Source directory not found: {SOURCE}")
    raise SystemExit(1)

files = [path for path in SOURCE.rglob("*") if path.is_file()]

if not files:
    print("ERROR: No files found to back up.")
    raise SystemExit(1)

BACKUP_DIR.mkdir(parents=True, exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
archive = BACKUP_DIR / f"backup_{timestamp}.zip"

try:
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for path in files:
            zip_file.write(path, arcname=path.relative_to(SOURCE))

    with zipfile.ZipFile(archive, "r") as zip_file:
        if zip_file.testzip() is not None:
            raise zipfile.BadZipFile("Archive verification failed")

    print(f"Backup successful: {archive}")
    print(f"Files backed up: {len(files)}")
    print(f"Archive size: {archive.stat().st_size} bytes")

except (OSError, zipfile.BadZipFile) as error:
    print(f"ERROR: Backup failed: {error}")
    raise SystemExit(1)
