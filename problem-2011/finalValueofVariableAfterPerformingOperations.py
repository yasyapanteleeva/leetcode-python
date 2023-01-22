from typing import List

def finalValueAfterOperations(operations: List[str]) -> int:
    """
    Найти значение, после применения операций

    Parameters
    ----------
    operations: List[str]
        список операций

    Returns
    -------
    Значение, после выполненых опереций
    """
    dict_operations = {
        '++X': 1,
        'X++': 1,
        '--X': -1,
        'X--': -1
    }
    x = 0

    for op in operations:
        x += dict_operations[op]

    return x


print(finalValueAfterOperations(operations = ["--X","X++","X++"]))