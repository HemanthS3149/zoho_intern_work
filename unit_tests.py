import unittest
from unittest.mock import patch #for replacing objects during testing, such as funcs or class methods, with mock objects
def get_data_from_api():
    #I am assuming this function makes a real API call
    pass
def process_data():
    data=get_data_from_api()
    return data["key"] #returns the value associated with the key

#unit test class(for initializing a unit test for the process_data() func)
class TestProcessData(unittest.TestCase):
    @patch('__main__.get_data_from_api')#decorator to modify behavior of functions, it intercepts calls to 'get_data_from_api()' in the scope of __main__
    def test_process_data(self,mock_get_data):#allows us to control what 'get_data_from_api' returns without actually making a real API call
        mock_get_data.return_value={"key":"value"} # sets the return value of mocked func to dict like thing
        self.assertEqual(process_data(),"value") #checks that process_data() behaves as expected based on mocked data

if __name__=="__main__":
    unittest.main()
