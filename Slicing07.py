def main(a,n):
    """
    The s string variable is given. return all characters except n characters at the end.
    Args:
        s(str): parameter
        n(int): parameter
    Returns:
        str: answer
    """
    return a[0:len(a)-n]
print(main("codeschooluz",3))