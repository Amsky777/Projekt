# main.py
import tkinter as tk
from tkinter import ttk, messagebox
import Untils.controller as controller
import Untils.map_utils as map_utils
import tkintermapview  # wymagane do korzystania z tkintermapview

# Inicjalizacja głównego okna aplikacji
root = tk.Tk()
root.title("Zarządzanie Zakładami Energetycznymi")
root.geometry("1000x600")

# Utworzenie kontrolera (warstwa logiki)
controller = controller.AppController()

# Utworzenie widgetu z zakładkami (Notebook)
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Tworzenie ramek dla poszczególnych zakładek
tab_zaklady = ttk.Frame(notebook)
tab_pracownicy = ttk.Frame(notebook)
tab_klienci = ttk.Frame(notebook)
tab_mapa = ttk.Frame(notebook)
notebook.add(tab_zaklady, text="Zakłady")
notebook.add(tab_pracownicy, text="Pracownicy")
notebook.add(tab_klienci, text="Klienci")
notebook.add(tab_mapa, text="Mapa")

# Zakładka 1: Lista zakładów energetycznych
zaklad_tree = ttk.Treeview(tab_zaklady, columns=("Nazwa", "Szer.", "Dł."), show='headings')
zaklad_tree.heading("Nazwa", text="Nazwa")
zaklad_tree.heading("Szer.", text="Szer.")
zaklad_tree.heading("Dł.", text="Dł.")
zaklad_tree.column("Nazwa", width=150, stretch=True)
zaklad_tree.column("Szer.", width=80, stretch=False)
zaklad_tree.column("Dł.", width=80, stretch=False)
# Scrollbar pionowy dla listy zakładów
scroll_z = ttk.Scrollbar(tab_zaklady, orient="vertical", command=zaklad_tree.yview)
zaklad_tree.configure(yscrollcommand=scroll_z.set)
# Umieszczenie drzewa i scrollbara
zaklad_tree.grid(row=0, column=0, sticky="nsew")
scroll_z.grid(row=0, column=1, sticky="ns")
# Ramka z przyciskami operacji CRUD dla zakładów
frame_z_buttons = ttk.Frame(tab_zaklady)
frame_z_buttons.grid(row=1, column=0, columnspan=2, pady=5)
btn_add_z = ttk.Button(frame_z_buttons, text="Dodaj")
btn_edit_z = ttk.Button(frame_z_buttons, text="Edytuj")
btn_del_z = ttk.Button(frame_z_buttons, text="Usuń")
btn_add_z.pack(side="left", padx=5)
btn_edit_z.pack(side="left", padx=5)
btn_del_z.pack(side="left", padx=5)
# Ustawienie rozszerzania okna (lista zakładów)
tab_zaklady.rowconfigure(0, weight=1)
tab_zaklady.columnconfigure(0, weight=1)

# Zakładka 2: Lista pracowników
prac_tree = ttk.Treeview(tab_pracownicy, columns=("Zakład", "Nazwa", "Szer.", "Dł."), show='headings')
prac_tree.heading("Zakład", text="Zakład")
prac_tree.heading("Nazwa", text="Nazwa")
prac_tree.heading("Szer.", text="Szer.")
prac_tree.heading("Dł.", text="Dł.")
prac_tree.column("Zakład", width=120, stretch=True)
prac_tree.column("Nazwa", width=120, stretch=True)
prac_tree.column("Szer.", width=80, stretch=False)
prac_tree.column("Dł.", width=80, stretch=False)
scroll_p = ttk.Scrollbar(tab_pracownicy, orient="vertical", command=prac_tree.yview)
prac_tree.configure(yscrollcommand=scroll_p.set)
prac_tree.grid(row=0, column=0, sticky="nsew")
scroll_p.grid(row=0, column=1, sticky="ns")
frame_p_buttons = ttk.Frame(tab_pracownicy)
frame_p_buttons.grid(row=1, column=0, columnspan=2, pady=5)
btn_add_p = ttk.Button(frame_p_buttons, text="Dodaj")
btn_edit_p = ttk.Button(frame_p_buttons, text="Edytuj")
btn_del_p = ttk.Button(frame_p_buttons, text="Usuń")
btn_add_p.pack(side="left", padx=5)
btn_edit_p.pack(side="left", padx=5)
btn_del_p.pack(side="left", padx=5)
tab_pracownicy.rowconfigure(0, weight=1)
tab_pracownicy.columnconfigure(0, weight=1)

