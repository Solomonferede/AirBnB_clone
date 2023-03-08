#!/usr/bin/python3
"""
test_base_model module

Contains the test case for the base_model python module
"""


from models.base_model import BaseModel
import unittest
import datetime


class TestBaseModelMethods(unittest.TestCase):
    """Testing the BaseModel methods"""


    def test_base_model(self):
        """test the base model"""
        my_model = BaseModel()
        self.assertIs(type(my_model.id), str)
        self.assertIs(type(my_model.created_at), datetime.datetime)
        self.assertIs(type(my_model.updated_at), datetime.datetime)
        self.assertEqual(my_model.updated_at, my_model.created_at)

    def test_save(self):
        """test the save method"""
        my_model2 = BaseModel()
        my_model2.name = "solomon"
        my_model2.number = 89
        my_model2.save()
        self.assertIsNot(my_model2.created_at, my_model2.updated_at)
        #self.assertEqual(my_model.save, second)




if __name__ == '__main__':
    unittest.main()