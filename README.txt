Hallgató neve: Bernscherer Antal
Neptun kód: QLPFEF
Monogram: BA

FELADAT LEÍRÁSA:
A program egy grafikus felülettel (GUI) rendelkező alkalmazás, amely lekéri a felhasználó számítógépének alapvető adatait (operációs rendszer típusa, verziója, gépnév), valamint demonstrál egy egyszerű véletlenszerű sorsolást egy saját osztály segítségével.
A program a kapott eredményeket nemcsak a képernyőn jeleníti meg, hanem fájlkezelés segítségével egy "eredmeny.txt" nevű szöveges fájlba is elmenti.

MODULOK ÉS A MODULOKBAN HASZNÁLT FÜGGVÉNYEK:

1. modul_BA.py (Saját modul):
   - SorsoloOsztaly_BA (osztály): Lista kezelése és keverése.
   - adat_formazas_BA (függvény): Szöveges adatok formázása.

2. main.py (Főprogram):
   - Grafikus felület indítása és vezérlése.
   - Fájlkezelés (írás): open(), write() függvények használata az eredmény mentéséhez.

3. platform (Bemutatandó modul):
   - platform.system(): Operációs rendszer nevének lekérése.
   - platform.release(): Verziószám lekérése.
   - platform.node(): Számítógép hálózati nevének lekérése.

4. tkinter (Tanult modul - GUI):
   - Tk(), Label(), Button(), messagebox: Ablak és vezérlők létrehozása.

5. random (Tanult modul):
   - shuffle(): Lista elemeinek véletlenszerű összekeverése.
