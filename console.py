#!/usr/bin/python3
import cmd
import sys
import os
import json
import models
import shlex


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

    # ----- extended CLI commands ----- #
    def do_create(self, arg):
        """Creates a new instance of BaseModel, \
        saves it (to the JSON file) and prints the id.\n"""
        pass

    def do_show(self, arg):
        """Prints the string representation of \
        an instance based on the class name and id.\n"""
        pass

    def do_destroy(self, arg):
        """Deletes an instance based on the class \
        name and id (save the change into the JSON file).\n"""
        pass

    def do_all(self, arg):
        """Prints all string representation of all \
        instances based or not on the class name.\n"""
        pass

    def do_update(self, arg):
        """Updates an instance based on the class name \
        and id by adding or updating attribute (save \
        the change into the JSON file).\n"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
