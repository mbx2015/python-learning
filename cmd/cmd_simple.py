import cmd


class HellowWorld(cmd.Cmd):

    def do_greet(self, line):
        print('hello')

    def do_EOF(self, line):
        return True


if __name__ == '__main__':
    HellowWorld().cmdloop()
