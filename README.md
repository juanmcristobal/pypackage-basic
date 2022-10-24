# Cookiecutter PyPackage Basic

Cookiecutter template for a Python package.

* GitHub repo:

## Features

* Testing setup with ``pytest``
* Tox_ testing: Setup to easily test for Python 3.6, 3.7, 3.8, 3.9, 3.10 and 3.11.rc-2
* Reformat code with `Black`
* Sort imports alphabetically, and automatically separated into sections and by type with `isort`
* bump2version_: Pre-configured version bumping with a single command
* Command line interface using Click (optional)
* Github actions

_Cookiecutter: https://github.com/cookiecutter/cookiecutter


## Quickstart

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter git@github.com:juanmcristobal/pypackage-basic.git

Then:

* Create a repo and put it there.
* Install the dev requirements into a virtualenv. ( ``pip install -r requirements_dev.txt`` ) & ( ``pip install -r requirements_dev_others.txt`` )
* Release your package by pushing a new tag to master.
* Add a ``requirements.txt`` file that specifies the packages you will need for

