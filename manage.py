import os
import unittest

from flask_script import Manager
from app import create_app


app = create_app(config_name=os.environ.get('APP_SETTINGS'))
manager = Manager(app)

# check if the environment configuration is production
is_prod = (os.environ.get('APP_SETTINGS') == 'production')


@manager.command
def test(type=""):
    """Run the unit tests without code coverage."""
    try:
        tests = unittest.TestLoader().discover(
            f'tests/{type}',
            pattern='test*.py'
        )
        result = unittest.TextTestRunner(verbosity=2).run(tests)
        if result.wasSuccessful():
            return 0
        return 1
    except ImportError:
        print("There is no test like that!")


if __name__ == "__main__":
    manager.run()
