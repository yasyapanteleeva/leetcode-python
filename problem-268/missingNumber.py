from typing import List

def missingNumber(nums: List[int]) -> int:
    """
    Поиск элемента, отсутствующего в списке [0, n]

    Parameters
    ----------
    nums: List[int]
        список чисел

    Returns
    -------
    Отсутствующий элемент
    """
    amount = len(nums)
    total = (amount * (amount + 1)) // 2

    for num in nums:
        total -= num
    
    return total


res = missingNumber(nums = [3,0,1])
print(res)