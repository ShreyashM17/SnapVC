# Version Control System (SVCS)

A Python-based lightweight version control system inspired by Git, designed as an educational project to demonstrate core version control concepts. This system features a unique "house" system (similar to branches), staging areas, snapshot creation with SHA-256 hashing, and file reversion capabilities.

## ✨ Features

- **Repository Initialization**: Set up a new SVCS repository
- **House System**: Create and switch between different "houses" (similar to Git branches)
- **File Staging**: Stage files in a "ready" area before snapshotting
- **Snapshot Creation**: Create versioned snapshots using SHA-256 hashing and binary serialization
- **File Reversion**: Revert to any previous snapshot
- **Ignore Patterns**: Exclude files and directories using configurable ignore rules
- **Incremental Versioning**: Automatic version numbering for snapshots
- **Version Tracking**: View current version and total snapshot count

## 📁 Project Structure

```
Version-control/
├── main.py           # CLI entry point and command parser
├── housing.py        # House (branch-like) management system
├── snapshot.py       # Snapshot creation and versioning logic
├── staging.py        # File staging and ready area management
├── revert.py         # Snapshot reversion functionality
├── ignore.py         # File/directory ignore patterns
└── README.md         # This file
```

## 🚀 Installation

1. Clone or download this repository:
   ```bash
   git clone <repository-url>
   cd Version-control
   ```

2. Ensure you have Python 3.6+ installed

3. Run commands using:
   ```bash
   python main.py <command> [options]
   ```

## 📖 Usage Guide

### Initialize a Repository

Initialize SVCS in the current directory:
```bash
python main.py init
```
This creates an `svcs` directory with the default "main" house.

### House Management

Houses are similar to Git branches, allowing you to work on different versions simultaneously.

**View current house:**
```bash
python main.py house
```

**View all available houses:**
```bash
python main.py house show
```

**Create a new house:**
```bash
python main.py house new <house_name>
```

**Switch to an existing house:**
```bash
python main.py house <house_name>
```

### File Staging

Stage files for snapshotting (prepares files in the "ready" area):
```bash
python main.py ready
```
This command stages all files from the parent directory, respecting ignore patterns.

### Create Snapshots

Create a snapshot of all staged files:
```bash
python main.py snapshot
```
Each snapshot is assigned:
- An incremental version number
- A SHA-256 hash for integrity verification
- Binary serialization for efficient storage

### Version Information

**Check current version:**
```bash
python main.py current
```

**Check total number of snapshots:**
```bash
python main.py snaps
```

### Revert to Previous Snapshots

Revert your working directory to a specific snapshot:
```bash
python main.py revert <version_number>
```
This will:
- Restore all files from the specified snapshot
- Remove files that weren't present in that snapshot
- Preserve the repository structure

## 🔧 Technical Implementation

### Storage Structure
```
svcs/
├── house.txt              # Current active house
├── all_house.txt          # List of all available houses
├── <house_name>/
│   ├── ready/             # Staging area for files
│   └── snapshot/
│       ├── version.txt    # Current version counter
│       └── <version>/
│           └── <hash>     # Pickled snapshot data
```

### Snapshot Data Format
Each snapshot contains:
- **File contents**: Binary data for all staged files
- **File list**: Paths of all files in the snapshot
- **Integrity hash**: SHA-256 checksum for verification

### Ignore Rules

The system automatically ignores certain patterns defined in `ignore.py`:

**Directories:**
- `.venv` - Virtual environments
- `.git` - Git repositories
- `.idea` - IDE configuration
- `__pycache__` - Python cache
- `Version-control` - This project directory

**Files:**
- `.DS_Store` - macOS system files

## 🔄 Workflow Example

```bash
# Initialize repository
python main.py init

# Create a new feature house
python main.py house new feature-branch

# View all available houses
python main.py house show

# Stage your changes
python main.py ready

# Create a snapshot
python main.py snapshot

# Check current version
python main.py current

# Check total snapshots
python main.py snaps

# Switch back to main
python main.py house main

# View current house
python main.py house

# Revert to version 1 if needed
python main.py revert 1
```

## 📋 Complete Command Reference

| Command | Description |
|---------|-------------|
| `python main.py init` | Initialize SVCS repository |
| `python main.py house` | Show current active house |
| `python main.py house show` | List all available houses |
| `python main.py house <name>` | Switch to specified house |
| `python main.py house new <name>` | Create new house |
| `python main.py ready` | Stage files for snapshot |
| `python main.py snapshot` | Create snapshot from staged files |
| `python main.py current` | Show current version number |
| `python main.py snaps` | Show total number of snapshots |
| `python main.py revert <version>` | Revert to specified version |

## ⚠️ Important Notes

- Run commands from the directory containing your project files (parent of the `svcs` directory)
- SVCS must be initialized before using any commands (except `init`)
- Snapshots are created using binary serialization - they're platform-independent but not human-readable
- Reverting will **permanently delete** files not present in the target snapshot
- House names are case-sensitive
- Version numbers start from 1 and increment automatically
- Unknown commands will display a help message with available options

## 🎯 Educational Focus

This project demonstrates key version control concepts:
- **Staging areas** for preparing commits
- **Content hashing** for integrity verification
- **Binary serialization** for efficient storage
- **Branch-like systems** for parallel development
- **File tracking** and change detection
- **Command-line interface** design patterns

## 🤝 Contributing

This is an educational project. Feel free to explore, modify, and enhance the code to better understand version control systems!