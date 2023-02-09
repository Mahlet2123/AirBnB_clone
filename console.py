#!/usr/bin/python3
""" the entry point of the command interpreter """
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """the HBNBCommand class"""

    prompt = "(hbnb)"

    def do_create(self, line):
        """Creates a new instance of BaseModel
        saves it (to the JSON file) and
        prints the id"""
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes_dict():
            print("** class doesn't exist **")
        else:
            base1 = storage.classes_dict()[line]()
            base1.save()
            print(base1.id)

    def do_show(self, line):
        """ Prints the string representation of
        an instance based on the class name and id """

        if line == "" or line is None:
            print("** class name missing **")
        else:
            class_atr = line.split(" ")
            if class_atr[0] not in storage.classes_dict():
                print("** class doesn't exist **")
            elif len(class_atr) == 1:
                print("** instance id missing **")
            else:
                key = f"{class_atr[0]}.{class_atr[1]}"
                all_objs = storage.all()
                for k in all_objs.keys():
                    if k == key:
                        obj = all_objs[key]
                        print (obj)
                        return
                print("** no instance found **")

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id
        (save the change into the JSON file) """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            class_atr = line.split(" ")
            if class_atr[0] not in storage.classes_dict():
                print("** class doesn't exist **")
            elif len(class_atr) == 1:
                print("** instance id missing **")
            else:
                key = f"{class_atr[0]}.{class_atr[1]}"
                all_objs = storage.all()
                for k in all_objs.keys():
                    if k == key:
                        obj = all_objs[key]
                        del storage.all()[key]
                        obj.save()
                        return
                print("** no instance found **")

    def do_all(self, line):
        """ Prints all string representation of all instances
        based or not on the class name. """

        list = []
        all_objs = storage.all()

        if line != "" and line is not None:
            arg = line.split(" ")
            if arg[0] not in storage.classes_dict():
                print("** class doesn't exist **")
            else:
                for key in all_objs.keys():
                    if all_objs[key].__class__.__name__ == arg[0]:
                        obj = all_objs[key]
                        list.append(obj.__str__())
        else:
            for key in all_objs.keys():
                obj = all_objs[key]
                list.append(obj.__str__())
        if len(list) > 0:
            print (list)

    def do_update(self, line):
        """ Updates an instance based on the class name and id
        by adding or updating attribute (save the change into
        the JSON file). """


    def emptyline(self):
        """empty line is entered in response to the prompt"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, line):
        """Hit ctrl+D (EOF) to exit the program"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
