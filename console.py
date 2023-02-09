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
                for k in storage.all().keys():
                    if k == key:
                        print (storage.classes_dict()[class_atr[0]]())
                        return
                print("** no instance found **")

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id
        (save the change into the JSON file) """


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
