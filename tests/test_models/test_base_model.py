#!/usr/bin/python3
"""
Instantiating BaseModel.
"""
import unittest
from models.base_model import BaseModel
import pycodestyle


class TestBaseModel(unittest.TestCase):
    """
    Starting Test.
    """
    @classmethod
    def setUpClass(cls):
        """
        Init testing enviroment
        """
        print('\n****************** Init Testing ******************\n')
        ...

    def test_split(self):
        str_g = 'Cristian Granada'
        self.assertEqual(str_g.split(), ['Cristian', 'Granada'])

    def test_is_an_instance(self):
        """
        Instantiating BaseModels
        """
        my_BaseModel = BaseModel()
        self.assertIsInstance(my_BaseModel, BaseModel)

    def test_attributes(self):
        """
        Check if the class had corrects attributes
        """
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_id(self):
        """
        Check if the class had unique id's
        """
        my_BaseModel = BaseModel().id
        my_1BaseModel = BaseModel().id
        self.assertNotEqual(my_BaseModel, my_1BaseModel)

    def test_save(self):
        """
        Check if the class save the update the date
        """
        my_BaseModel = BaseModel()
        my_1BaseModel = my_BaseModel.updated_at
        my_BaseModel.save()
        my_2BaseModel = my_BaseModel.updated_at
        self.assertNotEqual(my_1BaseModel, my_2BaseModel)

    def test_to_dict(self):
        """

        """

    def test_style(self):
        """
        Check if the file had correct style
        """
        pstyle = pycodestyle.StyleGuide(quiet=True)
        result = pstyle.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    @classmethod
    def tearDownClass(cls):
        """
        Clear testing enviroment
        """
        print('\n****************** Finish Testing ******************\n')
        ...


if __name__ == '__main__':
    unittest.main()