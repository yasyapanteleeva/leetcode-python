def mySqrt(x: int) -> int:
    """
    Поиск квадртного корня

    Parameters
    ----------
    x: int
        неотрицательное целое число

    Returns
    -------
    Квадратный корень
    """
    if x <= 1:
        return x
    
    left = 2
    right = x

    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid > x:
            right = mid - 1
        else:
            left = mid + 1
            
    return right


res = mySqrt(25)
print(res)