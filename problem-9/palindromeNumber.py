def isPalindrome(x: int) -> bool:
    """
    Проверка числа на палиндром

    Parameters
    ----------
    x: int
        заданное число

    Returns
    -------
    Boolean
    """
    if x < 0:
        return False

    new_x = 0
    tmp = x

    while tmp > 0:
        digit = tmp % 10
        new_x = new_x * 10 + digit
        tmp //= 10

    return x == new_x


res = isPalindrome(123)
print(res)