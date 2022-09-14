#!/usr/bin/python3
"""
Contains the class TestConsoleDocs
"""
import unittest
import console
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Testing documentation of the console"""
    def test_console_docstring(self):
        """Test docstring"""
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")
