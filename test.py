import unittest
import pathlib as pl
import json
from jsonschema import validate

class TestCaseBase(unittest.TestCase):
    def assertIsFile(self, path):
        if not pl.Path(path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(path))

    def test_list(self):
        path = pl.Path("data/data_1.json")
        self.assertIsFile(path)

    def test_json(self):
        path = pl.Path("data/data_1.json")
        with open(path) as f:
            data = json.load(f)      
        
        self.assertEqual(type(data),dict)




if __name__ == "__main__":
    unittest.main()
