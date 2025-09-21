import customtkinter
import tkinter
from tkinter import filedialog, messagebox
import tkinter.scrolledtext as st

# --- Funktionen ---
def ende():
    main.destroy()

def speichern():
    ordner = r"C:\Users\kinga\Documents"
    dateipfad = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Textdateien", "*.txt"), ("Alle Dateien", "*.*")],
        title="Datei speichern unter",
        initialdir=ordner
    )
    if dateipfad:  
        text = t.get("1.0", "end-1c").strip()
        with open(dateipfad, "w", encoding="utf-8") as f:
            f.write(text)

def msgyesno():
    antwort = messagebox.askyesno("Ja/nein", "Speichern?")
    if antwort:
        speichern()
        t.delete("1.0", tkinter.END)
    else:
        t.delete("1.0", tkinter.END)

def neu():
    inhalt = t.get("1.0", "end-1c")
    if inhalt.strip():
        msgyesno()
    else:
        t.delete("1.0", tkinter.END)

def laden():
    dateipfad = filedialog.askopenfilename(
        title="Datei öffnen",
        filetypes=[("Textdateien", "*.txt"), ("Alle Dateien", "*.*")],
        initialdir=r"C:\Users\kinga\Documents"
    )
    if dateipfad:  
        with open(dateipfad, "r", encoding="utf-8") as f:
            gelesener_text = f.read()
            t.delete("1.0", tkinter.END)
            t.insert("1.0", gelesener_text)

# --- GUI Setup ---
main = customtkinter.CTk()
main.geometry("800x600")
main.minsize(400, 300)
main.title("Texteditor mit CustomTkinter")
customtkinter.set_appearance_mode("dark")

# --- Menüleiste ---
mBar = tkinter.Menu(main)

mFile = tkinter.Menu(mBar, tearoff=0)
mFile.add_command(label="Neu", command=neu)
mFile.add_command(label="Laden", command=laden)
mFile.add_command(label="Speichern", command=speichern)
mFile.add_separator()
mFile.add_command(label="Beenden", command=ende)

mBar.add_cascade(label="Datei", menu=mFile)
main.config(menu=mBar)

# --- Textbereich mit Scrollbar ---
frame1 = customtkinter.CTkFrame(main)
frame1.pack(fill="both", expand=True, padx=10, pady=10)

t = st.ScrolledText(frame1, width=40, height=15, wrap="word")
t.pack(fill="both", expand=True)

# --- Start ---
main.mainloop()




               