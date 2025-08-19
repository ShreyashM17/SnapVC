from setuptools import setup

with open("docs/README_PYPI.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="snapvc",
    version="1.2.1",
    author="Shreyash Mogaveera",
    author_email="shreyashmogaveera@gmail.com",
    description="A lightweight version control system with cross-platform support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ShreyashM17/SnapVC",
    project_urls={
        "Bug Tracker": "https://github.com/ShreyashM17/SnapVC/issues",
        "Documentation": "https://github.com/ShreyashM17/SnapVC#readme",
        "Source Code": "https://github.com/ShreyashM17/SnapVC",
    },
    packages=["snapvc"],
    entry_points={
        "console_scripts": [
            "svcs=snapvc.main:main",
        ],
    },
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Topic :: Software Development :: Version Control",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    keywords=[
        "version-control",
        "vcs", 
        "educational",
        "git",
        "snapshots",
        "cross-platform",
        "cli",
        "learning",
        "development-tools"
    ],
    python_requires=">=3.7",
    license="MIT",
    zip_safe=False,
)
