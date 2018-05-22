import subprocess

completed = subprocess.run(
    ['ls', '-l'],
    stdout=subprocess.PIPE
)

print('returncode:', completed.returncode)
print('Have {} bytes in stdout: \n{}'.format(
    len(completed.stdout),
    completed.stdout.decode('utf-8')
))
