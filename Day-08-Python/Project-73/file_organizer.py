from pathlib import Path
import shutil

SOURCE = Path("test_files")

FOLDERS = {
    ".pdf": "Documents",
    ".txt": "Documents",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".py": "Code",
    ".zip": "Archives",
}

if not SOURCE.is_dir():
    print(f"Error: Folder not found: {SOURCE}")
    raise SystemExit(1)

moved = 0

for file in SOURCE.iterdir():
    if not file.is_file():
        continue

    folder_name = FOLDERS.get(file.suffix.lower(), "Others")
    destination_folder = SOURCE / folder_name
    destination_folder.mkdir(exist_ok=True)

    destination = destination_folder / file.name

    if destination.exists():
        print(f"Skipped duplicate: {file.name}")
        continue

    shutil.move(str(file), str(destination))
    print(f"Moved: {file.name} -> {folder_name}/")
    moved += 1

print(f"\nOrganization complete. Files moved: {moved}")
