from typing import List

def plusOne(digits: List[int]) -> List[int]:
    """
    Увеличение числа в списке на единицу

    Parameters
    ----------
    digits: List[int]
        целочисленный список

    Returns
    -------
    список увеличенный на единицу
    """
    number = 0

    while len(digits) > 0:
        number = number * 10 + digits[0]
        digits = digits[1:]
        
    number += 1
    
    return [int(i) for i in str(number)]


res = plusOne([9])
print(res)