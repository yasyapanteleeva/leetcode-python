from typing import List

def differenceOfSum(nums: List[int]) -> int:
    """
    Найти абсолютную разницу между суммой списка и суммой цифр

    Parameters
    ----------
    nums: List[int]
        список положительных целых чисел

    Returns
    -------
    Разница между суммами чисел и цифр списка
    """
    sum_el = 0
    sum_digit = 0

    for num in nums:
        sum_el += num
        if num < 10:
            sum_digit += num  
        else:
            while num > 0:
                sum_digit += num % 10
                num //= 10

    return abs(sum_el - sum_digit)


print(differenceOfSum(nums = [1,15,6,3]))