# Zakładka 3: Lista klientów
klient_tree = ttk.Treeview(tab_klienci, columns=("Zakład", "Nazwa", "Szer.", "Dł."), show='headings')
klient_tree.heading("Zakład", text="Zakład")
klient_tree.heading("Nazwa", text="Nazwa")
klient_tree.heading("Szer.", text="Szer.")
klient_tree.heading("Dł.", text="Dł.")
klient_tree.column("Zakład", width=120, stretch=True)
klient_tree.column("Nazwa", width=120, stretch=True)
klient_tree.column("Szer.", width=80, stretch=False)
klient_tree.column("Dł.", width=80, stretch=False)
scroll_k = ttk.Scrollbar(tab_klienci, orient="vertical", command=klient_tree.yview)
klient_tree.configure(yscrollcommand=scroll_k.set)
klient_tree.grid(row=0, column=0, sticky="nsew")
scroll_k.grid(row=0, column=1, sticky="ns")
frame_k_buttons = ttk.Frame(tab_klienci)
frame_k_buttons.grid(row=1, column=0, columnspan=2, pady=5)
btn_add_k = ttk.Button(frame_k_buttons, text="Dodaj")
btn_edit_k = ttk.Button(frame_k_buttons, text="Edytuj")
btn_del_k = ttk.Button(frame_k_buttons, text="Usuń")
btn_add_k.pack(side="left", padx=5)
btn_edit_k.pack(side="left", padx=5)
btn_del_k.pack(side="left", padx=5)
tab_klienci.rowconfigure(0, weight=1)
tab_klienci.columnconfigure(0, weight=1)

# Zakładka 4: Interaktywna mapa
frame_map_controls = ttk.Frame(tab_mapa)
frame_map_controls.pack(side="top", fill="x", padx=5, pady=5)
lbl_map = ttk.Label(frame_map_controls, text="Zakład:")
lbl_map.pack(side="left")
zaklad_combobox = ttk.Combobox(frame_map_controls, state="readonly")
zaklad_combobox.pack(side="left", padx=5)
# Ustawienie wartości dla comboboxa zakładów (pierwsza pozycja - "Wszystkie zakłady")
zaklad_combobox['values'] = ["Wszystkie zakłady"] + [z.nazwa for z in controller.zaklady]
zaklad_combobox.current(0)
# Utworzenie widgetu mapy
map_widget = tkintermapview.TkinterMapView(tab_mapa, width=800, height=500, corner_radius=0)
map_widget.pack(fill="both", expand=True)
# (Opcjonalnie) Ustawienie początkowej pozycji mapy:
# map_widget.set_position(52.0, 19.0)  # np. centrum Polski
# map_widget.set_zoom(6)

# Funkcje pomocnicze do aktualizacji widoków list (TreeView)
def odswiez_liste_zaklad():
    """Odśwież listę zakładów w widoku."""
    zaklad_tree.delete(*zaklad_tree.get_children())
    for zaklad in controller.zaklady:
        zaklad_tree.insert("", "end", iid=str(zaklad.id),
                           values=(zaklad.nazwa, zaklad.latitude, zaklad.longitude))

def odswiez_liste_pracownik():
    """Odśwież listę pracowników w widoku."""
    prac_tree.delete(*prac_tree.get_children())
    for prac in controller.pracownicy:
        prac_tree.insert("", "end", iid=str(prac.id),
                         values=(prac.zaklad.nazwa, prac.nazwa, prac.latitude, prac.longitude))

