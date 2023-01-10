from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    """
    Поиск позиции заданного числа в отсортированном списке

    Parameters
    ----------
    nums: List[int]
        отсортированный целочисленный список
    target: int
        число, для поиска его позиции

    Returns
    -------
    Позиция target
    """
    low = 0
    high = len(nums) - 1
    
    while low <= high:
        mid = (low + high) // 2
        value = nums[mid]
        
        if value == target:
            return mid
        if value > target:
            high = mid - 1
        else:
            low = mid + 1

    if nums[mid] > target:
        return mid
    else:
        return mid + 1


res = searchInsert(nums = [1,3,5,6], target = 5)
print(res)