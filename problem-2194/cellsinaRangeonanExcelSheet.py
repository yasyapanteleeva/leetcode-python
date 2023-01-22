from typing import List

def cellsInRange(s: str) -> List[str]:
    """
    Найти список ячеек (x, y) r1 <= x <= r2 и c1 <= y <= c2

    Parameters
    ----------
    s: str
        заданная строка в формате "<col1><row1>:<col2><row2>"

    Returns
    -------
    Список ячеек
    """
    lst = []

    for row in range(ord(s[0]), ord(s[3])+1):
        for col in range(int(s[1]), int(s[-1])+1):
            lst.append(f'{chr(row)}{col}')

    return lst


print(cellsInRange(s = "K1:L2"))
print(cellsInRange(s = "A1:F1"))