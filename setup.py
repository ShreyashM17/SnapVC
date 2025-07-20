from setuptools import setup

with open('Readme.md', 'r') as f:
  description = f.read()

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
  author_email="shreyashmogaveera@gmail.com",
  license="MIT",
  description='A simple version control system written in Python',
  long_description=description,
  long_description_content_type="text/markdown",
  url='https://github.com/ShreyashM17/Version-control',
  classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
  ],
  python_requires='>=3.7',
)
