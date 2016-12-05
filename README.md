# Quantus Tools
[![Build Status](https://travis-ci.org/lelandjansen/speed-of-sound.svg)](https://travis-ci.org/lelandjansen/quantus-tools)

Development environment tools and helpful scripts for [Quantus](http://github.com/lelandjansen/quantus).


## Work in Progress
Please note that this repository is a work in progress whose main purpose is to support my development workflow.


## Usage
```
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
    qtools code --compile
    qtools device --set-fuses

Help:
    For help using qtools, please open an issue on GitHub:
    https://github.com/lelandjansen/quantus-tools
'''
```
