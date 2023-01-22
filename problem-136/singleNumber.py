from typing import List

def singleNumber(nums: List[int]) -> int:
    """
    Найти единичный элемент массива

    Parameters
    ----------
    nums: List[int]
        заданные строки

    Returns
    -------
    Единичный элемент
    """
    if len(nums) == 1:
        return nums[0]

    if nums[0] in nums[1:]:
        elem = nums[0]
        nums = nums[1:]
        nums.remove(elem)
        return singleNumber(nums)
    else:
        return nums[0]


print(singleNumber(nums = [4,1,2,1,2]))