from typing import List

def restoreString(s: str, indices: List[int]) -> str:
    """
    Поиск перетасованной строки

    Parameters
    ----------
    s: str
        заданная строка
    indices: List[int]
        список целочисленных значений

    Returns
    -------
    Перетасованная строка
    """
    d = {indices[i]: s[i] for i in range(len(indices))}
    new_s = ''

    for idx in range(len(indices)):
        new_s += d[idx]

    return new_s


print(restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3]))
