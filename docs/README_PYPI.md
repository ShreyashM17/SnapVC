# SnapVC - Simple Version Control System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Cross-Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)](https://github.com/ShreyashM17/Version-control)

A lightweight, educational version control system written in Python. Perfect for learning how Git-like systems work internally, with a unique "house" system (similar to branches) and cross-platform compatibility.

## 🚀 Quick Start

### Install
```bash
pip install snapvc
```

### Basic Usage
```bash
# Initialize repository
svcs init

# Stage files
svcs ready

# Create snapshot
svcs snapshot

# View current version
svcs current
```

## ✨ Key Features

- **🏠 House System**: Branch-like parallel development environments
- **📸 Snapshots**: Version your code with SHA-256 integrity checking
- **🌍 Cross-Platform**: Works seamlessly on Windows, macOS, and Linux
- **📚 Educational**: Perfect for understanding version control internals
- **🚫 Smart Ignoring**: Automatically excludes OS-specific files (.DS_Store, Thumbs.db, etc.)
- **📦 Zero Dependencies**: Uses only Python standard library

## 📖 Commands

| Command | Description |
|---------|-------------|
| `svcs init` | Initialize repository in current directory |
| `svcs ready` | Stage all files for snapshot |
| `svcs snapshot` | Create versioned snapshot of staged files |
| `svcs house new <name>` | Create new development house (branch) |
| `svcs house <name>` | Switch to existing house |
| `svcs house show` | List all available houses |
| `svcs current` | Show current version number |
| `svcs revert <version>` | Restore to specific snapshot version |

## 🏠 House System (Branches)

Houses are SnapVC's equivalent to Git branches, allowing parallel development:

```bash
# Create feature house
svcs house new feature-auth

# Work on your feature
echo "login system" > auth.py
svcs ready && svcs snapshot

# Switch back to main
svcs house main

# Switch to your feature house
svcs house feature-auth
```

## 🔧 How It Works

SnapVC demonstrates core version control concepts:

- **Staging Area**: Files are prepared in a "ready" area before snapshotting
- **Content Hashing**: Each snapshot gets a unique SHA-256 hash for integrity
- **Binary Serialization**: Efficient storage using Python's pickle format
- **Path Normalization**: Cross-platform file path handling

### Storage Structure
```
.svcss/
├── house.txt              # Current active house
├── all_house.txt          # Available houses list
└── main/                  # Default house
    ├── ready/             # Staging area
    └── snapshot/
        ├── version.txt    # Version counter
        └── 1/
            └── <hash>     # Snapshot data
```

## 🌍 Cross-Platform Support

SnapVC automatically handles platform differences:

- **Windows**: Uses backslash paths, ignores `Thumbs.db`, `desktop.ini`
- **macOS**: Uses forward slash paths, ignores `.DS_Store`
- **Linux**: Supports all distributions, ignores `*~`, `.directory`

## 💡 Use Cases

### Learning & Education
- Understand version control system internals
- Learn about hashing, serialization, and file tracking
- Explore branching and parallel development concepts

### Small Projects
- Simple backup and versioning for personal projects
- Lightweight alternative when Git feels too heavy
- Experimentation with different development workflows

### Development Practice
- Practice CLI tool development patterns
- Study cross-platform Python programming
- Learn about binary data handling and file systems

## 🚦 Requirements

- **Python 3.7+**
- **Operating System**: Windows, macOS, or Linux
- **Dependencies**: None (standard library only)

## 📚 Example Workflow

```bash
# Start new project
mkdir my-project && cd my-project
svcs init

# Create some files
echo "print('Hello World')" > main.py
echo "# My Project" > README.md

# Stage and snapshot
svcs ready
svcs snapshot

# Create feature branch
svcs house new add-tests
echo "def test_hello(): pass" > test_main.py

# Stage and snapshot feature
svcs ready
svcs snapshot

# Check current state
svcs current  # Shows: You are at version 2
svcs house    # Shows: You are at add-tests

# Switch back to main
svcs house main
ls           # Only main.py and README.md (test_main.py not here)

# Go back to feature
svcs house add-tests
ls           # All files including test_main.py
```

## ⚠️ Important Notes

- **Destructive Operations**: `svcs revert` permanently deletes files not in target snapshot
- **Working Directory**: Always run commands from your project root
- **Binary Storage**: Snapshots are stored in binary format (not human-readable)
- **Case Sensitivity**: House names are case-sensitive

## 📝 License

MIT License - see full license text at [https://opensource.org/licenses/MIT](https://opensource.org/licenses/MIT)

## 👨‍💻 Author

**Shreyash Mogaveera**  
GitHub: [@ShreyashM17](https://github.com/ShreyashM17)

---

**Learn version control by building it yourself!** 🚀

*SnapVC makes complex version control concepts accessible through hands-on experience.* 