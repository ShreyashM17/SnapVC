# setup.py
from setuptools import setup

setup(
    name="s_vcs",                      # This name must be unique on PyPI!
    version="0.1.0",
    packages=["s_vcs"],
    entry_points={
        "console_scripts": [
            "svcs=s_vcs.main:main",
        ]
    },
    author="Shreyash Mogaveera",
    author_email="your@email.com",
    description="A custom version control system CLI tool",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ShreyashM17/Version-control",
    python_requires='>=3.7',
)
