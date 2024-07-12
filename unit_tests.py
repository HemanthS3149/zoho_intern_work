import unittest
from unittest.mock import patch
def get_data_from_api():
    #assuming this function makes a real API call
    pass
def process_data():
    data=get_data_from_api()
    return data["key"]

class TestProcessData(unittest.TestCase):
    @patch('__main__.get_data_from_api')
    def test_process_data(self,mock_get_data):
        mock_get_data.return_value={"key":"value"}
        self.assertEqual(process_data(),"value")

if __name__=="__main__":
    unittest.main()