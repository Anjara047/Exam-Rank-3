#!/usr/bin/env python3
"""
Règles et contraintes Moulinette
Fonctions autorisées : Aucune. Utilisez uniquement les fonctions autorisées pour éviter un zéro le jour de l’examen.
Énoncé

Écris une fonction qui compte le nombre de paires de chiffres consécutifs valides dans une chaîne. Une paire valide est formée de deux chiffres adjacents dont le second vaut exactement un de plus que le premier. Un 9 suivi d’un 0 n’est PAS une paire valide.

Signature de la fonction

def pattern_tracker(text: str) -> int:

Exemples
Entrée
pattern_tracker("123")
Sortie
2
Entrée
pattern_tracker("12a34")
Sortie
2
Entrée
pattern_tracker("987654321")
Sortie
0
Entrée
pattern_tracker("01234567")
Sortie
7
Entrée
pattern_tracker("abc")
Sortie
0
Entrée
pattern_tracker("1a2b3c4")
Sortie
0
Entrée
pattern_tracker("112233")
Sortie
2
"""
def pattern_tracker(text: str) -> int:
    count = 0
    i = 0
    while i < len(text) - 1:
        if '0' <= text[i] <= '9' and '0' <= text[i + 1] <= '9':
            if int(text[i + 1]) == int(text[i]) + 1:
                count += 1
        i += 1
    return count

if __name__ == "__main__":
    print(pattern_tracker("123"))
    print(pattern_tracker("12a34"))
    print(pattern_tracker("987654321"))
    print(pattern_tracker("01234567"))
    print(pattern_tracker("abc"))
    print(pattern_tracker("1a2b3c4"))
    print(pattern_tracker("112233"))