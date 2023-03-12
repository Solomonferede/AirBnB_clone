#!/usr/bin/python3
""" 
the console module
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """The cmd interpretre class"""

    prompt = "(hbnb) "
    def do_prompt(self, line):
        """ Change the defult prompt"""
        self.prompt = line

    def do_EOF(self, line):
        """quit and EOF to exit the program"""
        return True

    def emptyline(self):
        """Empty line"""
        pass






if __name__ == '__main__':
    HBNBCommand().cmdloop()