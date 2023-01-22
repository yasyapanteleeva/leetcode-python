def defangIPaddr(address: str) -> str:
    """
    Вернуть защищенный IP-адрес . -> [.]

    Parameters
    ----------
    address: str
        заданный IP-адрес

    Returns
    -------
    Защищенный IP
    """

    return '[.]'.join(address.split('.'))


print(defangIPaddr(address = "1.1.1.1"))