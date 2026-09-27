import time

# Dictionnaire de référence (extensible)
EXERCICES_BASE = {
    "développé couché": "poly",
    "squat": "poly",
    "soulevé de terre": "poly",
    "développé militaire": "poly",
    "tractions": "poly",
    "tirage poitrine": "poly",
    "dips": "poly",
    "fentes": "poly",
    "curl biceps": "mono",
    "extension triceps": "mono",
    "élévations latérales": "mono",
    "leg extension": "mono",
    "leg curl": "mono",
    "écarté couché": "mono",
    "elevation laterale": "mono",
    "developpe militaire": "poly",
    "poulie pro": "mono",
    "poulie arriere": "mono",
    "dips machine": "poly",
    "ecarte machine": "mono",
    "butterfly": "mono"
}


def determiner_type(nom_exercice):
    clean_nom = nom_exercice.strip().lower()
    if clean_nom in EXERCICES_BASE:
        return EXERCICES_BASE[clean_nom]

    print(f"\n⚠️ Exercice « {nom_exercice} » non répertorié.")
    while True:
        choix = (
            input(
                "Tape (1) pour Polyarticulaire ou (2) pour Monoarticulaire : "
            )
            .strip()
            .lower()
        )
        if choix in ["1", "poly", "polyarticulaire"]:
            return "poly"
        elif choix in ["2", "mono", "monoarticulaire"]:
            return "mono"
        print("Entrée invalide.")


def lancer_repos(secondes):
    print(
        f"\n⏱️ Repos : {secondes // 60} minute(s). Appuie sur Entrée pour démarrer le chrono (ou Ctrl+C pour passer)..."
    )
    try:
        input()
        for t in range(secondes, 0, -1):
            mins, secs = divmod(t, 60)
            print(f"\rTemps restant : {mins:02d}:{secs:02d}", end="")
            time.sleep(1)
        print("\n🔔 Temps écoulé ! Place à la série suivante.")
    except KeyboardInterrupt:
        print("\n⏩ Repos passé.")


def gerer_exercice(nom_exercice):
    type_exo = determiner_type(nom_exercice)

    is_poly = type_exo == "poly"
    max_series = 4 if is_poly else 3
    temps_repos = 180 if is_poly else 120  # en secondes
    label_type = "Polyarticulaire" if is_poly else "Monoarticulaire"

    print("\n" + "=" * 45)
    print(f"🏋️  EXERCICE : {nom_exercice.upper()}")
    print(f"📌 Type : {label_type}")
    print(f"⏱️  Repos : {temps_repos // 60} min | Séries prévues : 2 à {max_series}")
    print("=" * 45)

    reps_s1 = None

    for serie_actuelle in range(1, max_series + 1):
        while True:
            try:
                reps = int(
                    input(
                        f"\nSérie {serie_actuelle}/{max_series} — Nombre de répétitions : "
                    )
                )
                if reps <= 0:
                    print("Rentre un nombre strictement positif.")
                    continue
                break
            except ValueError:
                print("Merci de saisir un nombre entier.")

        # Première série : valeur de référence
        if serie_actuelle == 1:
            reps_s1 = reps
            print(f"➔ Série de référence enregistrée : {reps_s1} reps.")
            lancer_repos(temps_repos)
            continue

        # Calcul de la perte de répétitions (Inroad)
        perte_pct = ((reps_s1 - reps) / reps_s1) * 100
        print(f"➔ Inroad : {perte_pct:.1f}% de baisse / Série 1 ({reps_s1} reps)")

        # Vérification des conditions d'arrêt
        if perte_pct >= 20.0:
            print(
                f"\n⛔ Perte >= 20 % atteinte ({perte_pct:.1f} %). Arrêt de l'exercice !"
            )
            print("➡️ PASSE À L'EXERCICE SUIVANT.")
            break
        elif serie_actuelle == max_series:
            print(f"\n✅ Limite de {max_series} séries atteinte.")
            print("➡️ PASSE À L'EXERCICE SUIVANT.")
            break
        else:
            print(
                f"👍 Baisse inférieure à 20 % ({perte_pct:.1f} %). Tu refais une série."
            )
            lancer_repos(temps_repos)


def main():
    print("==========================================")
    print("      GESTIONNAIRE DE SÉANCE DE SPORT     ")
    print("==========================================")

    # Définition du programme
    saisie = input(
        "\nRentre tes exercices séparés par des virgules\n(ex: Développé couché, Élévations latérales, Leg extension) :\n> "
    ).strip()

    if not saisie:
        # Programme par défaut si rien n'est saisi
        exercices = [
            "Développé couché",
            "Élévations latérales",
            "Curl biceps",
            "Leg extension",
        ]
        print(
            f"\nAucune saisie. Lancement du programme par défaut : {', '.join(exercices)}"
        )
    else:
        exercices = [e.strip() for e in saisie.split(",") if e.strip()]

    # Déroulement de la séance
    for exo in exercices:
        gerer_exercice(exo)

    print("\n==========================================")
    print("🏁 SÉANCE TERMINÉE !")
    print("==========================================")


if __name__ == "__main__":
    main()