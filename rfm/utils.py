import os
import datetime


def format_metadata(path_obj):
    """Returns a formatted string of file metadata."""
    stats = path_obj.stat()
    size_mb = stats.st_size / (1024 * 1024)
    created = datetime.datetime.fromtimestamp(stats.st_ctime).strftime('%Y-%m-%d %H:%M:%S')
    modified = datetime.datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')

    return (
        f"File: {path_obj.name}\n"
        f"Path: {path_obj}\n"
        f"Size: {size_mb:.2f} MB\n"
        f"Created: {created} | Modified: {modified}\n"
        f"{'-' * 40}"
    )


def resolve_conflict(destination_path):
    """
    Handles file conflicts.
    Returns:
        Path: New destination path (for overwrite or rename)
        None: If the user chooses to skip.
    """
    if not destination_path.exists():
        return destination_path

    print(f"\n[!] Conflict: '{destination_path.name}' already exists at destination.")
    while True:
        choice = input("    (S)kip, (O)verwrite, (R)ename? [s/o/r]: ").lower().strip()

        if choice == 's':
            print("    -> Skipped.")
            return None

        elif choice == 'o':
            print("    -> Overwriting.")
            return destination_path

        elif choice == 'r':
            # Generate a new name: file.jpg -> file_1.jpg
            directory = destination_path.parent
            stem = destination_path.stem
            suffix = destination_path.suffix
            counter = 1
            new_path = directory / f"{stem}_{counter}{suffix}"

            while new_path.exists():
                counter += 1
                new_path = directory / f"{stem}_{counter}{suffix}"

            print(f"    -> Renaming to: {new_path.name}")
            return new_path