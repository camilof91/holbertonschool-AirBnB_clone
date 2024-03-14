#!/usr/bin/python3
import cmd
"""
Defines the HBnB console.
Attributes
cmd
"""


class HBNBCommand(cmd.Cmd):
    """
    HBNB command interpreter class.
    This class provides an interactive command interpreter.
    """
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program when Ctrl + D is pressed"""
        print("")
        return True

    def do_help(self, arg):
        """Show help"""
        if arg == "quit":
            print("Quit command to exit the program")
        else:
            cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
