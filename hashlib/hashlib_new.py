import argparse
import hashlib
import sys

from hashlib_data import lorem

parser = argparse.ArgumentParser('Hashlib demo')
parser.add_argument('hash_name', choices=hashlib.algorithms_available, help='the name of the algorithm to use')
parser.add_argument('data', nargs='?', default=lorem, help='the default data to hash default to lorem ipsum')

args = parser.parse_args()

h = hashlib.new(args.hash_name)
h.update(args.data.encode('utf-8'))
print(h.hexdigest())
