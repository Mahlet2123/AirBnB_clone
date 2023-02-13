#!/usr/bin/python3
""" the entry point of the command interpreter """
import cmd
import uuid
import models
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
            line_pattern = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|\
                          (?:(\S)+)))?)?)?'
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

        # --- Advanced tasks ---
    def dict_update(self, classname, uid, s_dict):
        """updates an instance from a dictionary"""
        s = s_dict.replace("'", '"')
        d = json.loads(s)
        if not classname:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[classname]
                for attribute, value in d.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def adv_parser(self, arg):
        """Rearranges commands of syntax class.< command >()"""
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", arg)
        if not match:
            return arg
        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False
        attr_and_value = ""
        if method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""
            match_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(
                    1) or "") + " " + (match_attr_and_value.group(2) or "")
        command = method + " " + classname + " " + uid + " " + attr_and_value
        self.onecmd(command)
        return command

    def default(self, arg):
        """Redirects input to adv_parser when syntax doesn't match"""
        response = self.adv_parser(arg)
        if response == arg:
            print("*** Unknown syntax:", arg)

    def do_count(self, line):
        """Retrieves the number of instances of a class
        Usage: <class name>.count()"""
        objs = storage.all()
        args = line.split(".")
        if not args[0]:
            print("** class name missing **")
        elif args[0] not in storage.classes_dict():
            print("** class doesn't exist **")
        else:
            instances = 0
            for id in objs.keys():
                classs = id.split(".")
                if line == classs[0]:
                    instances += 1
            print(instances)

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
