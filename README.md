# Cookiecutter PyPackage Basic

A Cookiecutter template for generating small Python packages with a modern baseline.

## What it generates

- Python 3.10 to 3.13 support
- `pyproject.toml` for build and tool config
- `setup.py` and `setup.cfg` for compatibility with older tooling
- optional Click CLI scaffolding
- optional package type selection, with Python and Rust variants
- `dev` extra for editable installs with development tools
- `pytest`, `black`, `isort`, `flake8`, `tox`, `coverage`, and `build`
- GitHub Actions workflows for the template and generated projects

## Usage

Install the template tooling:

```bash
pip install -U cookiecutter cruft
```

Generate a new project:

```bash
cruft create git@github.com:juanmcristobal/pypackage-basic.git
```

Then in the generated project:

```bash
pip install -e ".[dev]"
make lint
make test
make coverage
make dist
```

## Changelog

- `package_type` is now the main variant question.
- `python` keeps the release workflow on `python -m build` plus `twine`.
- `rust` switches the release workflow to a `maturin` matrix build with shared PyPI publish.
- `requirements_dev.txt` has been removed in favor of the `dev` extra.
- `setup.py` and `setup.cfg` remain for compatibility, but `pyproject.toml` and `pip install -e ".[dev]"` are the preferred path.
