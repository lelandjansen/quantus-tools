'''
Quantus Tools (qtools)

Usage:
    qtools bootstrap
    qtools code (-c | --compile)
    qtools code (-t | --test)
    qtools device (-C | --check-connection)
    qtools device (-u | --upload)
    qtools device (-f | --set-fuses)
    qtools hello
    qtools (-h | --help)
    qtools --version

Options:
    -h --help              Show this help message
    --version              Show qtools version
    -c --compile           Compile code using avr-gcc
    -t --test              Run code tests
    -C --check-connection  Check if microcontroller is connected using avrdude
    -u --upload            Upload hex file to microcontroller using avrdude
    -f --set-fuses         Set microcontroller fuses using avrdude

Examples:
    qtools bootstrap

Help:
    For help using qtools, please open an issue on GitHub:
    https://github.com/lelandjansen/quantus-tools
'''
# Good resource: https://stormpath.com/blog/building-simple-cli-interfaces-in-python

from docopt import docopt
VERSION = '0.0.1' # from . import __version__ as VERSION
from inspect import getmembers, isclass
from commands.base import Base
from lib.config import Config
import subprocess


def main():
    options = docopt(__doc__, version = VERSION)
    commands = dict((sc.__name__.lower(), sc) for sc in Base.__subclasses__())
    for k, v in options.items():
        if k in commands and v:
            command = commands[k](options).run()
            subprocess.run(command)


main() # TODO: remove