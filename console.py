#!/usr/bin/python3
"""
This is a module for HBNBCommand class.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()