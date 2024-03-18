#!/usr/bin/python3
"""Defines the HBnB console."""
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models import storage
import cmd
import models



class HBNBCommand(cmd.Cmd):
    """
    HBNB command interpreter class.
    This class provides an interactive command interpreter.
    """
    prompt = "(hbnb) "
    List_classes = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]

    '''def __init__(self):
        super().__init__()
        self.List_classes = ["BaseModel", "User"]'''
        
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
        elif argl[0] not in self.List_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(argl[0])()
            storage.new(new_instance)
            storage.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        argl = arg.split()
        if not argl:
            print("** class name missing **")
            return

        class_name = argl[0]
        if class_name not in self.List_classes:
            print("** class doesn't exist **")
            return

        if len(argl) < 2:
            print("** instance id missing **")
            return

        key = class_name + '.' + argl[1]
        objects = models.storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        print(objects[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        argl = arg.split()
        if len(argl) < 2:
            print("** instance id missing **")
            return
        class_name = argl[0]
        instance_id = argl[1]
        objects = models.storage.all()

        key_to_delete = "{}.{}".format(class_name, instance_id)
        if key_to_delete not in objects:
            print("** no instance found **")
            return

        del objects[key_to_delete]
        models.storage.save()

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

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        argl = line.split()
        if len(argl) < 1:
            print("** class name missing **")
            return
        class_name = argl[0]
        if class_name not in self.List_classes:
            print("** class doesn't exist **")
            return
        if len(argl) < 2:
            print("** instance id missing **")
            return
        instance_id = argl[1]
        key = class_name + '.' + instance_id
        objects = models.storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        instance = objects[key]
        if len(argl) < 3:
            print("** attribute name missing **")
            return
        if len(argl) < 4:
            print("** value missing **")
            return
        attribute_name = argl[2]
        value = argl[3]
        if not hasattr(instance, attribute_name):
            print("** attribute doesn't exist **")
            return
        # Asigna el nuevo valor al atributo
        setattr(instance, attribute_name, value)
        models.storage.save()
        print("Instance updated successfully!")
            
if __name__ == '__main__':
    HBNBCommand().cmdloop()            