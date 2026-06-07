import template.output as output
import matplotlib.pyplot as plt


def zeige_korrelationsbeispiele():
    x_pos = [1, 2, 2, 3, 4, 5, 5, 6, 6, 7, 8, 8, 9, 10, 4]
    y_pos = [3, 5, 7, 9, 10, 13, 11, 15, 13, 17, 19, 17, 21, 23, 18]

    x_neg = [1, 2, 2, 3, 4, 5, 5, 6, 6, 7, 8, 8, 9, 10, 7]
    y_neg = [22, 19, 21, 17, 14, 12, 14, 10, 12, 8, 6, 8, 4, 2, 18]

    x_kein = [1, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 10]
    y_kein = [12, 5, 18, 3, 14, 9, 20, 2, 15, 7, 16, 4, 11, 19, 8]

    fig, achsen = plt.subplots(1, 3, figsize=(14, 4))

    achsen[0].scatter(x_pos, y_pos)
    achsen[0].set_title("Typ A")
    achsen[0].set_xlabel("Variable A")
    achsen[0].set_ylabel("Variable B")

    achsen[1].scatter(x_neg, y_neg)
    achsen[1].set_title("Typ B")
    achsen[1].set_xlabel("Variable A")

    achsen[2].scatter(x_kein, y_kein)
    achsen[2].set_title("Typ C")
    achsen[2].set_xlabel("Variable A")

    plt.tight_layout()
    plt.show()


def get_einkommen_daten():
    # Monatliche Streaming-Einnahmen von 10 Musiker:innen in Euro
    # 9 davon verdienen zwischen 1150 und 1600 €, eine Person ist ein Superstar
    return [1200, 1350, 1450, 1300, 1600, 1250, 1500, 1400, 1150, 32000]


def get_follower_daten():
    # Instagram-Follower-Zahlen einer Schulklasse
    # Ein Mitglied ist Influencer
    return [120, 200, 185, 300, 250, 165, 180, 220, 4500, 280, 195, 210]


def get_feuerwehr_daten():
    # Brandeinsätze: Anzahl Feuerwehrleute vor Ort vs. Sachschaden in Tausend Euro
    # Ausreißer: (10, 220) – wenige Feuerwehrleute, trotzdem hoher Schaden (z.B. Chemieunfall)
    feuerwehrleute = [5, 6, 8, 8, 10, 12, 14, 15, 15, 18,
                      20, 22, 25, 28, 30, 35, 38, 42, 45, 50, 10]
    schaden_tsd    = [12, 25, 20, 40, 55, 70, 85, 100, 120, 140,
                      180, 200, 240, 290, 360, 460, 510, 590, 640, 720, 220]
    return feuerwehrleute, schaden_tsd


def get_lerndaten():
    lernstunden = [0.5, 1, 1.5, 2, 2, 3, 3, 3.5, 4, 4.5, 5, 6, 7, 8]
    klausurnoten = [32, 38, 45, 50, 55, 60, 63, 68, 72, 74, 80, 83, 88, 94]
    return lernstunden, klausurnoten
