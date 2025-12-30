from pathlib import Path


def find_files(source_dir, recursive=True, ext=None, starts_with=None, ends_with=None):
    """
    Generator that yields Path objects based on filters.
    """
    source_path = Path(source_dir)

    if not source_path.exists():
        raise FileNotFoundError(f"Source directory '{source_dir}' not found.")

    # 1. Selection Strategy
    if recursive:
        iterator = source_path.rglob("*")  # Recursive
    else:
        iterator = source_path.glob("*")  # Flat

    # 2. Filtering
    for file_path in iterator:
        if not file_path.is_file():
            continue

        # Filter: Extension
        if ext and file_path.suffix.lower() != ext.lower():
            continue

        # Filter: Starts With
        if starts_with and not file_path.name.startswith(starts_with):
            continue

        # Filter: Ends With (checking stem or full name depending on user intent)
        # Usually users mean the filename before extension, but strict "ends with"
        # implies the whole string. Let's check name.
        if ends_with and not file_path.name.endswith(ends_with):
            continue

        yield file_path