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

    """
    Testing for pwd with missing lowercase letter,
    it should be rejected if there's no lowercase letter.
    """
    def test4(self):
        self.assertFalse(check_pwd("ABC123!@#"))

    """"
    Testing for pwd with missing uppercase letter,
    it should be rejected if there's no uppercase letter.
    """
    def test5(self):
        self.assertFalse(check_pwd("abc123!@#"))

    """
    Testing for pwd with missing digit,
    it should be rejected if there's no digits.
    """
    def test6(self):
        self.assertFalse(check_pwd("Abc!@#xyz"))

if __name__ == "__main__":
    unittest.main()
