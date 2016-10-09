from .base import Base
import subprocess

class Code(Base):
    def run(self):
        # TODO: Make this better
        if self.options['--compile']:
            self.avr_gcc_compile()
        elif self.options['--test']:
            self.test()

    def avr_gcc_compile(self):
        # TODO: Make this better
        subprocess.run('avr-gcc -g -Os -mmcu=atmega328p -c main.cc'.split())
        subprocess.run('avr-gcc -g -mmcu=atmega328p -o main.elf main.o'.split())
        subprocess.run('avr-objcopy -j .text -j .data -O ihex main.elf main.hex'.split())

    def test(self):
        # TODO: Implement
        pass
