# Local RCA Agent (LangGraph) — Toy Project

A fully local proof-of-concept for automated root-cause analysis (RCA) using:

- LangGraph orchestrator
- Logs normalizer (yaml-driven parsers)
- NetworkX knowledge graph
- Markdown RCA reports

## Structure

- `src` should contain `.py` files for deployment.
- `notebooks` should have jupyter notebooks for exploration.
- `weights` should include pre-trained weights (models).
- [config.ini](.): for mainly configuration setting
- [src/utils](./src/utils/): for utilities like custom logging

## Poetry environment for development

### Pre-requisites
>
> NOTE: You may skip these steps if you have already performed them before.

1. Install a [Git](https://git-scm.com/) client.

2. Install [pyenv](https://github.com/pyenv/pyenv#installation) (Linux & macOS) or [pyenv-win](https://github.com/pyenv-win/pyenv-win#installation) (Windows) as a Python version manager.

3. Install a recent CPython interpreter and enable it:

    ```shell
    pyenv install 3.12
    pyenv shell 3.12
    ```

4. Install [pipx](https://github.com/pypa/pipx/#install-pipx) (Please check your OS and how to install):

    ```shell
    pip install --user pipx
    python -m pipx ensurepath

5. Install [Poetry via pipx](https://code.siemens.com/micore-templates/python-package/-/blob/main/CONTRIBUTING.md?ref_type=heads#:~:text=Install-,Poetry%20via%20pipx,-%3A) (Please check your OS and how to install):

    ```shell
    pipx install "poetry>=1.8"
    ```

### Installation

1. Create a virtual environment using Python's builtin [venv](https://docs.python.org/3/library/venv.html) in `<repo_path>`:

    ```shell
    python -m venv .venv
    # Linux / macOS
    . .venv/bin/activate
    # Windows
    .venv\Scripts\activate
    ```

2. Install runtime and development dependencies:

    ```shell
    poetry install --with dev
    ```

3. Set up the git hook scripts (only once):

    run pre-commit install to set up the git hook scripts

    ```shell
    pre-commit install
    ```

    now pre-commit will run automatically on git commit!

### Usage

1. Activate the poetry environment

    ```shell
    poetry shell
    ```

2. How to install Python packages

    ```shell
    poetry add <package_name>
    ```

3. How to install dev Python packages

    ```shell
    poetry add --group dev <package_name>
    ```

4. When you want to git commit without pre-commit,

    ```shell
    git commit --no-verify
    ```

## Deployment

Create your package.

1. Build *.whl file.

    ```shell
    poetry build
    ```

2. Go to the env where you want to run

    ```shell
    pip install <.whl>
    ```

3. Then, you should be able to run main.py with this.

    ```shell
    repository
    ```

## Log useage

```python
import logging

from src.utils.logging import SetLogger

# Leave the arguments empty if you don't want to generate the log file
logger = SetLogger(log_level=logging.DEBUG).logger
```

If you installed the whl file,

```python
import logging

from .utils.logging import SetLogger
```
