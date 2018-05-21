from configparser import ConfigParser

parser = ConfigParser()

candidates = ['does_not_exist.ini', 'also_does_not_exist.ini', 'simple.ini', 'multi_section.ini']
found = parser.read(candidates)
missing = set(candidates) - set(found)

print('Found config files:', sorted(found))
print('Missing files     :', sorted(missing))
