import unittest
from main import get_sheet_data

class TestGoogleSheetsAPI(unittest.TestCase):

    def test_get_sheet_data(self):
        sheet_name = 'Sheet1'
        data = get_sheet_data(sheet_name)
        self.assertIsNotNone(data)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

if __name__ == '__main__':
    unittest.main()
