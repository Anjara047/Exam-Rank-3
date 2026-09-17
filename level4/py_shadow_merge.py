#!/usr/bin/env python3
"""
Règles et contraintes Moulinette
Fonctions autorisées : Aucune. Utilisez uniquement les fonctions autorisées pour éviter un zéro le jour de l’examen.
Énoncé

Écris une fonction qui fusionne deux listes triées en une seule liste triée.

Signature de la fonction

def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:

Exemples:

Entrée
shadow_merge([1,3,5], [2,4,6])
Sortie
[1,2,3,4,5,6]

Entrée
shadow_merge([1,2,3], [4,5,6])
Sortie
[1,2,3,4,5,6]

Entrée
shadow_merge([1], [2,3,4])
Sortie
[1,2,3,4]

Entrée
shadow_merge([], [1,2,3])
Sortie
[1,2,3]

Entrée
shadow_merge([1,1,2], [1,3,3])
Sortie
[1,1,1,2,3,3]
"""
def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    result = []
    for c in list1:
        result.append(c)
    for c in list2:
        result.append(c)
    return result

if __name__ == "__main__":
    print(shadow_merge([1,3,5], [2,4,6]))
    print(shadow_merge([1,2,3], [4,5,6]))
    print(shadow_merge([1], [2,3,4]))
    print(shadow_merge([], [1,2,3]))
    print(shadow_merge([1,1,2], [1,3,3]))
