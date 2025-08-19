# Cross-platform ignore patterns
dir_ignore = [
    ".venv", ".git", ".idea", "__pycache__", "venv",
    "Version-control", ".svcs", "svcs",
    # Windows specific
    "node_modules", ".vs", "bin", "obj",
    # macOS specific  
    ".DS_Store.d",
    # Linux specific
    ".cache"
]

files_ignore = [
    # macOS specific
    ".DS_Store", 
    # Windows specific
    "Thumbs.db", "desktop.ini",
    # Linux specific
    ".directory",
    # Cross-platform
    ".gitignore", ".gitkeep"
]