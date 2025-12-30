# Recursive File Manager (RFM)

**A lightweight, zero-dependency CLI utility to filter, organize, and manage files in bulk.**

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## 🚀 Overview

**RFM** is a general-purpose tool designed to tame messy directory structures. It allows you to recursively find specific files and perform batch operations (copy, move, delete) without writing complex shell scripts.

It is ideal for tasks like:
- Consolidating scattered backups
- Cleaning up deeply nested Downloads folders
- Managing server logs
- Filtering files by name, extension, or prefix

## ✨ Features

- **Deep Search:** Automatically traverses all subdirectories (recursive by default).
- **Granular Filters:** Target files by **extension** (e.g., `.log`), **prefix** (`IMG_`), or **suffix** (`_backup`).
- **Safe Operations:** Interactive conflict resolution (Skip, Overwrite, or Rename) prevents accidental data loss during moves/copies.
- **Metadata Inspector:** View file details (size, dates) without opening them.

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/maithiljanardan/recursive_file_manager.git
cd recursive-file-manager
```

2. Run directly (no pip install required; standard library only):
```bash
python main.py --help
```

## ⚡ Command Reference

The basic syntax is:
`python main.py [SOURCE_DIR] [ACTION] [OPTIONS]`

| Argument | Description |
| --- | --- |
| `source` | The folder to scan. |
| `action` | `list`, `view`, `copy`, `move`, `delete`. |
| `--dest` | Destination folder (required for copy/move). |
| `--ext` | Filter by extension (e.g., `.jpg`, `.pdf`). |
| `--starts-with` | Filter by filename start. |
| `--ends-with` | Filter by filename end. |
| `--no-recursive` | Restrict search to the top-level folder only. |

---

## 📖 Real-World Examples

### Scenario 1: Organizing Photos (Consolidating Backups)

If you have a backup folder with photos scattered inside many sub-folders (e.g., `Year/Month/Day/photo.jpg`), you can pull them all into one flat directory.

Command:
```bash
python main.py ./OldBackup copy --dest ./All_Photos --ext .jpg
```

Conflict handling behavior:
If `photo.jpg` already exists in the destination, the tool will prompt:
```
[!] Conflict: 'photo.jpg' exists. (S)kip, (O)verwrite, (R)ename?
```
- Select **(R)ename** to automatically save it as `photo_1.jpg`.
- Select **(S)kip** to ignore the file.
- Select **(O)verwrite** to replace the existing file.

### Scenario 2: Cleaning up Downloads

Move all PDF documents from your Downloads folder (and its subfolders) to a distinct Documents folder:

```bash
python main.py ~/Downloads move --dest ~/Documents --ext .pdf
```

### Scenario 3: Server Maintenance (Logs)

Find and list all error logs recursively to inspect them without moving them:

```bash
python main.py /var/logs view --starts-with error --ext .log
```

### Scenario 4: Project Cleanup

Delete all temporary `.tmp` files from a project directory:

```bash
python main.py ./MyProject delete --ext .tmp
```

(Note: You must type YES to confirm any delete operation.)

---

## 🛠️ Project Structure

```text
recursive-file-manager/
├── main.py             # Entry point
└── rfm/                # Source package
    ├── cli.py          # Argument parsing
    ├── finder.py       # File search logic
    ├── actions.py      # Copy/Move/Delete operations
    └── utils.py        # Helper functions (formatting, conflict handling)
```

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a Pull Request.
