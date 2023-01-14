def isPerfectSquare(num: int) -> bool:
    """
    Проверка на существование квадратного корня числа

    Parameters
    ----------
    num: int
        число для проверки

    Returns
    -------
    Boolean
    """
    if num <= 1:
        return True

    left = 2
    right = num

    while left <= right:
        mid = (left + right) // 2
        square = mid * mid

        if square == num:
            return True
        elif square > num:
            right = mid - 1
        else:
            left = mid + 1
            
    return False


res = isPerfectSquare(16)
print(res)