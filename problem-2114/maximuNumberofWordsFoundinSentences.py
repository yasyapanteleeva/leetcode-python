from typing import List

def mostWordsFound(sentences: List[str]) -> int:
    """
    Поиск строки с максимальным количеством слов

    Parameters
    ----------
    sentences: List[str]
        список предложений

    Returns
    -------
    Максимальное число 
    """
    lst_len = []

    for el in sentences:
        lst_len.append(len(el.split()))

    return max(lst_len)


print(mostWordsFound(sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))