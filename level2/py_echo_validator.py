#!/usr/bin/env python3
"""
Règles et contraintes Moulinette
Fonctions autorisées : Aucune. Utilisez uniquement les fonctions autorisées pour éviter un zéro le jour de l’examen.
Énoncé

Écris une fonction qui vérifie si une chaîne est un palindrome, en ignorant espaces et casse, et en ne considérant que les caractères alphabétiques pour la comparaison.

Signature de la fonction

def echo_validator(text: str) -> bool:

Exemples:

Entrée
echo_validator("racecar")
Sortie
True

Entrée
echo_validator("A man a plan a canal Panama")
Sortie
True

Entrée
echo_validator("race a car")
Sortie
False

Entrée
echo_validator("Was it a car or a cat I saw")
Sortie
True

Entrée
echo_validator("hello")
Sortie
False

Entrée
echo_validator("Madam Im Adam")
Sortie
True

Entrée
echo_validator("")
Sortie
False
"""
def echo_validator(text: str) -> bool:
    if text == "":
        return False
    clean = ""
    for char in text:
        if char != " ":
            clean += char.lower()
    if clean == clean[::-1]:
        return True
    return False

if __name__ == "__main__":
    print(echo_validator("racecar"))
    print(echo_validator("A man a plan a canal Panama"))
    print(echo_validator("race a car"))
    print(echo_validator("Was it a car or a cat I saw"))
    print(echo_validator("hello"))
    print(echo_validator("Madam Im Adam"))
    print(echo_validator(""))