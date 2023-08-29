##Elections scraper
---
####Projekt_3 pro Engeto Python Akademii
---
####POPIS PROJEKTU
---
Úkolem je vytvořit scraper výsledků voleb z roku 2017, který vytáhne data přímo z webu [www.volby.cz](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ). Vybrat libovolnou oblast pro scraper a výstupní soubor pojmenovat dle vlastního uvážení s příponou .csv  

####INSTALACE KNIHOVEN
---
Použité knihovny, které jsou součástí projektu a jsou umístěny v souboru **knihovny_3.txt**. Pro instalaci použitých knihoven je nutné:
1. vytvořit virtuální prostředí
```
python3 -m venv virtual_3
python3 virtual_3\Scripts\activate
```
2. nainstalovat balíčky (např.)
```
pip install requirements
pip install bs4
```
####SPUŠTĚNÍ PROGRAMU
---
Pro spuštění souboru **"volby_rok_2017_3.py"** jsou povinné dva argumenty.
python volby_rok_2017_3.py <"url územního celku"> <"výstupní soubor.csv">
Výstupem je soubor .csv s výsledky voleb

####UKÁZKA PROJEKTU
---
**Výsledky hlasování v okrese Kolín:**
1. argument (url územního celku)... "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2104" 
2. argument (výstupní soubor .csv)... "Kolin.csv"

**Spštění programu:**
python volby_rok_2017_3.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2104" "Kolin.csv"

**Stahování dat:**   
- stahování dat,    
- zápis dat do .csv,   
- vytvoření .csv souboru dle argumentu,   
- ukončení programu
```
Downloading data from: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2104   
Printing file into CSV File!   
Data was saved into file: Kolin.csv.   
Exiting program!
```

**Částečný výstup:**
```
Code,Location,Registered,Envelopers,Valid,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné ---
533173,Barchovice,185,132,132,8,0,0,11,0,14,11,0,0,2,1,0,27,0,0,8,37,0,2,2,0,1,0,1,7,0
533181,Bečváry,822,492,491,41,0,1,32,0,94,48,3,3,3,0,0,34,0,0,10,167,0,3,6,0,2,0,2,41,1
533190,Bělušice,229,123,123,9,0,0,12,0,16,18,0,1,0,0,0,8,0,0,0,46,0,0,1,0,0,0,0,12,0
533211,Břežany I,251,147,147,9,0,0,4,0,34,5,2,4,2,0,0,7,0,0,1,51,0,0,11,0,0,0,0,16,1
```
**Možné chyby:**
Program potřebuje dva argumenty URL a název souboru .csv.   
V případě že jeden z nich bude chybět, nebo nebude správný, program se ukončí!
```
Program need 2 arguments to run: URL and CSV file name. Exiting program!   
```
