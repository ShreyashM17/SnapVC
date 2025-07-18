# Version-Control

A Python-based lightweight version control system inspired by Git, aimed primarily as an educational project to demonstrate core version control concepts such as staging, snapshotting, and reverting, with simplified functionality tailored for learning and experimentation. This project provides core version control features such as staging, snapshotting, and reverting.

## Features

* Initialize a new repository.
* Create snapshots of current files.
* Stage files before snapshotting.
* Revert to previous snapshots.
* Ignore files using rules similar to `.gitignore` via `ignore.py`.

## Project Structure

```
Version-control/
├── ignore.py         # Handles file ignore logic similar to .gitignore
├── main.py           # CLI entry point and command parser
├── snapshot.py       # Logic for creating file snapshots
├── staging.py        # Manages the staging area
├── revert.py         # Logic for reverting to previous snapshots
└── README.md         # Project overview
```

## Installation

1. Clone this repository:

```bash
git clone https://github.com/ShreyashM17/Version-control.git
cd Version-control
```

2. Run using Python 3:

```bash
python main.py <command> [options]
```

## Usage

### Initialize Repository

```bash
python main.py init
```

### Stage Files

Use the `ready` command to stage files (the term `ready` is used instead of `stage` to emphasize that files are prepared and marked as ready for snapshotting):

```bash
python main.py ready
```

### Create Snapshot

```bash
python main.py snapshot
```

### Revert to Snapshot

```bash
python main.py revert <snapshot_id>
```

## Ignore Rules

* The `ignore.py` script implements ignore logic similar to `.gitignore`.
* It uses two predefined lists:

```python
# ignore.py

# Directories to ignore
dir_ignore = [".venv", ".git", ".idea", "__pycache__"]

# Files to ignore
files_ignore = [".DS_Store"]
```

* Patterns specified in these lists are respected during staging and snapshotting.