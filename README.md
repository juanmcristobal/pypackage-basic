# Cookiecutter PyPackage Basic

A Cookiecutter template to kick-start your Python packaging with modern tools and practices.

[![python](https://img.shields.io/badge/Python-3.8-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![python](https://img.shields.io/badge/Python-3.9-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![python](https://img.shields.io/badge/Python-3.10-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![python](https://img.shields.io/badge/Python-3.11-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![python](https://img.shields.io/badge/Python-3.12-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
![GitHub Actions](https://img.shields.io/github/actions/workflow/status/juanmcristobal/pypackage-basic/test.yml?branch=master)

## Features

- **Testing Setup**: Uses `pytest` for testing.
- **Tox Testing**: Pre-configured environments for Python versions 3.6 through 3.11.rc-2.
- **Code Formatting**: Utilizes `Black` for code formatting.
- **Import Sorting**: Arranges imports using `isort`.
- **Version Management**: Simplifies version bumps with `bump2version`.
- **CLI Support**: Optionally creates a command line interface using `Click`.
- **CI/CD**: Integrates GitHub Actions for Continuous Integration.

## Quickstart

### Prerequisites

Ensure you have Cookiecutter 1.4.0 or higher and cruft installed:
```bash
pip install -U cookiecutter cruft
```

### Generate Your Project

Create your new Python package project with a single command:
```bash
cruft create git@github.com:juanmcristobal/pypackage-basic.git
```

### Next Steps

- **Initialize Your Git Repository**:
  Create a new repository on GitHub and push your project files.
- **Setup Development Environment**:
  Install development dependencies within a virtual environment:
  ```bash
  pip install -r requirements_dev.txt
  ```
- **Prepare for Release**:
  Release your package by tagging your commits and pushing them to the master branch.
- **Manage Dependencies**:
  Maintain a `requirements.txt` file specifying necessary production dependencies.
