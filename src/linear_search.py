from typing import List


def linear_search(v: List[int], key: int) -> int:
    """
    Funcția primește o listă de exact 5 numere întregi și o cheie întreagă.
    Returnează indicele primei apariții a lui key sau -1 dacă elementul
    nu se află în listă.
    Dacă lungimea listei este diferită de 5, ridică ValueError.
    """
    if len(v) != 5:
        raise ValueError("Lista trebuie să aibă exact 5 elemente.")

    for i, element in enumerate(v):
        if element == key:
            return i

    return -1
