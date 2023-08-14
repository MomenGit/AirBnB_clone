#!/usr/bin/python3
"""Module that contains AirBnB command interpreter"""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """Command interpreter to manage AirBnB objects using CRUD operations"""

    prompt = '(hbnb) '

    def default(self, line: str) -> None:
        new_line = self.precmd(line)
        if new_line:
            self.onecmd(new_line)
        else:
            super().default(line)

    def precmd(self, line: str) -> str:
        import re
        pattern = r"(\w+)\.(\w+)\((.*)\)"
        # match line to <class name>.<cmd>(<args>)
        match = re.match(pattern, line)

        if match:
            # converts matched into a list
            groups = list(match.groups())
            # find the parameters
            # parameters = re.findall(r"\b\w+\b", groups[2])
            parameters = re.findall(r"\b\w+[-?\w+]*\b", groups[2])
            # creates a new list by adding
            # the cmd then the class name then the parameters
            groups = [groups[1], groups[0]] + parameters
            return ' '.join(groups)
        else:
            return super().precmd(line)

    def cmdloop(self, intro=None) -> None:
        import sys
        if len(sys.argv) > 1:
            self.onecmd(' '.join(sys.argv[1:]))
        else:
            super().cmdloop(intro)

    def do_quit(self, arg):
        """Quit command to exit the program"""

        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""

        print()
        return True

    def do_create(self, obj_type):
        """Creates a new instance of the obj_type"""

        if not obj_type:
            print("** class name missing **")
        elif obj_type not in map(lambda val: val.__name__,
                                 models.dispatch_dict().values()):
            print("** class doesn't exist **")
        else:
            model = models.dispatch_dict()[obj_type]()
            model.save()
            print(model.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """

        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in map(lambda val: val.__name__,
                                models.dispatch_dict().values()):
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj = models.storage.all().get("{}.{}".format(args[0], args[1]))
            if obj:
                print(obj)
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""

        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in map(lambda val: val.__name__,
                                models.dispatch_dict().values()):
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            obj = models.storage.all().get(key)
            if obj:
                models.storage.all().pop(key)
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of
        all instances based or not on the class name.
        """
        if not arg:
            print([str(value) for value in models.storage.all().values()])
        else:
            if arg not in models.dispatch_dict().keys():
                print("** class doesn't exist **")
            else:
                print([str(obj) for obj in models.storage.all().values()
                       if obj.__class__.__name__ == arg])

    def do_update(self, args):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file)
        """
        import shlex
        from datetime import datetime

        args = shlex.split(args)  # arg.split(' ', 3)
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            class_name = args[0]
            obj_id = args[1]
            if (class_name not in models.dispatch_dict().keys()):
                print("** class doesn't exist **")
                return
            obj = models.storage.all().get("{}.{}"
                                           .format(class_name, obj_id))
            attr_name = args[2]
            attr_value = args[3]

            if obj:
                i = 2
                while (i + 1 < len(args)):
                    attr_name = args[i]
                    attr_value = args[i + 1]
                    if (hasattr(obj, attr_name)):
                        attr_type = type(getattr(obj, attr_name))
                        obj.__dict__[attr_name] = attr_type(attr_value)
                    else:
                        obj.__dict__[attr_name] = attr_value
                    models.storage.save()
                    i += 2
            else:
                print("** no instance found **")

    def do_count(self, arg):
        """Retrieve the number of instances of a class"""

        obj_count = 0
        for obj in models.storage.all().values():
            if (arg == obj.__class__.__name__):
                obj_count += 1
        print(obj_count)

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
