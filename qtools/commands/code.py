from .base import Base
from qtools.lib.config import Config

class Code(Base):
    def run(self):
        # TODO: Make this better (use techniue from device)
        if self.options['--compile']:
            return self.avr_gcc_compile()
        elif self.options['--test']:
            return self.test()

    def avr_gcc_compile(self):
        # TODO: Refactor (and remove duplication) for use with CMake
        quantus_config_path = Config.locate_file('quantus.yml')
        mmcu = Config.value('microcontroller.model', quantus_config_path)
        compile1 = 'avr-gcc -g -Os -mmcu={} -c main.cc -std=c++11'.format(mmcu).split()
        compile2 = 'avr-gcc -g -mmcu={} -o main.elf main.o'.format(mmcu).split()
        compile3 = 'avr-objcopy -j .text -j .data -O ihex main.elf main.hex'.split()
        return [compile1, compile2, compile3]

    def test(self):
        # TODO: Implement
        pass
