from typing import List

def majorityElement(nums: List[int]) -> int:
    """
    Поиск элемента списка, встречающего n/2 раз

    Parameters
    ----------
    nums: List[int]
        список чисел

    Returns
    -------
    Элемент большинства
    """
    n = len(nums)
    amount = n // 2

    if n <= 1:
        return nums[0]

    nums.sort()

    return nums[amount]


res = majorityElement(nums = [2,2,1,1,1,2,2])
print(res)