#!/usr/bin/python3
"""
======================================================
Module with the entry point of the command interpreter
======================================================
"""
import cmd
import shlex
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models import storage


class HBNBCommand(cmd.Cmd):
    """command interpreter class"""

    # intro = 'Welcome the Airbnb console'
    prompt = '(hbnb) '
    classes = ["BaseModel", "User", "Place",  # List of classes we might need
               "State", "City", "Amenity", "Review"]

    def do_quit(self, arg):
        """method for close and exit from the console"""

        return True

    def do_EOF(self, arg):
        """method for exit from the console"""
        print()
        exit()



if __name__ == '__main__':
    HBNBCommand().cmdloop()
