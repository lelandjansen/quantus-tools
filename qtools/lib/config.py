import os
from pathlib import Path
import yaml

class Config:

    def locate_file(file_name):
        file_path = '{}/{}'.format(os.getcwd(), file_name)
        if not Path(file_path).is_file():
            raise FileNotFoundError('cannot find {} configuration file.'
                .format(file_dir.split('/')[-1]))
        return file_path

    def value(option, config_file):
        with open(config_file, 'r') as f:
            value = yaml.load(f)
            for o in option.split('.'):
                try:
                    value = value[o]
                except KeyError:
                    err_msg = 'configuration file \'{}\' has no option \'{}\'' \
                        .format(config_file, o)
                    raise KeyError(err_msg)
        return value
