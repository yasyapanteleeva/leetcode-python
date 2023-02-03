from typing import List

def shuffle(nums: List[int], n: int) -> List[int]:
    """
    Найти целочисленный список 
    [x1, x2, y1, y1] -> [x1, y1, x2, y2]

    Parameters
    ----------
    operations: List[int]
        целочисленный список
    n: int
        разделитель


    Returns
    -------
    Список 
    """
    ans = []
        
    for i in range(n):
        ans.append(nums[i])
        ans.append(nums[n+i])
    
    return ans

print(shuffle(nums = [2, 5, 1, 3, 4, 7], n = 3))