#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    # TODO completer la fonction ici
    nouveauMot = ""
    for lettre in mot:
        if 'a' <= lettre <= 'z':
            nouveauMot += chr(ord(lettre) - 32)
        else:
            nouveauMot += lettre

    return nouveauMot


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
