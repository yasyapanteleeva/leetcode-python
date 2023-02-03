from typing import List

def numIdenticalPairs(nums: List[int]) -> int:
    """
    Найти хорошие пары nums[i] = nums[j], i < j

    Parameters
    ----------
    nums: List[int]
        целочисленный список

    Returns
    -------
    Количество хороших пар
    """
    amount = 0

    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[i] == nums[j] and i < j:
                amount += 1

    return amount


print(numIdenticalPairs(nums = [1, 2, 3, 1, 1, 3]))
print(numIdenticalPairs(nums = [1, 1, 1, 1]))