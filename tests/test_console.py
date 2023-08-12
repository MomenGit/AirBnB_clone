#!/usr/bin/python3
"""Console Unit Test Module"""
from io import StringIO
import unittest
from unittest.mock import patch
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Console Unit Test Case"""

    def setUp(self) -> None:
        self.console = HBNBCommand()
        return super().setUp()

    def test_help(self):
        """Test help command"""
        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("help")
            output = file.getvalue().strip()
            self.assertIn("Documented commands (type help <topic>):", output)

    def test_quit(self):
        """Test quit cmd"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.assertTrue(self.console.onecmd("quit"))

    def test_EOF_command(self):
        """Test EOF cmd"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.assertTrue(self.console.onecmd("EOF"))

    def test_create(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create BaseModel")
            output = file.getvalue()
            self.assertRegex(
                output, r'\b\w+[-?\w+]*\b')

    def test_show(self):
        """Test show command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create BaseModel")
            model_id = file.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as file:
                self.console.onecmd("show BaseModel {}".format(model_id))
                output = file.getvalue().strip()
                self.assertIn(model_id, output)

    def test_destroy(self):
        """Test destroy command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create BaseModel")
            model_id = file.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as file:
                self.console.onecmd("destroy {}".format(model_id))
                output = file.getvalue().strip()
                self.assertNotIn(model_id, output)

    def test_all(self):
        """Test all command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create BaseModel")
            model_id = file.getvalue().strip()
            with patch('sys.stdout', new=StringIO())as file:
                self.console.onecmd("all BaseModel")
                output = file.getvalue().strip()
                self.assertIn(model_id, output)

    def test_update(self):
        """Test update command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create BaseModel")
            model_id = file.getvalue()
            with patch('sys.stdout', new=StringIO) as file:
                self.console.onecmd(
                    "update BaseModel {} name 'Betty'".format(model_id))
                with patch('sys.stdout', new=StringIO()) as file:
                    self.console.onecmd("show BaseModel {}".format(model_id))
                    output = file.getvalue().strip()
                    self.assertIn('name', output)

    def test_count(self):
        """Test count command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("count")
            output = file.getvalue().strip()
            self.assertEqual('0', output)


if __name__ == "__main__":
    unittest.main()
