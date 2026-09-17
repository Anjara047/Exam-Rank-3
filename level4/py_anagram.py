#!/usr/bin/env python3
"""
Règles et contraintes Moulinette
Fonctions autorisées : Aucune. Utilisez uniquement les fonctions autorisées pour éviter un zéro le jour de l’examen.
Énoncé

Écris une fonction qui vérifie si deux chaînes sont des anagrammes. Elles doivent contenir exactement les mêmes lettres avec les mêmes quantités, en ignorant la casse et les espaces.

Signature de la fonction

def anagram(s1: str, s2: str) -> bool:

Exemples:

Entrée
anagram("listen", "silent")
Sortie
True

Entrée
anagram("Triangle", "Integral")
Sortie
True

Entrée
anagram("Dormitory", "Dirty Room")
Sortie
True

Entrée
anagram("hello", "world")
Sortie
False

Entrée
anagram("", "")
Sortie
True

Entrée
anagram("abc", "abcc")
Sortie
False
"""
def anagram(s1: str, s2: str) -> bool:
    clean_s1 = ""
    clean_s2 = ""
    space_s1 = ""
    space_s2 = ""
    for char in s1:
        if char != " ":
            clean_s1 += char.lower()
    for c in s2:
        if c != " ":
            clean_s2 += c.lower()
    if len(clean_s1) != len(clean_s2):
        return False
    for char in clean_s1:
        if char not in clean_s2:
            return False
        else:
            return True
    for c in s1:
        if c == " ":
            space_s1 += c
    for c in s2:
        if c == " ":
            space_s2 += c
    if len(space_s1) == len(space_s2):
        return True
    else:
        return False

if __name__ == "__main__":
    print(anagram("listen", "silent"))
    print(anagram("Triangle", "Integral"))
    print(anagram("Dormitory", "Dirty Room"))
    print(anagram("hello", "world"))
    print(anagram("", ""))
    print(anagram("abc", "abcc"))
    print(anagram("   ", "   "))