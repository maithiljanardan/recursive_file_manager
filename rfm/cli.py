import argparse
import sys
from .finder import find_files
from .actions import ActionHandler


def parse_arguments():
    parser = argparse.ArgumentParser(description="Google Takeout Manager CLI")

    # Core Arguments
    parser.add_argument("source", help="Source directory path")
    parser.add_argument("action", choices=["list", "view", "copy", "move", "delete"], help="Action to perform")

    # Filters
    parser.add_argument("--ext", help="Filter by file extension (e.g., .jpg, .json)")
    parser.add_argument("--starts-with", help="Filter files starting with this name")
    parser.add_argument("--ends-with", help="Filter files ending with this name")
    parser.add_argument("--no-recursive", action="store_true", help="Disable recursive search (default is recursive)")

    # Action Specifics
    parser.add_argument("--dest", help="Destination directory (Required for copy/move)")

    return parser.parse_args()


def main():
    args = parse_arguments()

    # Validation
    if args.action in ['copy', 'move'] and not args.dest:
        print("Error: --dest [DIRECTORY] is required for copy and move operations.")
        sys.exit(1)

    if args.action == 'delete':
        confirm = input(f"WARNING: You are about to DELETE files in '{args.source}'.\nType 'YES' to confirm: ")
        if confirm != 'YES':
            print("Aborted.")
            sys.exit(0)

    # Initialize Logic
    handler = ActionHandler(dest_dir=args.dest)
    recursive_search = not args.no_recursive

    print(f"Scanning '{args.source}'...")

    count = 0
    # execute search
    try:
        files = find_files(
            args.source,
            recursive=recursive_search,
            ext=args.ext,
            starts_with=args.starts_with,
            ends_with=args.ends_with
        )

        for file_path in files:
            count += 1
            if args.action == "list":
                handler.list_files(file_path)
            elif args.action == "view":
                handler.view_metadata(file_path)
            elif args.action == "copy":
                handler.copy_file(file_path)
            elif args.action == "move":
                handler.move_file(file_path)
            elif args.action == "delete":
                handler.delete_file(file_path)

        print(f"\nOperation completed. Processed {count} files.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()