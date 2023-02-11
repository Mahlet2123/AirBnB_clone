#!/usr/bin/python3
""" the entry point of the command interpreter """
import cmd
import uuid
from models.base_model import BaseModel
from models import storage
import re


class HBNBCommand(cmd.Cmd):
    """the HBNBCommand class"""

    prompt = "(hbnb)"

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes_dict():
            print("** class doesn't exist **")
        else:
            base1 = storage.classes_dict()[line]()
            base1.save()
            print(base1.id)

    def do_show(self, line):
        """Prints the string representation of an instance"""

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
                        print(obj)
                        return
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
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
        """Prints all string representation of all instances"""

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
            print(list)

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            line_pattern = (r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|\
                          (?:(\S)+)))?)?)?')
            m = re.search(line_pattern, line)
            class_name = m.group(1)
            class_id = m.group(2)
            attribute = m.group(3)
            value = m.group(4)

            if class_name not in storage.classes_dict():
                print("** class doesn't exist **")
            elif class_id is None:
                print("** instance id missing **")
            else:
                key = f"{class_name}.{class_id}"
                all_objs = storage.all()
                for k in all_objs.keys():
                    if k == key:
                        if attribute is None:
                            print("** attribute name missing **")
                            return
                        elif value is None:
                            print("** value missing **")
                            return
                        else:
                            cast = None
                            if not re.search('^".*"$', value):
                                if "." in value:
                                    cast = float
                                else:
                                    cast = int
                            else:
                                value = value.replace('"', "")
                            """attributes = storage.attr_dict()[classname]
                            if attribute in attributes:
                                value = attributes[attribute](value)"""
                            if cast:
                                try:
                                    value = cast(value)
                                except ValueError:
                                    pass
                            setattr(all_objs[key], attribute, value)
                            all_objs[key].save()
                            return
                print("** no instance found **")

    def emptyline(self):
        """empty line is entered in response to the prompt"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Hit ctrl+D (EOF) to exit the program"""
        print()
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
