"""Tasks to be performed using invoke."""
from invoke import task


@task
def black(context):
    """Python Code Style."""
    command = "black ."
    context.run(command)


@task
def flake8(context):
    """PEP8 Compliance."""
    command = "flake8 . --config .flake8"
    context.run(command)


@task
def bandit(context):
    """Python Security Analysis."""
    command = "bandit . --recursive --configfile .bandit.yml"
    context.run(command)


@task
def pydocstyle(context):
    """Python Docstring Compliance."""
    command = "pydocstyle ."
    context.run(command)


@task
def yamllint(context):
    """YAML Syntax and Cosmetic Analysis."""
    command = "yamllint ."
    context.run(command)


@task
def pylint(context):
    """Python Code Analysis."""
    command = "pylint *.py --rcfile pyproject.toml"
    context.run(command)


@task
def tests(context):
    """Run all linters."""
    print("Black...")
    black(context)
    print("Flake8...")
    flake8(context)
    print("Bandit...")
    bandit(context)
    print("Pydocstyle...")
    pydocstyle(context)
    print("Yamllint...")
    yamllint(context)
    print("Pylint...")
    pylint(context)
