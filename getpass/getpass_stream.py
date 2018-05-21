import getpass
import sys

p = getpass.getpass(stream=sys.stderr)
print('You entered:', p)

# python getpass_stream.py >/dev/null
