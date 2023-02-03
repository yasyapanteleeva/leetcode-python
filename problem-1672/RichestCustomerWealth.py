from typing import List

def maximumWealth(accounts: List[List[int]]) -> int:
    """
    Найти значение, после применения операций

    Parameters
    ----------
    accounts: List[List[int]]
        целочисленный список

    Returns
    -------
    Сумму максимального списка
    """
    
    return max([sum(accounts[i]) for i in range(len(accounts))])


print(maximumWealth([[1,5],[7,3],[3,5]]))