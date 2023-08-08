#!/usr/bin/python3
import cmd
from typing import Any
"""Module that contains AirBnB command interpreter"""


class HBNBCommand(cmd.Cmd):
    """Command interpreter to manage AirBnB objects
    using CRUD operations
    """

    prompt = '(hbnb) '

    def cmdloop(self, intro: Any | None = None) -> None:
        import sys
        if len(sys.argv) > 1:
            self.onecmd(' '.join(sys.argv[1:]))
        else:
            super().cmdloop(intro)

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program
        """
        print()
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
