import tkinter as tk
from tkinter import messagebox
import platform
import modul_BA

root = tk.Tk()
root.title("Rendszerinfo és Sorsoló - BA")
root.geometry("400x350")

def informacio_lekerese():
    try:
        rendszer_neve = platform.system()
        rendszer_verzio = platform.release()
        gep_nev = platform.node()

        formazott_szoveg = modul_BA.adat_formazas_BA("Operációs rendszer", rendszer_neve)
        
        elemek = ["Python", "Vizsga", "Projekt", "Ötös", "Programozás"]
        sorsolo_objektum = modul_BA.SorsoloOsztaly_BA(elemek)
        kevert_lista = sorsolo_objektum.keveres()
        
        vegleges_uzenet = (
            f"{formazott_szoveg}\n"
            f"Verzió: {rendszer_verzio}\n"
            f"Számítógép neve: {gep_nev}\n\n"
            f"Mai sorsolt kulcsszó: {kevert_lista[0]}"
        )

        lbl_eredmeny.config(text=vegleges_uzenet, fg="blue")

        with open("eredmeny.txt", "w", encoding="utf-8") as f:
            f.write(vegleges_uzenet)
        
        messagebox.showinfo("Siker", "Az adatok mentése az eredmeny.txt fájlba megtörtént!")
        
    except Exception as e:
        messagebox.showerror("Hiba", f"Valami nem sikerült: {e}")

lbl_cim = tk.Label(root, text="Rendszer Információk (BA)", font=("Arial", 14, "bold"))
lbl_cim.pack(pady=10)

lbl_leiras = tk.Label(root, text="Kattints a gombra az adatok lekéréséhez!")
lbl_leiras.pack(pady=5)

btn_start = tk.Button(root, text="Indítás és Mentés", command=informacio_lekerese, bg="lightgray", height=2, width=20)
btn_start.pack(pady=15)

lbl_eredmeny = tk.Label(root, text="", font=("Courier", 10), justify="left")
lbl_eredmeny.pack(pady=10)

btn_kilepes = tk.Button(root, text="Kilépés", command=root.destroy, fg="red")
btn_kilepes.pack(side="bottom", pady=10)

root.mainloop()
