#!/usr/bin/env python3
"""
Règles et contraintes Moulinette
Fonctions autorisées : Aucune. Utilisez uniquement les fonctions autorisées pour éviter un zéro le jour de l’examen.
Énoncé

Écris une fonction qui réalise un chiffrement simple en décalant les lettres d’une chaîne d’un montant donné. Les caractères non alphabétiques restent inchangés.

Signature de la fonction

def whisper_cipher(text: str, shift: int) -> str:

Exemples:

Entrée
whisper_cipher("hello", 3)
Sortie
"khoor"

Entrée
whisper_cipher("Hello World!", 1)
Sortie
"Ifmmp Xpsme!"

Entrée
whisper_cipher("xyz", 3)
Sortie
"abc"

Entrée
whisper_cipher("ABC123def", 5)
Sortie
"FGH123ijk"

Entrée
whisper_cipher("", 10)
Sortie
""

Entrée
whisper_cipher("abc", -3)
Sortie
"xyz"
"""
def whisper_cipher(text: str, shift: int) -> str:
    result = ""
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for char in text:
        if char in lower:
            i = lower.index(char)
            i = (i + shift) % 26
            result += lower[i]
        elif char in upper:
            i = upper.index(char)
            i = (i + shift) % 26
            result += upper[i]
        else:
            result += char
    return result


if __name__ == "__main__":
    print(whisper_cipher("hello", 3))
    print(whisper_cipher("Hello World!", 1))
    print(whisper_cipher("xyz", 3))
    print(whisper_cipher("ABC123def", 5))
    print(whisper_cipher("", 10))
    print(whisper_cipher("abc", -3))