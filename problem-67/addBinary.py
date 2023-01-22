def addBinary(a: str, b: str) -> str:
    """
    Найти двоичную сумму строк

    Parameters
    ----------
    a, b: str
        заданные двоичные строки

    Returns
    -------
    Сумма двоичная
    """
    num_a, num_b = int(a, 2), int(b, 2)

    return bin(num_a + num_b).replace("0b", "")


print(addBinary(a = "11", b = "1"))