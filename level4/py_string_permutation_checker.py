#!/usr/bin/env python3
"""
Règles et contraintes Moulinette
Fonctions autorisées : Aucune. Utilisez uniquement les fonctions autorisées pour éviter un zéro le jour de l’examen.
Énoncé

Écris une fonction qui détermine si deux chaînes sont des permutations l’une de l’autre.
Deux chaînes sont des permutations si elles contiennent les mêmes caractères avec les mêmes fréquences.

La fonction doit :
- Vérifier que les deux chaînes contiennent exactement les mêmes caractères
- Compter les fréquences (sensible à la casse)
- Retourner True si ce sont des permutations, sinon False
- Gérer les chaînes vides (deux chaînes vides sont des permutations)
- Traiter espaces et ponctuation comme des caractères normaux

Signature de la fonction

def string_permutation_checker(s1: str, s2: str) -> bool:

Exemples:

Entrée
string_permutation_checker("abc", "bca")
Sortie
True

Entrée
string_permutation_checker("abc", "def")
Sortie
False

Entrée
string_permutation_checker("listen", "silent")
Sortie
True

Entrée
string_permutation_checker("hello", "bello")
Sortie
False

Entrée
string_permutation_checker("", "")
Sortie
True

Entrée
string_permutation_checker("a", "")
Sortie
False

Entrée
string_permutation_checker("Abc", "abc")
Sortie
False

Entrée
string_permutation_checker("a gentleman","elegant man")
Sortie
True
"""
def string_permutation_checker(s1: str, s2: str) -> bool:
    if s1 == "" and s2 == "":
        return True
    if s1 == "" or s2 == "":
        return False
    for c in s1:
        if c in s2:
            if len(s1) == len(s2):
                return True
            else:
                return False
        else:
            return False
if __name__ == "__main__":
    print(string_permutation_checker("abc", "bca"))
    print(string_permutation_checker("abc", "def"))
    print(string_permutation_checker("listen", "silent"))
    print(string_permutation_checker("hello", "bello"))
    print(string_permutation_checker("", ""))
    print(string_permutation_checker("a", ""))
    print(string_permutation_checker("Abc", "abc"))
    print(string_permutation_checker("a gentleman","elegant man"))