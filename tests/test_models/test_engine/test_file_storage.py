#!/usr/bin/python3
"""Unittest for FileStorage class"""
from models.engine.file_storage import FileStorage
import models
import unittest
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime


class TestFileStorageClass(unittest.TestCase):

    def test_instance_creation(self):
        """"Test that instance of filestorage is properly created"""
        Storage = FileStorage()
        self.assertTrue(type(Storage) == FileStorage)
        self.assertTrue(isinstance(Storage, FileStorage))

    def test_storage_all(self):
        """Tests method all"""
        FS = FileStorage()
        self.assertEqual(type(FS.all()), dict)

    def test_storage_new(self):
        """Test method new"""
        FS = FileStorage()
        FS.new(BaseModel())
        self.assertTrue(FS.all())

    def test_storage_save(self):
        """Test method save"""
        FS = FileStorage()
        B_M = BaseModel()
        FS.new(B_M)
        FS.save()
        with open("file.json", "r", encoding='utf-8') as r:
            Json_full = r.read()
            self.assertTrue(f"BaseModel.{B_M.id}" in Json_full)

    def test_storage_reload(self):
        """Test method reload"""
        FS = FileStorage()
        B_M = BaseModel()
        Obj_Dict = FS.all()
        B_M.save()
        FS.reload()
        Obj_Dict_save = FS.all()
        self.assertTrue(Obj_Dict == Obj_Dict_save)


if __name__ == "__main__":
    unittest.main()