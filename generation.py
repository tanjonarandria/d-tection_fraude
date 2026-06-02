#!python3
import Etudiant
import random


def connecter_sommet(x, y, G):
    if x not in G:
        G[x] = []
    if y not in G[x]:
        G[x].append(y)
    if y not in G:
        G[y] = []
    if x not in G[y]:
        G[y].append(x)


def genereG(nb_sommet, proba):
    list_etudiant = []
    G = {}
    roles = ["Citoyen", "Consommateur", "Dealer", "Fournisseur"]

    for x in range(nb_sommet):
        e = Etudiant.Etudiant()
        e.id = x
        e.role = random.choice(roles)
        list_etudiant.append(e)
        G[e] = []

    for x in list_etudiant:
        for y in list_etudiant:
            if x != y:
                p = random.random()
                if p <= proba:
                    connecter_sommet(x, y, G)
                    
    return G, list_etudiant#!python3
import Etudiant
import random


def connecter_sommet(x, y, G):
    if x not in G:
        G[x] = []
    if y not in G[x]:
        G[x].append(y)
    if y not in G:
        G[y] = []
    if x not in G[y]:
        G[y].append(x)


def genereG(nb_sommet, proba):
    list_etudiant = []
    G = {}
    roles = ["Citoyen", "Consommateur", "Dealer", "Fournisseur"]

    for x in range(nb_sommet):
        e = Etudiant.Etudiant()
        e.id = x
        e.role = random.choice(roles)
        list_etudiant.append(e)
        G[e] = []

    for x in list_etudiant:
        for y in list_etudiant:
            if x != y:
                p = random.random()
                if p <= proba:
                    connecter_sommet(x, y, G)
                    
    return G, list_etudiant