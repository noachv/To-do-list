active = True
import os

# 📂 Chemin complet du dossier où tu veux enregistrer le fichier
chemin_dossier = r"D:\ECOLE\Solo\To do list"

# 📄 Nom complet du fichier
chemin_fichier = os.path.join(chemin_dossier, "taches.txt")

# ✅ Crée le dossier s’il n’existe pas (évite les erreurs)
os.makedirs(chemin_dossier, exist_ok=True)

def choix_1_add():
    with open(chemin_fichier, "a") as fichier:
        tache_1 = input("Quelle tâche voulez-vous ajouter ? ")
        fichier.write(f"{tache_1} | False\n")

    new = input("Voulez-vous encore ajouter une nouvelle tâche ? (oui/non) : ")
    if new.lower().strip() == "oui":
        choix_1_add()
    else:
        print("Tâches enregistrées !")


def choix_2_marked_as_done():
    try:
        with open(chemin_fichier, "r") as fichier:
            lignes = fichier.readlines()

        if not lignes:
            print("Aucune tâche à valider pour le moment !")
            return

        print("\n=== Liste des tâches ===")
        for i, ligne in enumerate(lignes, start=1):
            nom, etat = ligne.strip().split(" | ")
            statut = "✅" if etat == "True" else "❌"
            print(f"{i}. [{statut}] {nom}")

        tache_a_valider = int(input("\nQuelle tâche voulez-vous valider ? "))
        if 1 <= tache_a_valider <= len(lignes):
            nom, etat = lignes[tache_a_valider - 1].strip().split(" | ")
            lignes[tache_a_valider - 1] = f"{nom} | True\n"
            with open(chemin_fichier, "w") as fichier:
                fichier.writelines(lignes)
            print(f"✅ Tâche '{nom}' validée avec succès !")
        else:
            print("Numéro invalide.")

    except FileNotFoundError:
        print("Le fichier", chemin_fichier, "n'existe pas encore.")

def choix_4_afficher():
    with open(chemin_fichier, "r") as fichier:
            lignes = fichier.readlines()
    print("\n=== Liste des tâches ===")
    for i, ligne in enumerate(lignes, start=1):
        nom, etat = ligne.strip().split(" | ")
        statut = "✅" if etat == "True" else "❌"
        print(f"{i}. [{statut}] {nom}")
    
def choix_3_marked_as_not_done():
    try:
        with open(chemin_fichier, "r") as fichier:
            lignes = fichier.readlines()

        if not lignes:
            print("Aucune tâche à valider pour le moment !")
            return

        print("\n=== Liste des tâches ===")
        for i, ligne in enumerate(lignes, start=1):
            nom, etat = ligne.strip().split(" | ")
            statut = "❌" if etat == "False" else "✅"
            print(f"{i}. [{statut}] {nom}")

        tache_a_valider = int(input("\nQuelle tâche voulez-vous dé-valider ? "))
        if 1 <= tache_a_valider <= len(lignes):
            nom, etat = lignes[tache_a_valider - 1].strip().split(" | ")
            lignes[tache_a_valider - 1] = f"{nom} | False\n"
            with open(chemin_fichier, "w") as fichier:
                fichier.writelines(lignes)
            print(f"❌ Tâche '{nom}' dé-validée avec succès !")
        else:
            print("Numéro invalide.")

    except FileNotFoundError:
        print("Le fichier", chemin_fichier, "n'existe pas encore.")

def choix_5_del_tache():
    try:
        with open(chemin_fichier, "r") as fichier:
            lignes = fichier.readlines()

        if not lignes:
            print("Aucune tâche à supprimer.")
            return

        print("\n=== Liste des tâches ===")
        for i, ligne in enumerate(lignes, start=1):
            nom, etat = ligne.strip().split(" | ")
            statut = "✅" if etat == "True" else "❌"
            print(f"{i}. [{statut}] {nom}")

        tache_a_sup = int(input("\nNuméro de la tâche à supprimer : ")) - 1

        if 0 <= tache_a_sup < len(lignes):
            nom, etat = lignes[tache_a_sup].strip().split(" | ")
            del lignes[tache_a_sup]

            with open(chemin_fichier, "w") as fichier:
                fichier.writelines(lignes)
            
            print(f"🗑️    Tâche '{nom}' supprimée avec succès !")
        else:
            print("Numéro invalide.")

        new = input("Voulez-vous supprimer une nouvelle tâche ? (oui/non) : ")
        if new.lower().strip() == "oui":
           choix_5_del_tache()

    except FileNotFoundError:
        print("Le fichier n'existe pas encore.")

def choix_6_exit():
    exit()




while True:
    print("""====Gestionnaire des tâches====
1. Ajouter une tâche
2. Marquer une tâche comme terminée
3. Marquer une tâche comme non terminée
4. Afficher les tâches
5. Supprimer une tâche
6. Quitter
=============================""")
    choix = int(input("Que voulez-vous faire ? "))

    if choix == 1:
        choix_1_add()
    elif choix == 2:
        choix_2_marked_as_done()
    elif choix == 4:
        choix_4_afficher()
    elif choix == 3:
        choix_3_marked_as_not_done()
    elif choix == 5:
        choix_5_del_tache()
    elif choix == 6:
        choix_6_exit()

    else:
        active = False