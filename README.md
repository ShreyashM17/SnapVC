# SnapVC - Simple Version Control System

A lightweight, Python-based version control system inspired by Git. Features a unique "house" system (similar to branches), content-addressable storage with gzip compression, and cross-platform compatibility.

## ✨ Key Features

- **🏠 House System**: Git-like branches for parallel development
- **📋 Staging & Snapshots**: Stage files and create versioned snapshots with SHA-256 hashing
- **🔍 Content-Addressable Storage**: Hash-based storage with automatic deduplication
- **🗜️ Gzipped Storage**: Compressed snapshots for efficient disk usage
- **📊 JSON Metadata**: Structured version tracking with complete file lifecycle
- **⏪ Smart Reversion**: Intelligent file restoration with proper lifecycle management
- **🌍 Cross-Platform**: Works seamlessly on Windows, macOS, and Linux
- **🚫 Smart Ignoring**: Platform-aware file filtering

## 🚀 Installation

```bash
# From source (recommended for development)
git clone https://github.com/ShreyashM17/SnapVC.git
cd SnapVC
pip install -e .

# From PyPI (when published)
pip install snapvc
```

**Requirements**: Python 3.7+ (no external dependencies)

## 📖 Quick Start

```bash
# Initialize repository
svcs init

# Stage files
svcs ready

# Create snapshot
svcs snapshot

# Check version info
svcs current    # Current version
svcs snaps      # Total snapshots

# Work with houses (branches)
svcs house new feature    # Create new house
svcs house feature        # Switch to house
svcs house show          # List all houses

# Revert to previous version
svcs revert 1
```

## 📋 Command Reference

| Command | Description |
|---------|-------------|
| `svcs init` | Initialize SnapVC repository |
| `svcs ready` | Stage files for snapshot |
| `svcs snapshot` | Create snapshot from staged files |
| `svcs current` | Show current version |
| `svcs snaps` | Show total snapshots |
| `svcs house [name]` | Show current house or switch to house |
| `svcs house new <name>` | Create new house |
| `svcs house show` | List all houses |
| `svcs revert <version>` | Revert to specified version |

## 🗂️ Storage Architecture

```
your-project/
├── .svcs/
│   ├── house.txt              # Current active house
│   ├── all_house.txt          # All available houses
│   ├── main/                  # Default house
│   │   ├── data.json          # Version metadata
│   │   ├── ready/             # Staging area
│   │   └── snapshot/          # Content-addressable storage (gzipped)
│   │       ├── a1b2c3d4...    # Files stored by SHA-256 hash (compressed)
│   │       └── e5f6g7h8...    # Automatic deduplication
│   └── feature/               # Other houses (independent metadata, shared content)
└── your-files.txt
```

### JSON Metadata Schema
```json
{
  "current_version": 2,
  "all_versions": [1, 2],
  "/path/to/file.txt": {
    "added_in": 1,
    "deleted_in": 0,
    "updated_hash": "a1b2c3d4e5f6g7h8...",
    "all_hashes": {
      "1": "old_hash",
      "2": "new_hash"
    }
  }
}
```

## 🔧 Technical Highlights

- **Content Deduplication**: Identical files share storage across houses
- **Hash-Based Integrity**: SHA-256 ensures data integrity and enables O(1) lookup
- **Gzipped Storage**: Snapshot files are compressed for efficient storage
- **File Lifecycle Tracking**: Automatic detection of additions, modifications, deletions
- **Cross-Platform Paths**: OS-agnostic path handling with proper normalization
- **Smart Ignore Patterns**: Platform-specific files automatically excluded

## 📚 Learning Concepts

While SnapVC started as a side project, it demonstrates several important software engineering concepts:

- **Staging Areas** and commit preparation workflows
- **Content Hashing** and integrity verification  
- **Binary Serialization** and compression (gzip) for efficient storage
- **Content-Addressable Storage** and deduplication strategies
- **Branch-like Systems** for parallel development workflows
- **CLI Design** and cross-platform development considerations

These concepts are valuable for understanding how real version control systems work under the hood.

## ⚠️ Important Notes

- Run commands from your project's root directory
- Must run `svcs init` before other commands
- Files must be staged with `svcs ready` before snapshots
- House names are case-sensitive
- Version numbering starts from 1
- Content stored by SHA-256 hash for deduplication and integrity
- Snapshot files are gzipped for efficient storage

## 🧪 Testing

```bash
# Basic test
svcs init && echo "test" > file.txt && svcs ready && svcs snapshot

# Test deduplication
echo "same content" > file1.txt && echo "same content" > file2.txt
svcs ready && svcs snapshot  # Both files share same storage hash

# Test houses
svcs house new feature && svcs ready && svcs snapshot  # Shared storage
```

## 📄 License & Contributing

- **License**: MIT License
- **Author**: Shreyash Mogaveera ([@ShreyashM17](https://github.com/ShreyashM17))
- **Contributing**: Bug reports, features, and documentation improvements welcome!

---

**A lightweight version control system that's both practical and educational! 🚀**