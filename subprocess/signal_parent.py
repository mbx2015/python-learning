import os
import signal
import subprocess
import sys

import time

proc = subprocess.Popen(['python', 'signal_child.py'])
print('PARENT:      : Pausing before sending signal...')
sys.stdout.flush()
time.sleep(1)
print('PARENT       : Signaling child')
sys.stdout.flush()
os.kill(proc.pid, signal.SIGUSR1)
