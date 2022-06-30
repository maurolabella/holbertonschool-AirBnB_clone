#!/usr/bin/python3
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import cmd
import sys
import os
import json
import models
import shlex


systemClasses = {"BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    # ----- basic CLI commands ----- #
    def do_quit(self, arg):
        """Quit command to exit the program"""
        quit()

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        quit()

    def emptyline(self):
        """Pass on empty line"""
        return

    # ----- extended CLI commands ----- #
    def do_create(self, arg):
        """Creates a new instance of BaseModel, \
saves it (to the JSON file) and prints the id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in systemClasses:
            print("** class doesn't exist **")
            return
        else:
            myObject = eval(args[0])()
            myObject.save()
            print(myObject.id)
            return

    def do_show(self, arg):
        """Prints the string representation of \
an instance based on the class name and id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif args[0] not in systemClasses:
            print("** class doesn't exist **")
            return
        else:
            myObject = "{}.{}".format(args[0], args[1])
            if myObject not in models.storage.all().keys():
                print("** no instance found **")
                return
            else:
                print("[{}] ({}) {}".format(args[0], myObject[1],
                      models.storage.all()[myObject]))
                return

    def do_destroy(self, arg):
        """Deletes an instance based on the class \
name and id (save the change into the JSON file)."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif args[0] not in systemClasses:
            print("** class doesn't exist **")
            return
        else:
            key = args[0] + "." + args[1]
            if key in models.storage.all():
                del models.storage.all()[key]
                models.storage.save()
                return
            else:
                print("** no instance found **")
                return

    def do_all(self, arg):
        """Prints all string representation of all \
instances based or not on the class name."""
        args = shlex.split(arg)
        myObject = models.storage.all()
        myObjectsList = []

        if not args:
            print("** class name missing **")
            return
        elif args[0] not in systemClasses:
            print("** class doesn't exist **")
            return
        else:
            for key, value in myObject.items():
                if arg in key:
                    classIdTokens = key.split(".")
                    classId = "[" + classIdTokens[0] + "]"\
                              + " (" + classIdTokens[1] + ")"
                    myObjectsList.append(classId + " " + str(value))
                    print(myObjectsList)
            return

    def do_update(self, arg):
        """Updates an instance based on the class name \
and id by adding or updating attribute (save \
the change into the JSON file)."""
        args = shlex.split(arg)

        if not args:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing  **")
            return
        elif len(args) == 2:
            print("** attribute name missing  **")
            return
        elif len(args) == 3:
            print("** value missing  **")
            return
        elif args[0] not in systemClasses:
            print("** class doesn't exist **")
            return
        else:
            classId = args[0] + "." + args[1]
            myObject = models.storage.all()

            if classId not in myObject:
                print("** no instance found **")
                return
            else:
                setAttr = args[2]
                setAttrValue = args[3].strip('"')
                setattr(myObject[classId], setAttr, setAttrValue)
                models.storage.save()
                return

    def do_count(self, arg):
        """Returns the number of instances of a specific class."""
        instancesNumber = 0
        myObject = models.storage.all()

        if arg in systemClasses:
            for key in myObject.keys():
                classId = key.split(".")
                if classId[0] == arg:
                    instancesNumber += 1
            print(instancesNumber)
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
