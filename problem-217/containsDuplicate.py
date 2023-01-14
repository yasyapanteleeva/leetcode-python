from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    """
    Проверка на содержание дубликата в списке

    Parameters
    ----------
    nums: List[int]
        список чисел

    Returns
    -------
    Boolean
    """
    hast = set()

    for num in nums:
        if num in hast:
            return True
        else:
            hast.add(num)
            
    return False


res = containsDuplicate(nums = [1,2,3,1])
print(res)