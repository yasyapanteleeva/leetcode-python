def findTheDifference(s: str, t: str) -> str:
    """
    Поиск различия в буквах между строками

    Parameters
    ----------
    s, t: str
        заданные строки

    Returns
    -------
    Различия в строках
    """
    if len(t) == 1:
        return t

    return findTheDifference(s[:-1], t.replace(s[-1], "", 1))


res = findTheDifference(s = "abcd", t = "abdec")
print(res)