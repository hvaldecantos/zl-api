import unittest
from zlapi import create_app
from zlapi.database.db import db


test_config = {"SECRET_KEY": 'test',
               "TESTING": True,
               "MONGODB_DB": 'zlapi-test',
               "MONGODB_HOST": '127.0.0.1',
               "MONGODB_PORT": 27017}

class BaseCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(test_config).test_client()
        self.db = db.get_db()
    
    def tearDown(self):
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)
