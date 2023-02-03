from typing import List

def buildArray(nums: List[int]) -> List[int]:
    """
    Получить новый список из перестановок 
    nums[i] = nums[nums[i]]

    Parameters
    ----------
    nums: List[int]
        список чисел

    Returns
    -------
    Новый список
    """
    return [nums[nums[i]] for i in range(len(nums))]


print(buildArray(nums = [5,0,1,2,3,4]))