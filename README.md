# SnapVC - Simple Version Control System

A Python-based lightweight version control system inspired by Git, designed as an educational project to demonstrate core version control concepts. This system features a unique "house" system (similar to branches), staging areas, snapshot creation with SHA-256 hashing, and file reversion capabilities.

## ✨ Features

- **📦 Python Package**: Installable via pip with cross-platform compatibility
- **🏠 House System**: Create and switch between different "houses" (similar to Git branches)
- **📋 File Staging**: Stage files in a "ready" area before snapshotting
- **📸 Snapshot Creation**: Create versioned snapshots using SHA-256 hashing and binary serialization
- **⏪ File Reversion**: Revert to any previous snapshot
- **🚫 Smart Ignore Patterns**: Cross-platform file/directory exclusion rules
- **📈 Incremental Versioning**: Automatic version numbering for snapshots
- **📊 Version Tracking**: View current version and total snapshot count
- **🌍 Cross-Platform**: Works on Windows, macOS, and Linux

## 📁 Project Structure

```
snapvc/
├── snapvc/
│   ├── __init__.py       # Package initialization
│   ├── main.py           # CLI entry point and command parser
│   ├── housing.py        # House (branch-like) management system
│   ├── snapshot.py       # Snapshot creation and versioning logic
│   ├── staging.py        # File staging and ready area management
│   ├── revert.py         # Snapshot reversion functionality
│   └── ignore.py         # Cross-platform file/directory ignore patterns
├── setup.py              # Package installation configuration
├── pyproject.toml        # Modern Python packaging metadata
├── LICENSE               # MIT License
└── README.md             # This file
```

## 🚀 Installation

### Option 1: Install from Source (Recommended for Development)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ShreyashM17/Version-control.git
   cd Version-control
   ```

2. **Install in development mode:**
   ```bash
   pip install -e .
   ```

3. **Verify installation:**
   ```bash
   svc --help
   ```

### Option 2: Install from PyPI (When Published)

```bash
pip install snapvc
```

### System Requirements

- **Python 3.7+** 
- **Operating Systems**: Windows, macOS, Linux
- **Dependencies**: None (uses only Python standard library)

## 📖 Usage Guide

### Initialize a Repository

Initialize SnapVC in the current directory:
```bash
svc init
```
This creates a `.svcs` directory with the default "main" house.

### House Management

Houses are similar to Git branches, allowing you to work on different versions simultaneously.

**View current house:**
```bash
svc house
```

**View all available houses:**
```bash
svc house show
```

**Create a new house:**
```bash
svc house new <house_name>
```

**Switch to an existing house:**
```bash
svc house <house_name>
```

### File Staging

Stage files for snapshotting (prepares files in the "ready" area):
```bash
svc ready
```
This command stages all files from the current directory, respecting cross-platform ignore patterns.

### Create Snapshots

Create a snapshot of all staged files:
```bash
svc snapshot
```
Each snapshot is assigned:
- An incremental version number
- A SHA-256 hash for integrity verification
- Binary serialization for efficient storage

### Version Information

**Check current version:**
```bash
svc current
```

**Check total number of snapshots:**
```bash
svc snaps
```

### Revert to Previous Snapshots

Revert your working directory to a specific snapshot:
```bash
svc revert <version_number>
```
This will:
- Restore all files from the specified snapshot
- Remove files that weren't present in that snapshot
- Preserve the repository structure

## 🔧 Technical Implementation

### Storage Structure
```
.svcs/
├── house.txt              # Current active house
├── all_house.txt          # List of all available houses
└── <house_name>/
    ├── ready/             # Staging area for files
    └── snapshot/
        ├── version.txt    # Current version counter
        ├── current_version.txt  # Working version tracker
        └── <version>/
            └── <hash>     # Pickled snapshot data
```

### Cross-Platform Compatibility

SnapVC is designed to work seamlessly across different operating systems:

- **🪟 Windows**: Uses proper path separators (`\`) and handles Windows-specific files
- **🍎 macOS**: Ignores `.DS_Store` files and handles Unix-style paths
- **🐧 Linux**: Supports all Linux distributions with proper file permissions

### Smart Ignore Patterns

The system automatically ignores platform-specific files and directories:

**Cross-Platform Directories:**
```
.venv, .git, .idea, __pycache__, node_modules
```

**Cross-Platform Files:**
```
# Windows: Thumbs.db, desktop.ini, *.tmp
# macOS: .DS_Store
# Linux: .directory, *~, .cache
```

### Snapshot Data Format

Each snapshot contains:
- **File contents**: Binary data for all staged files (cross-platform compatible)
- **File list**: Normalized paths of all files in the snapshot
- **Integrity hash**: SHA-256 checksum for verification
- **Metadata**: Version information and timestamps

## 🔄 Workflow Example

```bash
# Install SnapVC
pip install -e .

