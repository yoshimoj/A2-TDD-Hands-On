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
    Checks for at least one uppercase letter if there's no
    uppercase letter it returns False.
    """
    if not any(c.isupper() for c in password):
        return False

    """
    Checks for at least one digit, if there's no digit
    it returns False.
    """
    if not any(c.isdigit() for c in password):
        return False

    """
    Allowed symbols copied from Canvas
    """
    allowed_symbols = set("~`!@#$%^&*()_+-=")

    """
    Checks that at least one symbol from the list is present,
    if none are present it will return False.
    """
    if not any(c in allowed_symbols for c in password):
        return False

    """
    If all tests are passed, return True
    """
    return True
