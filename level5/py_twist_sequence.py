#!/usr/bin/env python3
"""
Règles et contraintes Moulinette
Fonctions autorisées : Aucune. Utilisez uniquement les fonctions autorisées pour éviter un zéro le jour de l’examen.
Énoncé

Écris une fonction qui effectue une rotation à droite d'un tableau de k positions. Une rotation à droite de k signifie que les k derniers éléments sont déplacés vers l'avant.

Signature de la fonction

def twist_sequence(arr: list[int], k: int) -> list[int]:

Exemples:

Entrée
twist_sequence([1,2,3,4,5], 2)
Sortie
[4,5,1,2,3]

Entrée
twist_sequence([1,2,3], 1)
Sortie
[3,1,2]

Entrée
twist_sequence([1,2,3,4], 0)
Sortie
[1,2,3,4]

Entrée
twist_sequence([1,2,3], 5)
Sortie
[2,3,1]

Entrée
twist_sequence([], 3)
Sortie
[]
"""
def twist_sequence(arr: list[int], k: int) -> list[int]:
    if len(arr) == 0:
        return []
    k = k % len(arr)
    for number in arr:
        return arr[-k:] + arr[:-k]

if __name__ == "__main__":
    print(twist_sequence([1, 2, 3, 4, 5], 2))
    print(twist_sequence([1, 2, 3], 1))
    print(twist_sequence([1, 2, 3, 4], 0))
    print(twist_sequence([1, 2, 3], 5))
    print(twist_sequence([], 3))