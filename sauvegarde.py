from neo4j import GraphDatabase

uri = "neo4j://127.0.0.1:7687"
user = "neo4j"
password = "12345678"

driver = GraphDatabase.driver(uri, auth=(user, password))

COULEURS_ROLES = {
    "Dealer": "red",
    "Consommateur": "green",
    "Fournisseur": "orange",
    "Citoyen": "blue"
}

def vider_base(tx):
    tx.run("MATCH (n) DETACH DELETE n")

def creer_etudiant(tx, etudiant):
    couleur = COULEURS_ROLES.get(etudiant.role, "gray")
    tx.run(
        """
        MERGE (e:Etudiant {id: $id})
        SET e.role = $role,
            e.couleur_nom = $couleur
        """,
        id=etudiant.id, role=etudiant.role, couleur=couleur
    )

def creer_relation(tx, id_x, id_y):
    tx.run(
        """
        MATCH (a:Etudiant {id: $id_x}), (b:Etudiant {id: $id_y})
        MERGE (a)-[:CONNAIT]->(b)
        MERGE (b)-[:CONNAIT]->(a)
        """,
        id_x=id_x, id_y=id_y
    )

def sauvegarder_graphe(G):
    with driver.session() as session:
        print("Nettoyage de Neo4j...")
        session.execute_write(vider_base)

        print("Sauvegarde des étudiants et de leurs rôles...")
        for etudiant in G:
            session.execute_write(creer_etudiant, etudiant)

        print("Sauvegarde des relations non orientées...")
        for etudiant, voisins in G.items():
            for voisin in voisins:
                if etudiant.id < voisin.id:
                    session.execute_write(creer_relation, etudiant.id, voisin.id)
        print("Sauvegarde Neo4j réussie !")

def fermer_connexion():
    driver.close()