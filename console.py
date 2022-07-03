#!/usr/bin/python3
"""
Console Module
"""
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """
    Class Console
    """

    HBNC_systemClasses = ['BaseModel', 'User', 'State',
                          'City', 'Amenity', 'Place', 'Review']

    if sys.stdin and sys.stdin.isatty():
        prompt = '(hbnb) '
    else:
        prompt = '(hbnb)\n'

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
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in self.HBNC_systemClasses:
            print("** class doesn't exist **")
            return
        else:
            myObject = eval(args[0] + '()')
            myObject.save()
            print(myObject.id)
            return

    def do_show(self, arg):
        """Prints the string representation of \
an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in self.HBNC_systemClasses:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        else:
            myObject = "{}.{}".format(args[0], args[1])
            try:
                print("[{}] ({}) {}".format(args[0], myObject[1],
                                            storage.all()[myObject]))
            except Exception:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class \
name and id (save the change into the JSON file)."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in self.HBNC_systemClasses:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        else:
            key = args[0] + "." + args[1]
            try:
                del storage.all()[key]
                storage.save()
            except Exception:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all \
instances based or not on the class name."""
        myObject = storage.all()
        res = []
        if not arg:
            for key, value in myObject.items():
                res.append(str(value))
            if len(res) != 0:
                print(res)
            return
        args = arg.split()
        if args[0] not in self.HBNC_systemClasses:
            print("** class doesn't exist **")
            return
        for key, value in myObject.items():
            if args[0] == str(key.split('.')[0]):
                res.append(str(value))
        if len(res) != 0:
            print(res)
        return

    def do_update(self, arg):
        """Updates an instance based on the class name \
and id by adding or updating attribute (save \
the change into the JSON file)."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.HBNC_systemClasses and len(args) >= 1:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing  **")
            return
        if len(args) == 2:
            print("** attribute name missing  **")
            return
        if len(args) == 3:
            print("** value missing  **")
            return
        if len(args) == 4:
            classId = args[0] + "." + args[1]
            myObject = storage.all()
            if classId not in myObject:
                print("** no instance found **")
                return
            else:
                setAttr = args[2]
                setAttrValue = args[3].strip('"')
                setattr(myObject[classId], setAttr, setAttrValue)
                storage.save()
                return

    def precmd(self, arg):
        """Parser for inputs of the kind <ClassName>.command\n"""
        if arg and ('(' and ')' and '.' in arg):
            args = arg.split('.', 1)
            if args[1] != '':
                mod_class = args[0]
                args = args[1].split('(', 1)
                if args[1] != '':
                    cmnd = args[0]
                    args = args[1].split(')', 1)
                    if args[1] == '':
                        args = args[0].split(',')
                        id = args[0].strip('"')
                        attr_name = ''
                        attr_value = ''
                        if len(args) == 3:
                            attr_name = args[1].strip('"')
                            attr_value = args[2]
                        line = (cmnd + ' ' + mod_class + ' '
                                + id + ' ' + attr_name + ' ' + attr_value)
                        try:
                            return line
                        except Exception:
                            return arg
                    else:
                        return arg
                else:
                    return arg
            else:
                return arg
        else:
            return arg

    def do_count(self, arg):
        """Retrieves the number of instances of a class"""
        instancesNumber = 0
        myObject = models.storage.all()

        if not arg:
            for key in myObject.keys():
                instancesNumber += 1

        else:
            if arg in self.systemClasses:
                for key in myObject.keys():
                    classId = key.split(".")
                    if classId[0] == arg:
                        instancesNumber += 1
            else:
                print("** class doesn't exist **")
                return

        print(instancesNumber)
        return

    def do_stats(self, arg):
        """Returns an object with the number of instances for each class"""
        myObject = models.storage.all()
        myStats = {}
        if not arg:
            for key in myObject.keys():
                classId = key.split(".")
                if classId[0] not in myStats:
                    myStats.update({"{}".format(classId[0]): 1})
                else:
                    myStats[classId[0]] += 1
            print(myStats)
            return
        else:
            print("** no args allowed for this method **")
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
