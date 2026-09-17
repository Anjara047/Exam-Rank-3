#!/usr/bin/env python3

"""
Règles et contraintes Moulinette
Fonctions / modules interdits : sorted(), list.sort(). Utilisez uniquement les fonctions autorisées pour éviter un zéro le jour de l’examen.
Énoncé

Écris une fonction qui trie une liste de chaînes avec une priorité à trois niveaux :
1. Tri principal : par longueur (croissant)
2. Tri secondaire : lexicographique (alphabétique, insensible à la casse, croissant)
3. Tri tertiaire : par nombre de voyelles (croissant, si longueur et ordre lexicographique égaux)

La fonction doit gérer :
- Chaînes vides et listes vides
- Casses mixtes (traiter comme des minuscules pour le tri)
- Caractères spéciaux (les ignorer pour compter les voyelles)

Fonctions interdites : sorted(), list.sort()

Signature de la fonction

def cryptic_sorter(strings: list[str]) -> list[str]:
Exemples:
Entrée
cryptic_sorter(["apple","cat","banana","dog","elephant"])
Sortie
["cat","dog","apple","banana","elephant"]

Entrée
cryptic_sorter(["aaa","bbb","AAA","BBB"])
Sortie
["aaa", "AAA", "bbb", "BBB"]

Entrée
cryptic_sorter(["hello","world","hi","test"])
Sortie
["hi","test","hello","world"]

Entrée
cryptic_sorter([])
Sortie
[]

Entrée
cryptic_sorter([""])
Sortie
[""]
"""

def sorting(strings: list[str], key) -> list[str]:
    i = 0
    while i < len(strings) - 1:
        if key(strings[i]) > key(strings[i + 1]):
            strings[i], strings[i + 1] = strings[i + 1], strings[i]
            i = 0
        else:
            i = i + 1
    return strings


def cryptic_sorter(strings: list[str]) -> list[str]:
    return sorting(strings, lambda x: (len(x), x.lower(), x.isupper()))


if __name__ == "__main__":
    print(cryptic_sorter(["apple","cat","banana","dog","elephant"]))
    print(cryptic_sorter(["hello","world","hi","test"]))
    print(cryptic_sorter(["aaa","bbb","AAA","BBB"]))
    print(cryptic_sorter([""]))
    print(cryptic_sorter([]))
