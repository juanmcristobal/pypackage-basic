#!/usr/bin/env python

"""The setup script."""

from pathlib import Path

from setuptools import find_packages, setup

README = Path("README.md").read_text(encoding="utf-8")
HISTORY = Path("HISTORY.md").read_text(encoding="utf-8")
REQUIRED = Path("requirements.txt").read_text(encoding="utf-8").splitlines()
DEV_REQUIRED = [
    "black==24.4.0",
    "isort==5.13.2",
    "pip==24.0",
    "bump2version==1.0.1",
    "wheel==0.43.0",
    "flake8==7.0.0",
    "tox==4.14.2",
    "coverage==7.4.4",
    "pytest==8.1.1",
    "build",
    "twine==5.1.1",
]
{% if cookiecutter.command_line_interface|lower == 'click' -%}
DEV_REQUIRED.insert(0, "Click==8.1.7")
{% endif %}

setup(
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email="{{ cookiecutter.email }}",
    python_requires=">=3.10",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    description="{{ cookiecutter.project_short_description }}",
    {%- if 'no' not in cookiecutter.command_line_interface|lower %}
    entry_points={
        "console_scripts": [
            "{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.cli:main",
        ],
    },
    {%- endif %}
    extras_require={
        "dev": DEV_REQUIRED,
    },
    install_requires=REQUIRED,
    long_description=f"{README}\n\n{HISTORY}",
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="{{ cookiecutter.project_slug }}",
    name="{{ cookiecutter.project_slug }}",
    packages=find_packages(include=["{{ cookiecutter.project_slug }}", "{{ cookiecutter.project_slug }}.*"]),
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}",
    version='{{ cookiecutter.version }}',
    zip_safe=False,
)