# Initialize repository
svc init

# Create a new feature house
svc house new feature-branch

# View all available houses
svc house show

# Stage your changes
svc ready

# Create a snapshot
svc snapshot

# Check current version
svc current

# Check total snapshots
svc snaps

# Switch back to main
svc house main

# View current house
svc house

# Revert to version 1 if needed
svc revert 1
```

## 📋 Complete Command Reference

| Command | Description | Example |
|---------|-------------|---------|
| `svc init` | Initialize SnapVC repository | `svc init` |
| `svc house` | Show current active house | `svc house` |
| `svc house show` | List all available houses | `svc house show` |
| `svc house <name>` | Switch to specified house | `svc house main` |
| `svc house new <name>` | Create new house | `svc house new feature` |
| `svc ready` | Stage files for snapshot | `svc ready` |
| `svc snapshot` | Create snapshot from staged files | `svc snapshot` |
| `svc current` | Show current version number | `svc current` |
| `svc snaps` | Show total number of snapshots | `svc snaps` |
| `svc revert <version>` | Revert to specified version | `svc revert 1` |

## 🌟 What Makes SnapVC Special

### 🔄 Educational Value
- **Learn Version Control**: Understand how Git-like systems work internally
- **Binary Serialization**: See how data is efficiently stored and retrieved
- **Hash-based Integrity**: Experience content-addressable storage
- **Branch Simulation**: Explore parallel development workflows

### 🛡️ Production-Ready Features
- **Cross-Platform**: Runs on Windows, macOS, and Linux
- **Type Safety**: Proper error handling and validation
- **Path Normalization**: Handles different OS path conventions
- **Smart Ignoring**: Platform-aware file filtering

### 📚 Learning Concepts Demonstrated
- **Staging Areas**: Preparing commits before finalization
- **Content Hashing**: Ensuring data integrity with SHA-256
- **Binary Serialization**: Efficient data storage with Python's pickle
- **Branch-like Systems**: Parallel development workflows
- **File Tracking**: Monitoring changes across versions
- **CLI Design**: Building professional command-line interfaces

## ⚠️ Important Notes

- **Working Directory**: Run SnapVC commands from your project's root directory
- **Initialization Required**: Must run `svc init` before using other commands
- **Binary Storage**: Snapshots use binary serialization (platform-independent but not human-readable)
- **Destructive Revert**: Reverting permanently deletes files not in target snapshot
- **Case Sensitivity**: House names are case-sensitive
- **Version Numbering**: Starts from 1 and increments automatically
- **Cross-Platform Paths**: All paths are normalized for the target operating system

## 🧪 Development & Testing

### Running Tests
```bash
# Basic functionality test
svc init
echo "Hello World" > test.txt
svc ready
svc snapshot
svc current
```

### Development Installation
```bash
git clone https://github.com/ShreyashM17/Version-control.git
cd Version-control
pip install -e .  # Editable installation for development
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Shreyash Mogaveera**
- Email: shreyashmogaveera@gmail.com
- GitHub: [@ShreyashM17](https://github.com/ShreyashM17)

## 🤝 Contributing

This is an educational project, but contributions are welcome! Feel free to:

1. 🐛 Report bugs or issues
2. 💡 Suggest new features
3. 📝 Improve documentation
4. 🔧 Submit pull requests

## 🎯 Future Enhancements

Potential improvements for learning and development:

- **🌐 Remote Repositories**: Add support for remote snapshot storage
- **🔀 Merge Capabilities**: Implement house merging functionality
- **📊 Visual Diff**: Show differences between snapshots
- **🏷️ Tagging System**: Add meaningful labels to snapshots
- **📈 Statistics**: Show repository statistics and analytics
- **🔐 Encryption**: Optional snapshot encryption for sensitive data

---

**Happy version controlling with SnapVC! 🚀**

*Learn, explore, and understand how version control systems work under the hood.*