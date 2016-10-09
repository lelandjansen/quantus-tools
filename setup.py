from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup

from qtools import __version__


this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()


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
    long_description = long_description,
    url = 'https://github.com/lelandjansen/quantus-tools',
    author = 'Leland Jansen',
    keywords = 'cli',
    packages = find_packages(exclude=['docs', 'tests*']),
    install_requires = ['docopt'],
    extras_require = {
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    entry_points = {
        'console_scripts': [
            'qtools=qtools.cli:main',
        ],
    },
    cmdclass = {'test': RunTests},
)
