# SnapVC - Simple Version Control System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Cross-Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)](https://github.com/ShreyashM17/Version-control)

A lightweight, educational version control system with Git-like "house" branches, content-addressable storage, and cross-platform compatibility. Perfect for learning version control internals.

## 🚀 Quick Start

```bash
# Install
pip install snapvc

# Initialize and create first snapshot
svcs init
echo "Hello World" > file.txt
svcs ready && svcs snapshot

# Check status
svcs current  # Current version
svcs snaps    # Total snapshots
```

## ✨ Key Features

- **🏠 House System**: Git-like branches for parallel development
- **📸 Content-Addressable Storage**: SHA-256 hashing with automatic deduplication
- **🗜️ Gzipped Storage**: Compressed snapshots for efficient disk usage
- **🌍 Cross-Platform**: Windows, macOS, Linux support
- **📚 Educational**: Learn version control internals hands-on
- **📦 Zero Dependencies**: Python standard library only

## 📖 Essential Commands

| Command | Description |
|---------|-------------|
| `svcs init` | Initialize repository |
| `svcs ready` | Stage files for snapshot |
| `svcs snapshot` | Create versioned snapshot |
| `svcs house new <name>` | Create new house (branch) |
| `svcs house <name>` | Switch to house |
| `svcs current` | Show current version |
| `svcs revert <version>` | Restore to specific version |

## 🏠 House System Example

```bash
# Create feature branch
svcs house new feature
echo "new feature" > feature.py
svcs ready && svcs snapshot

# Switch back to main
svcs house main  # feature.py disappears

# Switch to feature
svcs house feature  # feature.py reappears
```

## 🔧 How It Works

- **Staging**: Files prepared in "ready" area before snapshotting
- **Hashing**: SHA-256 ensures integrity and enables deduplication
- **Compression**: Gzipped storage for efficient disk usage
- **Storage**: Content-addressable storage with automatic file sharing
- **Houses**: Independent version histories with shared content pool

```
.svcs/
├── house.txt           # Current house
├── main/              # Default house
│   ├── data.json      # Version metadata
│   ├── ready/         # Staging area
│   └── snapshot/      # Content by hash (gzipped)
└── feature/           # Other houses
```

## 💡 Perfect For

- **Learning**: Understand Git-like systems internally
- **Education**: Teaching version control concepts
- **Small Projects**: Lightweight versioning without Git complexity
- **Experimentation**: Try different workflows and branching strategies

## ⚠️ Requirements

- Python 3.7+
- Any OS (Windows, macOS, Linux)
- No external dependencies

## 📚 Documentation

For detailed documentation, examples, and architecture details, visit:
[https://github.com/ShreyashM17/SnapVC](https://github.com/ShreyashM17/Snapvc)

## 📝 License & Author

- **License**: MIT
- **Author**: Shreyash Mogaveera ([@ShreyashM17](https://github.com/ShreyashM17))

---

**Learn version control by building it! 🚀** 