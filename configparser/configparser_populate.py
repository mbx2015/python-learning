import configparser

parser = configparser.SafeConfigParser()

parser.add_section('bug_tracker')
parser.set('bug_tracker', 'url', 'http://localhost:8080/bugs')
parser.set('bug_tracker', 'username', 'mbx2017')
parser.set('bug_tracker', 'password', 'S3cr3t')

for section in parser.sections():
    print(section)
    for name, value in parser.items(section):
        print(' {} = {!r}'.format(name, value))
