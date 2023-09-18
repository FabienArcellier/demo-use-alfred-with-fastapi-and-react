import alfred

import os

@alfred.command("frontend:tests", help="run automatic test on frontend")
def frontend_tests():
    """
    >>> $ alfred frontend:tests
    """
    with alfred.env(CI='1'):
        os.chdir('frontend')
        alfred.run("npm test")
