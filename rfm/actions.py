import shutil
import os
from pathlib import Path
from .utils import format_metadata, resolve_conflict


class ActionHandler:
    def __init__(self, dest_dir=None):
        self.dest_dir = Path(dest_dir) if dest_dir else None

        # Ensure destination exists for Copy/Move
        if self.dest_dir and not self.dest_dir.exists():
            print(f"Creating destination directory: {self.dest_dir}")
            self.dest_dir.mkdir(parents=True, exist_ok=True)

    def list_files(self, file_path):
        print(f"[FOUND] {file_path}")

    def view_metadata(self, file_path):
        print(format_metadata(file_path))

    def copy_file(self, file_path):
        if not self.dest_dir:
            raise ValueError("Destination directory is required for COPY.")

        target_path = self.dest_dir / file_path.name
        final_path = resolve_conflict(target_path)

        if final_path:
            try:
                shutil.copy2(file_path, final_path)
                print(f"[COPIED] {file_path.name} -> {final_path}")
            except Exception as e:
                print(f"[ERROR] Could not copy {file_path.name}: {e}")

    def move_file(self, file_path):
        if not self.dest_dir:
            raise ValueError("Destination directory is required for MOVE.")

        target_path = self.dest_dir / file_path.name
        final_path = resolve_conflict(target_path)

        if final_path:
            try:
                shutil.move(str(file_path), str(final_path))
                print(f"[MOVED] {file_path.name} -> {final_path}")
            except Exception as e:
                print(f"[ERROR] Could not move {file_path.name}: {e}")

    def delete_file(self, file_path):
        # We assume the user confirmed the batch in the CLI layer
        try:
            os.remove(file_path)
            print(f"[DELETED] {file_path}")
        except Exception as e:
            print(f"[ERROR] Could not delete {file_path.name}: {e}")