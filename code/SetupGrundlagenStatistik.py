import template.output as output


def get_einkommen_daten():
    # Monatliche Streaming-Einnahmen von 10 Musiker:innen in Euro
    # 9 davon verdienen zwischen 1150 und 1600 €, eine Person ist ein Superstar
    return [1200, 1350, 1450, 1300, 1600, 1250, 1500, 1400, 1150, 32000]


def get_follower_daten():
    # Instagram-Follower-Zahlen einer Schulklasse
    # Ein Mitglied ist Influencer
    return [120, 200, 185, 300, 250, 165, 180, 220, 4500, 280, 195, 210]


def get_lerndaten():
    lernstunden = [0.5, 1, 1.5, 2, 2, 3, 3, 3.5, 4, 4.5, 5, 6, 7, 8]
    klausurnoten = [32, 38, 45, 50, 55, 60, 63, 68, 72, 74, 80, 83, 88, 94]
    return lernstunden, klausurnoten
