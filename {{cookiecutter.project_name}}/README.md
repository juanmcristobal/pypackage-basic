# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

{% if cookiecutter.package_type|lower == 'rust' %}
This project was generated as a Rust-backed Python package.
{% else %}
This project was generated as a pure Python package.
{% endif %}

## Quick Start

Install the project in editable mode:

```bash
pip install -e ".[dev]"
```

Run the standard checks:

```bash
make lint
make test
make coverage
make dist
```

## Project Layout

This template includes:

- Python 3.10 to 3.13 support
- `pyproject.toml` for build and tool configuration
- `setup.py` compatibility for setuptools-based installs
- optional Click CLI scaffolding
- `dev` extra for editable installs with development tools
- `pytest`, `black`, `isort`, `flake8`, `tox`, `coverage`, and `build`
- GitHub Actions CI for tests and release automation

{% if cookiecutter.package_type|lower == 'rust' %}
## Rust Package Notes

The release workflow uses `maturin` and builds wheels for multiple platforms before publishing to PyPI.
{% else %}
## Python Package Notes

The release workflow builds source and wheel distributions with `python -m build` before publishing to PyPI.
{% endif %}

## Notes

- `setup.py` and `setup.cfg` are kept for compatibility with the older workflow.
- `pyproject.toml` is the preferred place for formatter and test configuration in new projects.
- `pip install -e ".[dev]"` is the supported development install path.
- The old `requirements_dev.txt` flow has been removed.
- If CLI generation is disabled, `hooks/post_gen_project.py` removes the generated `cli.py`.
