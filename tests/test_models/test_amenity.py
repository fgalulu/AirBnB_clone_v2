#!/usr/bin/python3
"""Test amenity model"""
from tests.test_models.test_base_model import TestBaseModel
from models.amenity import Amenity


class test_Amenity(TestBaseModel):
    """Test amenity model """

    def __init__(self, *args, **kwargs):
        """initialization test"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """name test"""
        new = self.value()
        self.assertEqual(type(new.name), str)
