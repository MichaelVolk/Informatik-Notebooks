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
