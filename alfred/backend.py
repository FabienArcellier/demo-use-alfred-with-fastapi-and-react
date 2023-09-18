import alfred


@alfred.command("backend:lint", help="check type consistency of backend")
def lint():
    """
    check the type consistency with mypy

    >>> $ alfred lint
    """
    mypy = alfred.sh("mypy", "mypy should be present")
    alfred.run(mypy, ['backend/'])


@alfred.command("backend:tests", help="workflow to execute all automatic tests")
def tests():
    """
    execute tests with unittests

    >>> $ alfred tests
    """
    pytest = alfred.sh("pytest")
    alfred.run(pytest, ['backend/tests'])
