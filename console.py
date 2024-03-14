#!/usr/bin/python3
"""Defines the HBnB console."""
from models.base_model import BaseModel
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """
    HBNB command interpreter class.
    This class provides an interactive command interpreter.
    """
    prompt = "(hbnb) "

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

    def do_create(self, line):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        argl = line.split()
        if not argl:
            print("** class name missing **")
        elif argl[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            new_instance = eval(argl[0])()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return
        argl = arg.split()
        if len(argl) == 0:
            print("** class name missing **")
            return
        class_name = argl[0]
        try:
            instance_id = argl[1]
        except IndexError:
            print("** instance id missing **")
            return
        
        key = class_name + '.' + instance_id
        objects = models.storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        
        instance = objects[key]
        print(instance)


    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        argl = arg.split()
        if len(argl) == 0:
            print("** class name missing **")
            return
        class_name = argl[0]
        try:
            instance_class = eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return
        objects = models.storage.all()
        found_instance = False
        for key, obj in objects.items():
            if isinstance(obj, instance_class) and obj.id == argl[1]:
                del objects[key]
                models.storage.save()
                found_instance = True
                break
        if not found_instance:
            print("** no instance found **")


    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if not arg:
            print([str(obj) for obj in models.storage.all().values()])
            return
        argl = arg.split()
        if len(argl) == 0:
            print("** class name missing **")
            return
        class_name = argl[0]
        try:
            instances = [str(obj) for obj in models.storage.all().values() if isinstance(obj, eval(class_name))]
            print(instances)
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        argl = arg.split()
        if len(argl) == 0:
            print("** class name missing **")
            return
        class_name = argl[0]
        try:
            instance_class = eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return
        objects = models.storage.all()
        instance_id = None
        for obj_id in objects:
            if isinstance(objects[obj_id], instance_class):
                instance_id = obj_id
                break
        if instance_id is None:
            print("** no instance found **")
            return
        if len(argl) < 2:
            print("** instance id missing **")
            return
        instance_id = argl[1]
        key = class_name + '.' + instance_id
        if key not in objects:
            print("** no instance found **")
            return
        if len(argl) < 3:
            print("** attribute name missing **")
            return
        if len(argl) < 4:
            print("** value missing **")
            return
        setattr(objects[key], argl[2], argl[3])
        models.storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
