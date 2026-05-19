import template.output as output


def check_variablen(punkte, spieler, gewonnen):
    fehler = []
    if punkte != 100:
        fehler.append("'punkte' hat nicht den richtigen Wert.")
    if spieler != "Anna":
        fehler.append("'spieler' hat nicht den richtigen Wert.")
    if gewonnen is not True:
        fehler.append("'gewonnen' hat nicht den richtigen Wert. Denke an die Groß-/Kleinschreibung (True, nicht true)!")
    if not fehler:
        output.success("Alle Variablen sind korrekt übersetzt!")
    else:
        output.wrong(" | ".join(fehler))


def check_methode(quadrat):
    try:
        if quadrat(4) == 16 and quadrat(0) == 0 and quadrat(3) == 9:
            output.success("Die Methode funktioniert korrekt!")
        else:
            output.wrong("Die Methode gibt für manche Eingaben das falsche Ergebnis zurück.")
    except Exception as e:
        output.wrong("Fehler beim Aufrufen der Methode: " + str(e))


def check_for_schleife(summe):
    if summe == 15:
        output.success("Richtig! Die Schleife liefert das korrekte Ergebnis.")
    else:
        output.wrong("Das Ergebnis stimmt nicht. Erwartet: 15, erhalten: " + str(summe))


def check_arrays(zahlen, ungerade):
    erwartete_zahlen = list(range(100))
    erwartete_ungerade = list(range(1, 200, 2))

    fehler = []

    if zahlen == list(range(99)):
        fehler.append("'zahlen' enthält nur die Zahlen 0–98. Denk daran, dass range(99) bei 0 startet und vor 99 aufhört – für die Zahlen 0–99 brauchst du range(100).")
    elif zahlen != erwartete_zahlen:
        fehler.append("'zahlen' hat nicht den richtigen Inhalt. Es sollen die Zahlen 0–99 enthalten sein.")

    if ungerade != erwartete_ungerade:
        fehler.append("'ungerade' hat nicht den richtigen Inhalt. Es sollen die ersten 100 ungeraden Zahlen (1, 3, 5, ..., 199) enthalten sein.")

    if not fehler:
        output.success("Beide Listen sind korrekt!")
    else:
        output.wrong("\n".join(fehler))
