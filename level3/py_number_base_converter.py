#!/usr/bin/env python3
"""
Règles et contraintes Moulinette
Fonctions autorisées : Aucune. Utilisez uniquement les fonctions autorisées pour éviter un zéro le jour de l’examen.
Énoncé

Écris une fonction qui convertit un nombre d'une base vers une autre.
Prends en charge les bases de 2 à 36 inclus, avec les chiffres 0-9 et les lettres A-Z pour les valeurs 10-35. Renvoie "ERROR" pour les entrées invalides (base, chiffres).

Signature de la fonction

def number_base_converter(number: str, from_base: int, to_base: int) -> str:

Exemples:

Entrée
number_base_converter("1010", 2, 10)
Sortie
"10"

Entrée
number_base_converter("FF", 16, 10)
Sortie
"255"

Entrée
number_base_converter("255", 10, 16)
Sortie
"FF"

Entrée
number_base_converter("123", 10, 2)
Sortie
"1111011"

Entrée
number_base_converter("Z", 36, 10)
Sortie
"35"

Entrée
number_base_converter("35", 10, 36)
Sortie
"Z"

Entrée
number_base_converter("123", 1, 10)
Sortie
"ERROR"

Entrée
number_base_converter("G", 16, 10)
Sortie
"ERROR"
"""
def number_base_converter(
    number: str, from_base: int, to_base: int
) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if from_base < 2 or from_base > 36:
        return "ERROR"
    if to_base < 2 or to_base > 36:
        return "ERROR"
    decimal = 0
    for c in number:
        if c not in digits:
            return "ERROR"
        value = digits.index(c)
        if value >= from_base:
            return "ERROR"
        decimal = decimal * from_base + value
    if decimal == 0:
        return "0"
    result = ""
    while decimal > 0:
        value = decimal % to_base
        result = digits[value] + result
        decimal = decimal // to_base
    return result


if __name__ == "__main__":
    print(number_base_converter("1010", 2, 10))
    print(number_base_converter("FF", 16, 10))
    print(number_base_converter("255", 10, 16))
    print(number_base_converter("123", 10, 2))
    print(number_base_converter("Z", 36, 10))
    print(number_base_converter("35", 10, 36))
    print(number_base_converter("123", 1, 10))
    print(number_base_converter("G", 16, 10))