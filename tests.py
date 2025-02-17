import unittest
from check_pwd import check_pwd

class TestCheckPwd(unittest.TestCase):
    """
    Testing for empty pwd
    """
    def test1(self):
        self.assertFalse(check_pwd(""))

    """
    Testing for pwd that's too short,
    length must be 8 characters or more.
    """
    def test2(self):
        self.assertFalse(check_pwd("A1!bc"))

    """
    Testing for pwd that's too long,
    length can't be more than 20 characters.
    """
    def test3(self):
        self.assertFalse(check_pwd("A1!" + "a" * 18))

if __name__ == "__main__":
    unittest.main()
