import unittest
from check_pwd import check_pwd

class TestCheckPwd(unittest.TestCase):
    def test_empty_string(self):
        self.assertFalse(check_pwd(""))

if __name__ == "__main__":
    unittest.main()