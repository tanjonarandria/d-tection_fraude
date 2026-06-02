def _bron_kerbosch(R, P, X, G_set, toutes_les_cliques):
    if not P and not X:
        toutes_les_cliques.append(R)
        return
    
    pivot = list(P.union(X))[0]
    for sommet in list(P.difference(G_set[pivot])):
        voisins = G_set[sommet]
        _bron_kerbosch(
            R.union({sommet}),
            P.intersection(voisins),
            X.intersection(voisins),
            G_set,
            toutes_les_cliques
        )
        P.remove(sommet)
        X.add(sommet)


def chercher_toutes_les_cliques(G):
    toutes_les_cliques = []
    G_set = {sommet: set(voisins) for sommet, voisins in G.items()}
    _bron_kerbosch(set(), set(G.keys()), set(), G_set, toutes_les_cliques)
    return toutes_les_cliques