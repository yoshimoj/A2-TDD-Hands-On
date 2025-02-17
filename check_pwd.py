def check_pwd(password: str) -> bool:
    """
    Checks for correct password length
    (8-20 characters)
    """
    if not (8 <= len(password) <=20):
        return False

    """"
    Checks that there's at least one lowercase letter
    """
    if not any(c.islower() for c in password):
        return False

    """
    If all tests are passed, return True
    """
    return True
