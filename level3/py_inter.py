#!/usr/bin/env python3
"""
Règles et contraintes Moulinette
Fonctions autorisées : Aucune. Utilisez uniquement les fonctions autorisées pour éviter un zéro le jour de l’examen.
Énoncé

Écris une fonction qui renvoie une chaîne contenant les caractères qui apparaissent dans les deux chaînes, sans répétition. Les caractères sont ajoutés dans l'ordre où ils apparaissent dans la première chaîne.

Signature de la fonction

def inter(s1: str, s2: str) -> str:

Exemples:

Entrée
inter("hello", "world")
Sortie
"lo"

Entrée
inter("banana", "band")
Sortie
"ban"

Entrée
inter("abcabc", "bc")
Sortie
"bc"

Entrée
inter("abc", "xyz")
Sortie
""

Entrée
inter("", "abc")
Sortie
""
"""
def inter(s1: str, s2: str) -> str:
    result = ""
    seen = set()

    i = 0
    while i < len(s1):
        j = 0
        while j < len(s2):
            if s1[i] == s2[j] and s1[i] not in seen:
                result += s1[i]
                seen.add(s1[i])
                break
            j = j + 1
        i = i + 1
    return result

if __name__ == "__main__":
    print(inter("hello", "world"))
    print(inter("banana", "band"))
    print(inter("abcabc", "bc"))
    print(inter("abc", "xyz"))
    print(inter("", "abc"))