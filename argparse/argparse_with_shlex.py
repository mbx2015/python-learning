import argparse
import shlex
from configparser import ConfigParser

parser = argparse.ArgumentParser(description='Short simple app')

parser.add_argument('-a', action='store_true', default=False)
parser.add_argument('-b', action='store', dest='b')
parser.add_argument('-c', action='store', dest='c', type=int)

config = ConfigParser()
config.read('argparse_with_shlex.ini')

config_value = config.get('cli', 'options')
print('Config: ', config_value)

argument_list = shlex.split(config_value)
print('Arg list: ', argument_list)

print('Results: ', parser.parse_args(argument_list))
