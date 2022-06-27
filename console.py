#!/usr/bin/python3
import cmd, sys, os

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    # ----- basic CLI commands ----- #
    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        quit()
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program\n"""
        quit()
        return True

    def emptyline(self):
        """Pass on empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
