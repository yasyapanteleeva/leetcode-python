from typing import List

def getConcatenation(nums: List[int]) -> List[int]:
    """
    Создать новый список 2*len(nums)

    Parameters
    ----------
    nums: List[int]
        список операций

    Returns
    -------
    Новый список
    """
    len_nums = len(nums)
    ans = [0]*2*len_nums

    for i in range(2*len_nums):
        if i < len_nums:
            ans[i] = nums[i]
        else:
            ans[i] = nums[i-len_nums]

    return ans


print(getConcatenation(nums = [1, 3, 2, 1]))