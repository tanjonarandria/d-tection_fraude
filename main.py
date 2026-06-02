import generation
import sauvegarde
import clique_mathematique
import math

n = int(input("Nombre d'étudiants : "))
p = math.log(n) / n

G, list_etudiant = generation.genereG(n, p)

les_cliques = clique_mathematique.chercher_toutes_les_cliques(G)

print("\n=== ANALYSE DES CLIQUES MATHÉMATIQUES ===")
print(f"Total de cliques maximales : {len(les_cliques)}")
for i, clique in enumerate(les_cliques):
    if len(clique) >= 3:
        ids = sorted([e.id for e in clique])
        roles = [e.role for e in clique]
        print(f"Clique n°{i+1} (Taille {len(clique)}) : IDs {ids} | Rôles: {roles}")
print("=========================================\n")

sauvegarde.sauvegarder_graphe(G)
sauvegarde.fermer_connexion()