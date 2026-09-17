#!/usr/bin/env python3
"""
Règles et contraintes Moulinette
Fonctions autorisées : Aucune. Utilisez uniquement les fonctions autorisées pour éviter un zéro le jour de l’examen.
Énoncé

Écris une fonction qui vérifie si la chaîne 'small' est une sous-suite (subsequence) de 'big'. Une sous-suite signifie que tous les caractères de 'small' apparaissent dans 'big' dans le même ordre, mais pas nécessairement de manière consécutive. La fonction est sensible à la casse.

Signature de la fonction

def hidenp(small: str, big: str) -> bool:

Exemples:

Entrée
hidenp("abc", "a1b2c3")
Sortie
True

Entrée
hidenp("ace", "abcde")
Sortie
True

Entrée
hidenp("aec", "abcde")
Sortie
False

Entrée
hidenp("", "abc")
Sortie
True

Entrée
hidenp("abc", "ab")
Sortie
False

Entrée
hidenp("aaaa", "aaa")
Sortie
False

Entrée
hidenp("sing","subsequence testing")
Sortie
True
"""
def hidenp(small: str, big: str) -> bool:
    i = 0
    j = 0

    while j < len(big) and i < len(small):
        if small[i] == big[j]:
            i = i + 1
        j = j + 1
    if i == len(small):
        return True
    else:
        return False


if __name__ == "__main__":
    print(hidenp("abc", "a1b2c3"))
    print(hidenp("ace", "abcde"))
    print(hidenp("aec", "abcde"))
    print(hidenp("", "abc"))
    print(hidenp("abc", "ab"))
    print(hidenp("aaaa", "aaa"))
    print(hidenp("sing","subsequence testing"))
