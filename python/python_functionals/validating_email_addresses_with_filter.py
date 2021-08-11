"""Hackerrank Problem: https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem"""


def fun(s):
    """Determine if the passed in email address is valid based on the following rules:

    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores [a-z], [A-Z], [0-9], [_-].
    The website name can only have letters and digits [a-z][A-Z][0-9]
    The extension can only contain letters [a-z][A-Z].
    The maximum length of the extension is 3.

    Args:
        s (str): Email address to check

    Returns:
        (bool): Whether email is valid or not
    """
    if s.count("@") == 1:
        if s.count(".") == 1:
            user, domain = s.split("@")
            website, extension = domain.split(".")
            if user.replace("-", "").replace("_", "").isalnum():
                if website.isalnum():
                    if extension.isalnum():
                        if len(extension) <= 3:
                            return True
    return False


if __name__ == "__main__":
    test = "itsallcrap"
    print(fun(test))
