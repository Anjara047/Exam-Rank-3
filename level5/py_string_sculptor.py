#!/usr/bin/env python3
"""
Règles et contraintes Moulinette
Fonctions autorisées : Aucune. Utilisez uniquement les fonctions autorisées pour éviter un zéro le jour de l’examen.
Énoncé

Écris une fonction qui transforme une chaîne en alternant la casse des seuls caractères alphabétiques. Les autres caractères restent inchangés et ne comptent pas pour l’alternance. Le premier caractère alphabétique doit être en minuscule, le second en majuscule, le troisième en minuscule, etc. Les espaces réinitialisent l’alternance (la lettre suivante après un espace est à nouveau en minuscule).

Signature de la fonction

def string_sculptor(text: str) -> str:

Exemples:

Entrée
string_sculptor("hello")
Sortie
"hElLo"

Entrée
string_sculptor("Hello World")
Sortie
"hElLo wOrLd"

Entrée
string_sculptor("abc123def")
Sortie
"aBc123DeF"

Entrée
string_sculptor("Python3.9!")
Sortie
"pYtHoN3.9!"

Entrée
string_sculptor("")
Sortie
""
"""
def string_sculptor(text: str) -> str:
    result = ""
    i = 0
    for char in text:
        if char.isalpha():
            if i % 2 == 0:
                result += char.lower()
            else:
                result += char.upper()
            i = i +1
        else:
            result +=  char
    return result
if __name__ == "__main__":
    print(string_sculptor("hello"))
    print(string_sculptor("Hello World"))
    print(string_sculptor("abc123def"))
    print(string_sculptor("Python3.9!"))
    print(string_sculptor(""))