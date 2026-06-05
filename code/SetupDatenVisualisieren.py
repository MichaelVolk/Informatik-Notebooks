import template.output as output


def get_spotify_daten():
    songs = ["Blinding Lights", "Shape of You", "As It Was", "Cruel Summer", "Dance Monkey"]
    streams = [4.3, 4.2, 3.2, 3.0, 2.8]
    return songs, streams


def get_stream_verlauf():
    wochen = [1, 2, 3, 4, 5, 6, 7, 8]
    streams_pro_woche = [45, 78, 95, 102, 88, 71, 58, 47]
    return wochen, streams_pro_woche


def get_freizeit_daten():
    aktivitaeten = ["Social Media", "Gaming", "Serien / Filme", "Sport", "Musik hören", "Sonstiges"]
    anteile = [28, 18, 17, 15, 14, 8]
    return aktivitaeten, anteile