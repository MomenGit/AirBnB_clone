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

    def test_create_base_model(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create BaseModel")
            output = file.getvalue()
            self.assertRegex(
                output, r'\b\w+[-?\w+]*\b')

    def test_create_user(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create User")
            output = file.getvalue()
            self.assertRegex(
                output, r'\b\w+[-?\w+]*\b')

    def test_create_city(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create City")
            output = file.getvalue()
            self.assertRegex(
                output, r'\b\w+[-?\w+]*\b')

    def test_create_place(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create Place")
            output = file.getvalue()
            self.assertRegex(
                output, r'\b\w+[-?\w+]*\b')

    def test_create_amenity(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create Amenity")
            output = file.getvalue()
            self.assertRegex(
                output, r'\b\w+[-?\w+]*\b')

    def test_create_state(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create State")
            output = file.getvalue()
            self.assertRegex(
                output, r'\b\w+[-?\w+]*\b')

    def test_create_review(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create Review")
            output = file.getvalue()
            self.assertRegex(
                output, r'\b\w+[-?\w+]*\b')

    def test_show_base_model(self):
        """Test show command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create BaseModel")
            model_id = file.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as file:
                self.console.onecmd("show BaseModel {}".format(model_id))
                output = file.getvalue().strip()
                self.assertIn(model_id, output)

    def test_show_user(self):
        """Test show command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create User")
            model_id = file.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as file:
                self.console.onecmd("show User {}".format(model_id))
                output = file.getvalue().strip()
                self.assertIn(model_id, output)

    def test_show_place(self):
        """Test show command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create Place")
            model_id = file.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as file:
                self.console.onecmd("show Place {}".format(model_id))
                output = file.getvalue().strip()
                self.assertIn(model_id, output)

    def test_show_city(self):
        """Test show command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create City")
            model_id = file.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as file:
                self.console.onecmd("show City {}".format(model_id))
                output = file.getvalue().strip()
                self.assertIn(model_id, output)

    def test_show_amenity(self):
        """Test show command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create Amenity")
            model_id = file.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as file:
                self.console.onecmd("show Amenity {}".format(model_id))
                output = file.getvalue().strip()
                self.assertIn(model_id, output)

    def test_show_state(self):
        """Test show command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create State")
            model_id = file.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as file:
                self.console.onecmd("show State {}".format(model_id))
                output = file.getvalue().strip()
                self.assertIn(model_id, output)

    def test_show_review(self):
        """Test show command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create Review")
            model_id = file.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as file:
                self.console.onecmd("show Review {}".format(model_id))
                output = file.getvalue().strip()
                self.assertIn(model_id, output)

    def test_destroy_base_model(self):
        """Test destroy command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create BaseModel")
            model_id = file.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as file:
                self.console.onecmd("destroy BaseModel {}".format(model_id))
                output = file.getvalue().strip()
                self.assertNotIn(model_id, output)

    def test_destroy_user(self):
        """Test destroy command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create User")
            model_id = file.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as file:
                self.console.onecmd("destroy User {}".format(model_id))
                output = file.getvalue().strip()
                self.assertNotIn(model_id, output)

    def test_destroy_place(self):
        """Test destroy command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create Place")
            model_id = file.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as file:
                self.console.onecmd("destroy Place {}".format(model_id))
                output = file.getvalue().strip()
                self.assertNotIn(model_id, output)

    def test_destroy_city(self):
        """Test destroy command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create City")
            model_id = file.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as file:
                self.console.onecmd("destroy City {}".format(model_id))
                output = file.getvalue().strip()
                self.assertNotIn(model_id, output)

    def test_destroy_amenity(self):
        """Test destroy command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create Amenity")
            model_id = file.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as file:
                self.console.onecmd("destroy Amenity {}".format(model_id))
                output = file.getvalue().strip()
                self.assertNotIn(model_id, output)

    def test_destroy_state(self):
        """Test destroy command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create State")
            model_id = file.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as file:
                self.console.onecmd("destroy State {}".format(model_id))
                output = file.getvalue().strip()
                self.assertNotIn(model_id, output)

    def test_destroy_review(self):
        """Test destroy command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create Review")
            model_id = file.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as file:
                self.console.onecmd("destroy Review {}".format(model_id))
                output = file.getvalue().strip()
                self.assertNotIn(model_id, output)

    def test_all_base_model(self):
        """Test all command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create BaseModel")
            model_id = file.getvalue().strip()
            with patch('sys.stdout', new=StringIO())as file:
                self.console.onecmd("all BaseModel")
                output = file.getvalue().strip()
                self.assertIn(model_id, output)

    def test_all_user(self):
        """Test all command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create User")
            model_id = file.getvalue().strip()
            with patch('sys.stdout', new=StringIO())as file:
                self.console.onecmd("all User")
                output = file.getvalue().strip()
                self.assertIn(model_id, output)

    def test_all_place(self):
        """Test all command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create Place")
            model_id = file.getvalue().strip()
            with patch('sys.stdout', new=StringIO())as file:
                self.console.onecmd("all Place")
                output = file.getvalue().strip()
                self.assertIn(model_id, output)

    def test_all_city(self):
        """Test all command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create City")
            model_id = file.getvalue().strip()
            with patch('sys.stdout', new=StringIO())as file:
                self.console.onecmd("all City")
                output = file.getvalue().strip()
                self.assertIn(model_id, output)

    def test_all_amenity(self):
        """Test all command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create Amenity")
            model_id = file.getvalue().strip()
            with patch('sys.stdout', new=StringIO())as file:
                self.console.onecmd("all Amenity")
                output = file.getvalue().strip()
                self.assertIn(model_id, output)

    def test_all_state(self):
        """Test all command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create State")
            model_id = file.getvalue().strip()
            with patch('sys.stdout', new=StringIO())as file:
                self.console.onecmd("all State")
                output = file.getvalue().strip()
                self.assertIn(model_id, output)

    def test_all_review(self):
        """Test all command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create Review")
            model_id = file.getvalue().strip()
            with patch('sys.stdout', new=StringIO())as file:
                self.console.onecmd("all Review")
                output = file.getvalue().strip()
                self.assertIn(model_id, output)

    def test_update_base_model(self):
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

    def test_update_user(self):
        """Test update command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create User")
            model_id = file.getvalue()
            with patch('sys.stdout', new=StringIO) as file:
                self.console.onecmd(
                    "update User {} name 'Betty'".format(model_id))
                with patch('sys.stdout', new=StringIO()) as file:
                    self.console.onecmd("show User {}".format(model_id))
                    output = file.getvalue().strip()
                    self.assertIn('name', output)

    def test_update_place(self):
        """Test update command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create Place")
            model_id = file.getvalue()
            with patch('sys.stdout', new=StringIO) as file:
                self.console.onecmd(
                    "update Place {} name 'Betty'".format(model_id))
                with patch('sys.stdout', new=StringIO()) as file:
                    self.console.onecmd("show Place {}".format(model_id))
                    output = file.getvalue().strip()
                    self.assertIn('name', output)

    def test_update_city(self):
        """Test update command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create City")
            model_id = file.getvalue()
            with patch('sys.stdout', new=StringIO) as file:
                self.console.onecmd(
                    "update City {} name 'Betty'".format(model_id))
                with patch('sys.stdout', new=StringIO()) as file:
                    self.console.onecmd("show City {}".format(model_id))
                    output = file.getvalue().strip()
                    self.assertIn('name', output)

    def test_update_amenity(self):
        """Test update command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create Amenity")
            model_id = file.getvalue()
            with patch('sys.stdout', new=StringIO) as file:
                self.console.onecmd(
                    "update Amenity {} name 'Betty'".format(model_id))
                with patch('sys.stdout', new=StringIO()) as file:
                    self.console.onecmd("show Amenity {}".format(model_id))
                    output = file.getvalue().strip()
                    self.assertIn('name', output)

    def test_update_state(self):
        """Test update command"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.console.onecmd("create State")
            model_id = file.getvalue()
            with patch('sys.stdout', new=StringIO) as file:
                self.console.onecmd(
                    "update State {} name 'Betty'".format(model_id))
                with patch('sys.stdout', new=StringIO()) as file:
                    self.console.onecmd("show State {}".format(model_id))
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
