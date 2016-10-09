from setuptools import Command, setup, find_packages
from subprocess import call
from qtools import __version__


class RunTests(Command):
    description = 'run tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        errno = call(['py.test', '--cov=qtools', '--cov-report=term-missing'])
        raise SystemExit(errno)


setup(
    name = 'qtools',
    version = __version__,
    description = 'Quantus tooling and useful scripts.',
    url = 'https://github.com/lelandjansen/quantus-tools',
    author = 'Leland Jansen',
    packages = find_packages(exclude=['docs', 'tests*']),
    install_requires = ['docopt'],
    extras_require = {
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    entry_points = {
        'console_scripts': [
            'qtools=qtools.qtools:main',
        ],
    },
    cmdclass = {'test': RunTests},
)
