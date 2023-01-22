def lengthOfLastWord(s: str) -> int:
    """
    Найти длину последнего слова в строке

    Parameters
    ----------
    s: str
        заданная строка

    Returns
    -------
    Длина слова
    """
    return len(s.split()[-1])


print(lengthOfLastWord("   fly me   to   the moon  "))