try:
    import gnureadline as readline
except ImportError:
    import readline

readline.read_init_file('my_readline.rc')

while True:
    line = input('Prompt ("stop" to quit): ')
    if line == 'stop':
        break
    print('ENTERED: {!r}'.format(line))
