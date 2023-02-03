from typing import List

def runningSum(nums: List[int]) -> List[int]:
    """
    Найти накопительную сумму sum = (nums[0], nums[i])

    Parameters
    ----------
    nums: List[int]
        список операций

    Returns
    -------
    Список элементов
    """
    
    return [sum(nums[:i+1]) for i in range(len(nums))]


print(runningSum(nums = [1,2,3,4]))