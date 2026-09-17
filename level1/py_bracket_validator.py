#!/usr/bin/env python3
"""
Règles et contraintes Moulinette
Fonctions autorisées : Aucune. Utilisez uniquement les fonctions autorisées pour éviter un zéro le jour de l’examen.
Énoncé

Écris une fonction qui vérifie si les parenthèses d’une chaîne sont correctement appariées et imbriquées.
Prends en charge trois types : (), [], {}.

La fonction doit :
- Retourner True si toutes les parenthèses sont correctement appariées
- Retourner True pour les chaînes sans aucune parenthèse
- Retourner False si elles ne correspondent pas ou sont mal imbriquées
- Ignorer les caractères qui ne sont pas des parenthèses

Signature de la fonction

#def bracket_validator(s: str) -> bool:

Exemples:

Entrée
bracket_validator("()")
Sortie
True

Entrée
bracket_validator("()[]{}")
Sortie
True

Entrée
bracket_validator("(]")
Sortie
False

Entrée
bracket_validator("([)]")
Sortie
False

Entrée
bracket_validator("{[]}")
Sortie
True

Entrée
bracket_validator("hello(world)")
Sortie
True

Entrée
bracket_validator("((())")
Sortie
False

Entrée
bracket_validator("")
Sortie
True
"""
def bracket_validator(s: str) -> bool:
	stack = []
	for c in s:
		if c == "{":
			stack.append("}")
		elif c == "(":
			stack.append(")")
		elif c == "[":
			stack.append("]")
		elif c == ")" or c == "]" or c == "}":
			if len(stack) == 0:
				return False
			if stack[-1] != c:
				return False
			stack.pop()
	
	if len(stack) == 0:
		return True
	else:
		return False
if __name__ == "__main__":
	print(bracket_validator("([)]"))
