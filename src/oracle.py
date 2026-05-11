from typing import List


def oracle_linear_search(v: List[int], key: int) -> int:
    """
    Oracol independent pentru linear_search.

    Nu apelează funcția testată. Folosește propria căutare liniară.
    Pentru liste cu lungime diferită de 5 ridică ValueError, pentru a păstra
    aceeași specificație externă ca implementarea testată.
    """
    if len(v) != 5:
        raise ValueError("Lista trebuie să aibă exact 5 elemente.")

    idx = 0
    while idx < len(v):
        if v[idx] == key:
            return idx
        idx += 1

    return -1