def odswiez_liste_klient():
    """Odśwież listę klientów w widoku."""
    klient_tree.delete(*klient_tree.get_children())
    for kli in controller.klienci:
        klient_tree.insert("", "end", iid=str(kli.id),
                           values=(kli.zaklad.nazwa, kli.nazwa, kli.latitude, kli.longitude))

def aktualizuj_combobox_zaklady():
    """Zaktualizuj listę nazw zakładów w polu wyboru na mapie."""
    zaklad_values = ["Wszystkie zakłady"] + [z.nazwa for z in controller.zaklady]
    zaklad_combobox['values'] = zaklad_values
    # Po zmianie listy resetujemy wybór do "Wszystkie zakłady"
    zaklad_combobox.current(0)

# Funkcje obsługi zdarzeń (dodawanie, edycja, usuwanie)
def open_add_zaklad_window():
    """Otwórz okno dialogowe do dodawania nowego zakładu energetycznego."""
    win = tk.Toplevel(root)
    win.title("Dodaj Zakład Energetyczny")
    ttk.Label(win, text="Nazwa:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    entry_name = ttk.Entry(win)
    entry_name.grid(row=0, column=1, padx=5, pady=5)
    ttk.Label(win, text="Szer. geo:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    entry_lat = ttk.Entry(win)
    entry_lat.grid(row=1, column=1, padx=5, pady=5)
    ttk.Label(win, text="Dł. geo:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    entry_lon = ttk.Entry(win)
    entry_lon.grid(row=2, column=1, padx=5, pady=5)
    def submit_add_z():
        nazwa = entry_name.get().strip()
        lat = entry_lat.get().strip()
        lon = entry_lon.get().strip()
        if not nazwa or not lat or not lon:
            messagebox.showerror("Błąd", "Wszystkie pola muszą być uzupełnione!", parent=win)
            return
        try:
            float(lat); float(lon)
        except ValueError:
            messagebox.showerror("Błąd", "Niepoprawny format współrzędnych!", parent=win)
            return
        controller.dodaj_zaklad(nazwa, lat, lon)
        odswiez_liste_zaklad()
        aktualizuj_combobox_zaklady()
        win.destroy()
    ttk.Button(win, text="OK", command=submit_add_z).grid(row=3, column=0, padx=5, pady=10)
    ttk.Button(win, text="Anuluj", command=win.destroy).grid(row=3, column=1, padx=5, pady=10)

def open_edit_zaklad_window():
    """Otwórz okno dialogowe do edycji wybranego zakładu energetycznego."""
    selekcja = zaklad_tree.selection()
    if not selekcja:
        messagebox.showwarning("Brak wyboru", "Wybierz zakład do edycji.", parent=root)
        return
    zaklad_id = int(selekcja[0])
    zaklad = controller.szukaj_zaklad_po_id(zaklad_id)
    if zaklad is None:
        return
    win = tk.Toplevel(root)
    win.title("Edytuj Zakład Energetyczny")
    ttk.Label(win, text="Nazwa:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    entry_name = ttk.Entry(win)
    entry_name.grid(row=0, column=1, padx=5, pady=5)
    entry_name.insert(0, zaklad.nazwa)
    ttk.Label(win, text="Szer. geo:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    entry_lat = ttk.Entry(win)
    entry_lat.grid(row=1, column=1, padx=5, pady=5)
    entry_lat.insert(0, zaklad.latitude)
    ttk.Label(win, text="Dł. geo:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    entry_lon = ttk.Entry(win)
    entry_lon.grid(row=2, column=1, padx=5, pady=5)
    entry_lon.insert(0, zaklad.longitude)
    def submit_edit_z():
        nazwa = entry_name.get().strip()
        lat = entry_lat.get().strip()
        lon = entry_lon.get().strip()
        if not nazwa or not lat or not lon:
            messagebox.showerror("Błąd", "Wszystkie pola muszą być uzupełnione!", parent=win)
            return
        try:
            float(lat); float(lon)
        except ValueError:
            messagebox.showerror("Błąd", "Niepoprawny format współrzędnych!", parent=win)
            return
        controller.aktualizuj_zaklad(zaklad_id, nazwa, lat, lon)
        odswiez_liste_zaklad()
        odswiez_liste_pracownik()  # aktualizacja nazw zakładów przy pracownikach
        odswiez_liste_klient()     # aktualizacja nazw zakładów przy klientach
        aktualizuj_combobox_zaklady()
        win.destroy()
    ttk.Button(win, text="Zapisz", command=submit_edit_z).grid(row=3, column=0, padx=5, pady=10)
    ttk.Button(win, text="Anuluj", command=win.destroy).grid(row=3, column=1, padx=5, pady=10)

def delete_zaklad():
    """Usuń zaznaczony zakład energetyczny."""
    selekcja = zaklad_tree.selection()
    if not selekcja:
        messagebox.showwarning("Brak wyboru", "Wybierz zakład do usunięcia.", parent=root)
        return
    zaklad_id = int(selekcja[0])
    zaklad = controller.szukaj_zaklad_po_id(zaklad_id)
    if zaklad is None:
        return
    # Potwierdzenie usunięcia
    confirm = messagebox.askyesno("Potwierdzenie",
                                  f"Czy na pewno usunąć zakład '{zaklad.nazwa}'?\n"
                                  "Spowoduje to usunięcie powiązanych pracowników i klientów.",
                                  parent=root)
    if not confirm:
        return
    controller.usun_zaklad(zaklad_id)
    odswiez_liste_zaklad()
    odswiez_liste_pracownik()
    odswiez_liste_klient()
    aktualizuj_combobox_zaklady()

def open_add_pracownik_window():
    """Otwórz okno dialogowe do dodawania nowego pracownika."""
    if not controller.zaklady:
        messagebox.showerror("Brak zakładów", "Najpierw dodaj zakład energetyczny.", parent=root)
        return
    win = tk.Toplevel(root)
    win.title("Dodaj Pracownika")
    ttk.Label(win, text="Imię:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    entry_name = ttk.Entry(win)
    entry_name.grid(row=0, column=1, padx=5, pady=5)
    ttk.Label(win, text="Zakład:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    cb_zaklad = ttk.Combobox(win, state="readonly")
    zaklad_names = [z.nazwa for z in controller.zaklady]
    cb_zaklad['values'] = zaklad_names
    cb_zaklad.current(0)
    cb_zaklad.grid(row=1, column=1, padx=5, pady=5)
    ttk.Label(win, text="Szer. geo:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    entry_lat = ttk.Entry(win)
    entry_lat.grid(row=2, column=1, padx=5, pady=5)
    ttk.Label(win, text="Dł. geo:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
    entry_lon = ttk.Entry(win)
    entry_lon.grid(row=3, column=1, padx=5, pady=5)
    def submit_add_p():
        nazwa = entry_name.get().strip()
        lat = entry_lat.get().strip()
        lon = entry_lon.get().strip()
        zaklad_name = cb_zaklad.get()
        if not nazwa or not lat or not lon or not zaklad_name:
            messagebox.showerror("Błąd", "Wszystkie pola muszą być uzupełnione!", parent=win)
            return
        try:
            float(lat); float(lon)
        except ValueError:
            messagebox.showerror("Błąd", "Niepoprawny format współrzędnych!", parent=win)
            return
        zaklad_obj = controller.szukaj_zaklad_po_nazwie(zaklad_name)
        if zaklad_obj is None:
            messagebox.showerror("Błąd", "Wybrany zakład nie istnieje.", parent=win)
            return
        controller.dodaj_pracownika(nazwa, lat, lon, zaklad_obj)
        odswiez_liste_pracownik()
        win.destroy()
    ttk.Button(win, text="OK", command=submit_add_p).grid(row=4, column=0, padx=5, pady=10)
    ttk.Button(win, text="Anuluj", command=win.destroy).grid(row=4, column=1, padx=5, pady=10)

def open_edit_pracownik_window():
    """Otwórz okno dialogowe do edycji wybranego pracownika."""
    selekcja = prac_tree.selection()
    if not selekcja:
        messagebox.showwarning("Brak wyboru", "Wybierz pracownika do edycji.", parent=root)
        return
    prac_id = int(selekcja[0])
    prac = controller.szukaj_pracownik_po_id(prac_id)
    if prac is None:
        return
    win = tk.Toplevel(root)
    win.title("Edytuj Pracownika")
    ttk.Label(win, text="Imię:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    entry_name = ttk.Entry(win)
    entry_name.grid(row=0, column=1, padx=5, pady=5)
    entry_name.insert(0, prac.nazwa)
    ttk.Label(win, text="Zakład:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    cb_zaklad = ttk.Combobox(win, state="readonly")
    zaklad_names = [z.nazwa for z in controller.zaklady]
    cb_zaklad['values'] = zaklad_names
    try:
        current_index = zaklad_names.index(prac.zaklad.nazwa)
    except ValueError:
        current_index = 0
    cb_zaklad.current(current_index)
    cb_zaklad.grid(row=1, column=1, padx=5, pady=5)
    ttk.Label(win, text="Szer. geo:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    entry_lat = ttk.Entry(win)
    entry_lat.grid(row=2, column=1, padx=5, pady=5)
    entry_lat.insert(0, prac.latitude)
    ttk.Label(win, text="Dł. geo:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
    entry_lon = ttk.Entry(win)
    entry_lon.grid(row=3, column=1, padx=5, pady=5)
    entry_lon.insert(0, prac.longitude)
    def submit_edit_p():
        nazwa = entry_name.get().strip()
        lat = entry_lat.get().strip()
        lon = entry_lon.get().strip()
        zaklad_name = cb_zaklad.get()
        if not nazwa or not lat or not lon or not zaklad_name:
            messagebox.showerror("Błąd", "Wszystkie pola muszą być uzupełnione!", parent=win)
            return
        try:
            float(lat); float(lon)
        except ValueError:
            messagebox.showerror("Błąd", "Niepoprawny format współrzędnych!", parent=win)
            return
        zaklad_obj = controller.szukaj_zaklad_po_nazwie(zaklad_name)
        if zaklad_obj is None:
            messagebox.showerror("Błąd", "Wybrany zakład nie istnieje.", parent=win)
            return
        controller.aktualizuj_pracownika(prac_id, nazwa, lat, lon, zaklad_obj)
        odswiez_liste_pracownik()
        win.destroy()
    ttk.Button(win, text="Zapisz", command=submit_edit_p).grid(row=4, column=0, padx=5, pady=10)
    ttk.Button(win, text="Anuluj", command=win.destroy).grid(row=4, column=1, padx=5, pady=10)

def delete_pracownik():
    """Usuń zaznaczonego pracownika."""
    selekcja = prac_tree.selection()
    if not selekcja:
        messagebox.showwarning("Brak wyboru", "Wybierz pracownika do usunięcia.", parent=root)
        return
    prac_id = int(selekcja[0])
    prac = controller.szukaj_pracownik_po_id(prac_id)
    if prac is None:
        return
    confirm = messagebox.askyesno("Potwierdzenie",
                                  f"Czy na pewno usunąć pracownika '{prac.nazwa}'?",
                                  parent=root)
    if not confirm:
        return
    controller.usun_pracownika(prac_id)
    odswiez_liste_pracownik()

def open_add_klient_window():
    """Otwórz okno dialogowe do dodawania nowego klienta."""
    if not controller.zaklady:
        messagebox.showerror("Brak zakładów", "Najpierw dodaj zakład energetyczny.", parent=root)
        return
    win = tk.Toplevel(root)
    win.title("Dodaj Klienta")
    ttk.Label(win, text="Nazwa:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    entry_name = ttk.Entry(win)
    entry_name.grid(row=0, column=1, padx=5, pady=5)
    ttk.Label(win, text="Zakład:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    cb_zaklad = ttk.Combobox(win, state="readonly")
    zaklad_names = [z.nazwa for z in controller.zaklady]
    cb_zaklad['values'] = zaklad_names
    cb_zaklad.current(0)
    cb_zaklad.grid(row=1, column=1, padx=5, pady=5)
    ttk.Label(win, text="Szer. geo:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    entry_lat = ttk.Entry(win)
    entry_lat.grid(row=2, column=1, padx=5, pady=5)
    ttk.Label(win, text="Dł. geo:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
    entry_lon = ttk.Entry(win)
    entry_lon.grid(row=3, column=1, padx=5, pady=5)
    def submit_add_k():
        nazwa = entry_name.get().strip()
        lat = entry_lat.get().strip()
        lon = entry_lon.get().strip()
        zaklad_name = cb_zaklad.get()
        if not nazwa or not lat or not lon or not zaklad_name:
            messagebox.showerror("Błąd", "Wszystkie pola muszą być uzupełnione!", parent=win)
            return
        try:
            float(lat); float(lon)
        except ValueError:
            messagebox.showerror("Błąd", "Niepoprawny format współrzędnych!", parent=win)
            return
        zaklad_obj = controller.szukaj_zaklad_po_nazwie(zaklad_name)
        if zaklad_obj is None:
            messagebox.showerror("Błąd", "Wybrany zakład nie istnieje.", parent=win)
            return
        controller.dodaj_klienta(nazwa, lat, lon, zaklad_obj)
        odswiez_liste_klient()
        win.destroy()
    ttk.Button(win, text="OK", command=submit_add_k).grid(row=4, column=0, padx=5, pady=10)
    ttk.Button(win, text="Anuluj", command=win.destroy).grid(row=4, column=1, padx=5, pady=10)

def open_edit_klient_window():
    """Otwórz okno dialogowe do edycji wybranego klienta."""
    selekcja = klient_tree.selection()
    if not selekcja:
        messagebox.showwarning("Brak wyboru", "Wybierz klienta do edycji.", parent=root)
        return
    kli_id = int(selekcja[0])
    kli = controller.szukaj_klient_po_id(kli_id)
    if kli is None:
        return
    win = tk.Toplevel(root)
    win.title("Edytuj Klienta")
    ttk.Label(win, text="Nazwa:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    entry_name = ttk.Entry(win)
    entry_name.grid(row=0, column=1, padx=5, pady=5)
    entry_name.insert(0, kli.nazwa)
    ttk.Label(win, text="Zakład:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    cb_zaklad = ttk.Combobox(win, state="readonly")
    zaklad_names = [z.nazwa for z in controller.zaklady]
    cb_zaklad['values'] = zaklad_names
    try:
        current_index = zaklad_names.index(kli.zaklad.nazwa)
    except ValueError:
        current_index = 0
    cb_zaklad.current(current_index)
    cb_zaklad.grid(row=1, column=1, padx=5, pady=5)
    ttk.Label(win, text="Szer. geo:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    entry_lat = ttk.Entry(win)
    entry_lat.grid(row=2, column=1, padx=5, pady=5)
    entry_lat.insert(0, kli.latitude)
    ttk.Label(win, text="Dł. geo:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
    entry_lon = ttk.Entry(win)
    entry_lon.grid(row=3, column=1, padx=5, pady=5)
    entry_lon.insert(0, kli.longitude)
    def submit_edit_k():
        nazwa = entry_name.get().strip()
        lat = entry_lat.get().strip()
        lon = entry_lon.get().strip()
        zaklad_name = cb_zaklad.get()
        if not nazwa or not lat or not lon or not zaklad_name:
            messagebox.showerror("Błąd", "Wszystkie pola muszą być uzupełnione!", parent=win)
            return
        try:
            float(lat); float(lon)
        except ValueError:
            messagebox.showerror("Błąd", "Niepoprawny format współrzędnych!", parent=win)
            return
        zaklad_obj = controller.szukaj_zaklad_po_nazwie(zaklad_name)
        if zaklad_obj is None:
            messagebox.showerror("Błąd", "Wybrany zakład nie istnieje.", parent=win)
            return
        controller.aktualizuj_klienta(kli_id, nazwa, lat, lon, zaklad_obj)
        odswiez_liste_klient()
        win.destroy()
    ttk.Button(win, text="Zapisz", command=submit_edit_k).grid(row=4, column=0, padx=5, pady=10)
    ttk.Button(win, text="Anuluj", command=win.destroy).grid(row=4, column=1, padx=5, pady=10)

def delete_klient():
    """Usuń zaznaczonego klienta."""
    selekcja = klient_tree.selection()
    if not selekcja:
        messagebox.showwarning("Brak wyboru", "Wybierz klienta do usunięcia.", parent=root)
        return
    kli_id = int(selekcja[0])
    kli = controller.szukaj_klient_po_id(kli_id)
    if kli is None:
        return
    confirm = messagebox.askyesno("Potwierdzenie",
                                  f"Czy na pewno usunąć klienta '{kli.nazwa}'?",
                                  parent=root)
    if not confirm:
        return
    controller.usun_klienta(kli_id)
    odswiez_liste_klient()

# Przypisanie funkcji do przycisków po zdefiniowaniu funkcji
btn_add_z.config(command=open_add_zaklad_window)
btn_edit_z.config(command=open_edit_zaklad_window)
btn_del_z.config(command=delete_zaklad)
btn_add_p.config(command=open_add_pracownik_window)
btn_edit_p.config(command=open_edit_pracownik_window)
btn_del_p.config(command=delete_pracownik)
btn_add_k.config(command=open_add_klient_window)
btn_edit_k.config(command=open_edit_klient_window)
btn_del_k.config(command=delete_klient)

# Obsługa interakcji na mapie
def on_marker_click(marker):
    """Obsługa kliknięcia w znacznik zakładu na mapie."""
    zaklad = marker.data
    # Ustaw wybór comboboxa na kliknięty zakład
    zaklad_combobox.set(zaklad.nazwa)
    # Aktualizuj mapę, pokazując dane wybranego zakładu
    map_utils.aktualizuj_mape(map_widget, controller, wybrany_zaklad=zaklad, marker_click_callback=on_marker_click)

def on_combobox_select(event):
    """Zmiana wyboru zakładu w comboboxie na mapie."""
    wybor = zaklad_combobox.get()
    if wybor == "Wszystkie zakłady":
        map_utils.aktualizuj_mape(map_widget, controller, wybrany_zaklad=None, marker_click_callback=on_marker_click)
    else:
        zaklad_obj = controller.szukaj_zaklad_po_nazwie(wybor)
        if zaklad_obj:
            map_utils.aktualizuj_mape(map_widget, controller, wybrany_zaklad=zaklad_obj, marker_click_callback=on_marker_click)

def on_tab_change(event):
    """Obsługa zmiany zakładki - odświeżenie mapy przy przejściu na zakładkę mapy."""
    if notebook.index("current") == 3:  # indeks 3 = zakładka "Mapa"
        on_combobox_select(None)

zaklad_combobox.bind("<<ComboboxSelected>>", on_combobox_select)
notebook.bind("<<NotebookTabChanged>>", on_tab_change)

# Początkowe odświeżenie list (gdy brak danych początkowych listy będą puste)
odswiez_liste_zaklad()
odswiez_liste_pracownik()
odswiez_liste_klient()

# Uruchomienie głównej pętli aplikacji
root.mainloop()

