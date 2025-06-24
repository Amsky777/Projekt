# controller.py
from model import ZakladEnergetyczny, Pracownik, Klient

class AppController:
    """Kontroler aplikacji obsługujący operacje CRUD na danych modelu."""
    def __init__(self):
        # listy przechowujące obiekty modelu w pamięci
        self.zaklady = []
        self.pracownicy = []
        self.klienci = []

    # --- Operacje na ZakladEnergetyczny ---
    def dodaj_zaklad(self, nazwa, latitude, longitude):
        """Dodaj nowy zakład energetyczny."""
        zaklad = ZakladEnergetyczny(nazwa, latitude, longitude)
        self.zaklady.append(zaklad)
        return zaklad

    def usun_zaklad(self, zaklad_id):
        """Usuń zakład energetyczny o podanym id (usuwa także powiązanych pracowników i klientów)."""
        zaklad = self.szukaj_zaklad_po_id(zaklad_id)
        if zaklad is None:
            return False
        # Usunięcie powiązanych pracowników i klientów tego zakładu
        self.pracownicy = [p for p in self.pracownicy if p.zaklad.id != zaklad_id]
        self.klienci   = [k for k in self.klienci if k.zaklad.id != zaklad_id]
        self.zaklady.remove(zaklad)
        return True

    def aktualizuj_zaklad(self, zaklad_id, new_nazwa, new_lat, new_lon):
        """Zaktualizuj dane istniejącego zakładu energetycznego."""
        zaklad = self.szukaj_zaklad_po_id(zaklad_id)
        if zaklad is None:
            return False
        zaklad.nazwa = new_nazwa
        zaklad.latitude = float(new_lat)
        zaklad.longitude = float(new_lon)
        return True

    def szukaj_zaklad_po_nazwie(self, nazwa):
        """Wyszukaj zakład po nazwie (zwraca pierwszy znaleziony)."""
        for z in self.zaklady:
            if z.nazwa == nazwa:
                return z
        return None

    def szukaj_zaklad_po_id(self, zaklad_id):
        """Wyszukaj zakład po id."""
        for z in self.zaklady:
            if z.id == zaklad_id:
                return z
        return None

    # --- Operacje na Pracownik ---
    def dodaj_pracownika(self, nazwa, latitude, longitude, zaklad):
        """Dodaj nowego pracownika (zakład - obiekt ZakladEnergetyczny)."""
        if zaklad is None:
            return None
        prac = Pracownik(nazwa, latitude, longitude, zaklad)
        self.pracownicy.append(prac)
        return prac

    def usun_pracownika(self, prac_id):
        """Usuń pracownika o podanym id."""
        prac = self.szukaj_pracownik_po_id(prac_id)
        if prac is None:
            return False
        self.pracownicy.remove(prac)
        return True

    def aktualizuj_pracownika(self, prac_id, new_nazwa, new_lat, new_lon, new_zaklad):
        """Zaktualizuj dane pracownika."""
        prac = self.szukaj_pracownik_po_id(prac_id)
        if prac is None:
            return False
        prac.nazwa = new_nazwa
        prac.latitude = float(new_lat)
        prac.longitude = float(new_lon)
        if new_zaklad is not None:
            prac.zaklad = new_zaklad
        return True

    def szukaj_pracownik_po_id(self, prac_id):
        """Wyszukaj pracownika po id."""
        for p in self.pracownicy:
            if p.id == prac_id:
                return p
        return None

    # --- Operacje na Klient ---
    def dodaj_klienta(self, nazwa, latitude, longitude, zaklad):
        """Dodaj nowego klienta (zakład - obiekt ZakladEnergetyczny)."""
        if zaklad is None:
            return None
        kli = Klient(nazwa, latitude, longitude, zaklad)
        self.klienci.append(kli)
        return kli

    def usun_klienta(self, klient_id):
        """Usuń klienta o podanym id."""
        kli = self.szukaj_klient_po_id(klient_id)
        if kli is None:
            return False
        self.klienci.remove(kli)
        return True

    def aktualizuj_klienta(self, klient_id, new_nazwa, new_lat, new_lon, new_zaklad):
        """Zaktualizuj dane klienta."""
        kli = self.szukaj_klient_po_id(klient_id)
        if kli is None:
            return False
        kli.nazwa = new_nazwa
        kli.latitude = float(new_lat)
        kli.longitude = float(new_lon)
        if new_zaklad is not None:
            kli.zaklad = new_zaklad
        return True

    def szukaj_klient_po_id(self, klient_id):
        """Wyszukaj klienta po id."""
        for k in self.klienci:
            if k.id == klient_id:
                return k
        return None

    # --- Funkcje pomocnicze do wyszukiwania powiązanych danych ---
    def get_pracownicy_dla_zakladu(self, zaklad):
        """Zwróć listę pracowników przypisanych do danego zakładu."""
        return [p for p in self.pracownicy if p.zaklad == zaklad]

    def get_klienci_dla_zakladu(self, zaklad):
        """Zwróć listę klientów przypisanych do danego zakładu."""
        return [k for k in self.klienci if k.zaklad == zaklad]

