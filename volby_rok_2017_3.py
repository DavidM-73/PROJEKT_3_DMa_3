"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: David Marek
email: david.32@seznam.cz
discord: David M.#7065
"""
import requests
import sys
from bs4 import BeautifulSoup as bs
import pandas as pd


def analyza_dat(url):
    """
    Popis:
    Tato funkce získává a zpracovává data ze zadaného URL pomocí HTTP GET požadavku.
    Následně vytváří a vrací třídu BeautifulSoup, což je struktura, která umožňuje jednoduché
    vyhledávání a manipulaci s obsahem HTML stránky.

    Parametry:
    - url (str): Adresa URL, ze které se mají data získat a zpracovat.

    Návratová hodnota:
    - soup (BeautifulSoup): Třída BeautifulSoup reprezentující zpracovaná data ze stránky.
    """
    odezva = requests.get(url)
    soup = bs(odezva.content, "html.parser")
    return soup


def nazvy_obci_komplet(soup):
    """
    Popis:
    Tato funkce získává názvy jednotlivých obcí z webové stránky, které jsou označeny pomocí
    určité třídy v HTML struktuře.

    Parametry:
    - soup (BeautifulSoup): Třída BeautifulSoup reprezentující zpracovaná data ze stránky.

    Návratová hodnota:
    - nazvy_obci (list): Seznam názvů obcí, které byly nalezeny na stránce.
    """
    nazvy_obci_komplet = soup.find_all("td", {"class": "overflow_name"})
    nazvy_obci = [nazvy_obci.text for nazvy_obci in nazvy_obci_komplet]
    return nazvy_obci


def mesta_kody(soup):
    """
    Popis:
    Tato funkce získává kódy jednotlivých obcí z webové stránky, které jsou označeny pomocí
    určité třídy v HTML struktuře.

    Parametry:
    - soup (BeautifulSoup): Třída BeautifulSoup reprezentující zpracovaná data ze stránky.

    Návratová hodnota:
    - kody (list): Seznam kódů obcí, které byly nalezeny na stránce.
    """
    mesta_kody = soup.find_all("td", {"class": "cislo"})
    kody_seznam = [kod.text for kod in mesta_kody]
    return kody_seznam


def seznam_stran(url_sub, kody_seznam):
    """
    Popis:
    Tato funkce získává názvy jednotlivých politických stran pro dané obce na webové stránce.

    Parametry:
    - url_sub (str): Podadresa URL, která se použije pro vytvoření kompletní adresy pro konkrétní obec.
    - kody_seznam (list): Seznam kódů obcí.

    Návratová hodnota:
    - strany (list): Seznam názvů politických stran pro dané obce.
    """
    for kod in kody_seznam:
        url = f"{url_sub}{kod}"
        soup = analyza_dat(url)
        strany_soup = soup.find_all("td", {"class": "overflow_name", "headers": ["t1sa1 t1sb2", "t2sa1 t2sb2"]})
        nazvy_stran = [strana.text for strana in strany_soup]
    return nazvy_stran


def souhrn_dat(url_sub, kody_seznam, nazvy_obci, nazvy_stran):
    """
    Popis:
    Tato funkce shromažďuje, třídí a doplňuje všechna data.

    Parametry:
    - url_sub (str): Podadresa URL, která se použije pro vytvoření kompletní adresy pro konkrétní obec.
    - kody_seznam (list): Seznam kódů obcí.
    - nazvy_obci (list): Seznam názvů obcí.
    - nazvy_stran (list): Seznam názvů politických stran.

    Návratová hodnota:
    - data_komplet (dict): Slovník obsahující všechna shromážděná, tříděná a doplněná data.
    """
    registrovany = []
    odevzdane_hlasy = []
    platne_hlasy = []
    hlasy_data = []
    for kod in kody_seznam:
        url = f"{url_sub}{kod}"
        soup = analyza_dat(url)
        registrovany.append(soup.find("td", {"class": "cislo", "headers": "sa2"}).text.replace(" ", "").replace('\xa0', ''))
        odevzdane_hlasy.append(soup.find("td", {"class": "cislo", "headers": "sa3"}).text.replace(" ", "").replace('\xa0', ''))
        platne_hlasy.append(soup.find("td", {"class": "cislo", "headers": "sa6"}).text.replace(" ", "").replace('\xa0', ''))
        hlasy = soup.find_all("td", {"class": "cislo", "headers": ["t1sa2 t1sb3", "t2sa2 t2sb3"]})
        hlasy_ocist = [hlasovani.text.replace(" ", "").replace('\xa0', '') for hlasovani in hlasy]
        hlasy_data.append(hlasy_ocist)
        data_1 = {'Code': kody_seznam, 'Location': nazvy_obci, 'Registered': registrovany, 'Envelopers': odevzdane_hlasy, 'Valid': platne_hlasy}
        data_2 = {a: [hlasy_data[b][c] for b in range(len(hlasy_data)) for c, d in enumerate(nazvy_stran) if d == a] for a in nazvy_stran}
        data_komplet = {**data_1, **data_2}
    return data_komplet


def prevod_do_csv(data_komplet, soubor_csv):
    """
    Popis:
    Tato funkce konvertuje a ukládá data ze slovníku do CSV souboru.

    Parametry:
    - data_komplet (dict): Slovník obsahující kompletní shromážděná a tříděná data.
    - soubor_csv (str): Název výstupního CSV souboru.

    Návratová hodnota:
    - data_soubor (DataFrame): Pandas DataFrame obsahující data pro uložení.
    """
    data_soubor = pd.DataFrame.from_dict(data_komplet)
    print ("Printing file into CSV File! ")
    data_soubor.to_csv(soubor_csv, index=False)
    return data_soubor


def argumenty_spusteni():
    """
    Popis:
    Tato funkce kontroluje, zda jsou zadány platné argumenty pro spuštění programu.

    """
    if len(sys.argv) != 3:
        print(f"Program need 2 arguments to run: URL and CSV file name. Exiting program! ")
        sys.exit()
    if not sys.argv[1].startswith("https://www.volby.cz/pls/ps2017nss/"):
        print(f"First argument  is not correct. Exiting program! ")
        sys.exit()
    if not sys.argv[2].endswith(".csv"):
        print(f"Second argument  is not correct. Exiting program! ")
        sys.exit()
    else:
        print(f"Downloading data from: {sys.argv[1]} ")


def main():
    """
    Popis:
    Hlavní funkce pro spuštění programu. Zde probíhá volání dalších funkcí a zpracování dat.

    """
    argumenty_spusteni()
    soubor_csv = sys.argv[2]
    url = sys.argv[1]
    url_sub = f"https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec="
    soup = analyza_dat(url)
    kody_seznam = mesta_kody(soup)
    nazvy_obci = nazvy_obci_komplet(soup)
    nazvy_stran = seznam_stran(url_sub, kody_seznam)
    data_komplet = souhrn_dat(url_sub, kody_seznam, nazvy_obci, nazvy_stran)
    prevod_do_csv(data_komplet,soubor_csv)
    print(f"Data was saved into file: {soubor_csv}. Exiting program! ")


if __name__ == '__main__':
    main()