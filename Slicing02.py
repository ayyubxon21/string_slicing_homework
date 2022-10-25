def main(s):
    """
    The s string variable is given. return four characters from the end.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    return s[len(s)-4:len(s)]
print(main("pyhton"))