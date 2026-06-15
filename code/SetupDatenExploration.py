import csv
import os


def _bereinige_zahl(wert):
    if not wert or wert.strip() in ('', '-', 'N/A', 'n/a', 'NA'):
        return None
    bereinigt = wert.strip().replace('$', '').replace(',', '').replace('%', '').strip()
    try:
        return float(bereinigt)
    except ValueError:
        return None


def lade_daten():
    pfad = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'world-data-2023.csv')

    ergebnis = {
        'laender': [],
        'bevoelkerung': [],
        'flaeche': [],
        'dichte': [],
        'bip': [],
        'lebenserwartung': [],
        'geburtenrate': [],
        'co2': [],
        'aerzte': [],
        'saeuglingsterblichkeit': [],
        'fertilitaet': [],
        'stadtbevoelkerung': [],
        'waldflaeche': [],
        'arbeitslosigkeit': [],
        'bildung_hochschule': [],
        'demokatrie':[],
    }

    with open(pfad, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ergebnis['laender'].append(row['Country'].strip())
            ergebnis['bevoelkerung'].append(_bereinige_zahl(row['Population']))
            ergebnis['flaeche'].append(_bereinige_zahl(row['Land Area(Km2)']))
            ergebnis['dichte'].append(_bereinige_zahl(row['Density\n(P/Km2)']))
            ergebnis['bip'].append(_bereinige_zahl(row['GDP']))
            ergebnis['lebenserwartung'].append(_bereinige_zahl(row['Life expectancy']))
            ergebnis['geburtenrate'].append(_bereinige_zahl(row['Birth Rate']))
            ergebnis['co2'].append(_bereinige_zahl(row['Co2-Emissions']))
            ergebnis['aerzte'].append(_bereinige_zahl(row['Physicians per thousand']))
            ergebnis['saeuglingsterblichkeit'].append(_bereinige_zahl(row['Infant mortality']))
            ergebnis['fertilitaet'].append(_bereinige_zahl(row['Fertility Rate']))
            ergebnis['stadtbevoelkerung'].append(_bereinige_zahl(row['Urban_population']))
            ergebnis['waldflaeche'].append(_bereinige_zahl(row['Forested Area (%)']))
            ergebnis['arbeitslosigkeit'].append(_bereinige_zahl(row['Unemployment rate']))
            ergebnis['bildung_hochschule'].append(_bereinige_zahl(row['Gross tertiary education enrollment (%)']))
            ergebnis['demokratie'].append(_bereinige_zahl(row['Democracy']))

    return ergebnis


def filtere(liste1, liste2):
    paare = [(a, b) for a, b in zip(liste1, liste2) if a is not None and b is not None]
    if not paare:
        return [], []
    x, y = zip(*paare)
    return list(x), list(y)
