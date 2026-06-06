import template.output as output


def get_spotify_daten():
    songs = ["Blindings lights", "Shape of You", "Sweater Weather", "Starboy", "As It Was"]
    streams = [5443318332, 4944382666, 4652758344, 4572269955, 4449375500]
    return songs, streams


def get_stream_verlauf():
    wochen = [1, 2, 3, 4, 5, 6, 7, 8]
    streams_pro_woche = [45, 78, 95, 102, 88, 71, 58, 47]
    return wochen, streams_pro_woche


def get_freizeit_daten():
    aktivitaeten = ["Social Media", "Gaming", "Serien / Filme", "Sport", "Musik hören", "Sonstiges"]
    anteile = [28, 18, 17, 15, 14, 8]
    return aktivitaeten, anteile


def get_gaming_daten():
    stunden = [1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10]
    highscores = [850, 1100, 1250, 1600, 1850, 2100, 2300, 2450, 2800, 3100, 3500, 3750, 4200]
    return stunden, highscores