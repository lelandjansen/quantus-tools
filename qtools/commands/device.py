import os
from .base import Base
from qtools.lib.config import Config
from qtools.lib.fuse import Fuse

class Device(Base):

    def run(self):
        self.qtools_config_path = Config.locate_file('qtools.yml')
        self.quantus_config_path = Config.locate_file('quantus.yml')
        base_command = [
            'avrdude',
            '-p', Config.value('microcontroller.model', self.quantus_config_path),
            '-c', Config.value('programmer.model', self.qtools_config_path),
            '-P', Config.value('programmer.port', self.qtools_config_path)
        ]

        return base_command + self.subprocess_command()


    def subprocess_command(self):
        command = list()
        for k, v in self.options.items():
            if k.startswith('--') and v:
                method = k.strip('-').replace('-', '_')
                try:
                    command += getattr(self, method)()
                except AttributeError:
                    err_msg = '\'{}\' has no method \'{}\''.format(
                        self.__class__.__name__.lower(), method)
                    raise NotImplementedError(err_msg)

        return command


    def check_connection(self):
        return []


    def upload(self):
        return ['-U', 'flash:w:main.hex']


    def set_fuses(self):
        model = Config.value('microcontroller.model', self.quantus_config_path)
        fuse_config_path = '{}/../resources/fuse.yml'.format(
            os.path.dirname(os.path.realpath(__file__)))
        default_fuses = Config.value('{}.fuses'.format(model), fuse_config_path)
        device_fuses = Config.value('microcontroller.fuses', self.quantus_config_path)

        command = list()
        for fuse in sorted(list(default_fuses.keys())):
            fuse_value = Fuse.value(default_fuses[fuse], device_fuses.get(fuse))
            command += ['-U', '{}fuse:w:0x{:0>2X}:m'.format(fuse[0], fuse_value)]

        return command
