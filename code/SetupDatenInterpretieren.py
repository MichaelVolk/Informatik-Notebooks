import matplotlib.pyplot as plt


def zeige_lernplot():
    stunden_allg = [0.5, 0.5, 1.0, 1.0, 1.5, 1.5, 2.0, 2.0, 2.5, 2.5,
                    3.0, 3.0, 3.5, 3.5, 4.0, 4.0, 4.5, 5.0, 5.0, 5.5,
                    5.5, 6.0, 6.0, 6.5, 7.0, 7.0, 7.5, 8.0, 8.5, 9.0]
    punkte_allg  = [28, 55, 32, 60, 42, 70, 38, 75, 52, 65,
                    55, 82, 60, 68, 58, 88, 72, 70, 92, 75,
                    55, 80, 93, 85, 78, 95, 82, 88, 92, 90]

    # Person 1: wenig Lernzeit, konstant gute Ergebnisse
    stunden_p1 = [0.5, 1.0, 1.5, 0.5, 1.0]
    punkte_p1  = [70, 72, 74, 80, 75]

    # Person 2: sehr unterschiedliche Lernzeiten, immer ähnliche Ergebnisse
    stunden_p2 = [1.0, 3.0, 5.5, 7.0, 9.0]
    punkte_p2  = [62, 58, 64, 60, 63]

    # Person 3: mehr Lernen = deutlich bessere Ergebnisse
    stunden_p3 = [1.0, 3.0, 5.0, 7.0, 9.0]
    punkte_p3  = [38, 55, 68, 82, 92]

    plt.figure(figsize=(10, 6))
    plt.scatter(stunden_allg, punkte_allg, color="steelblue", alpha=0.5, label="Allgemeine Daten")
    plt.scatter(stunden_p1, punkte_p1, color="red", s=80, zorder=5, label="Person 1")
    plt.scatter(stunden_p2, punkte_p2, color="green", s=80, zorder=5, label="Person 2")
    plt.scatter(stunden_p3, punkte_p3, color="purple", s=80, zorder=5, label="Person 3")
    plt.xlabel("Lernstunden vor der Klausur")
    plt.ylabel("Erreichte Punktzahl (%)")
    plt.title("Lernzeit und Klausurergebnis")
    plt.legend()
    plt.xlim(-0.2, 10)
    plt.ylim(0, 100)
    plt.show()
