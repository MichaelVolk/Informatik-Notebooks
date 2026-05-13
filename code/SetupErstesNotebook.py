import template.output as output


def first_box():
    output.success("Code erfolgreich ausgeführt!")


def second_box(c):
    if c is None:
        output.wrong("Ersetze das None durch einen mathematischen Ausdruck")
        return
    if c == 123123 + 534434:
        output.success("Die Antwort ist richtig!")
    else:
        output.wrong("Das Ergebnis c = " + str(c) + " stimmt nicht.")


def get_werte():
    return 12, 3

def third_box(a,b):
    if a == 3 and b == 12:
        output.success("Du hast die Werte erfolgreich getauscht!")
        return
    if a == 12 and b == 3:
        output.wrong("Du hast die Werte noch nicht getauscht!")
        return
    output.wrong("Die Werte von a und b wurden verändert, aber nicht getauscht.")