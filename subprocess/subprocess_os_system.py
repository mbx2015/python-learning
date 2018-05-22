import subprocess

completeed = subprocess.run(['ls', '-l'])

print('returncode: ', completeed.returncode)
