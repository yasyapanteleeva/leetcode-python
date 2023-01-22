def numJewelsInStones(jewels: str, stones: str) -> int:
    """
    Поиск количества драгоценных камней

    Parameters
    ----------
    jewels: str
        строка драгоценных камней
    stones: str
        строка заданных камней

    Returns
    -------
    Количество драгоценных камней из заданных
    """
    dict_char = {ch: 1 for ch in jewels}
    amount = 0

    for item in stones:
        if item in dict_char:
            amount += 1

    return amount


print(numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))