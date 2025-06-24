# model.py
class ZakladEnergetyczny:
    """Model danych dla zakładu energetycznego."""
    _next_id = 1

    def __init__(self, nazwa, latitude, longitude):
        self.id = ZakladEnergetyczny._next_id
        ZakladEnergetyczny._next_id += 1
        self.nazwa = nazwa
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    def __repr__(self):
        return f"<ZakladEnergetyczny id={self.id} nazwa={self.nazwa}>"

class Pracownik:
    """Model danych dla pracownika zakładu energetycznego."""
    _next_id = 1

    def __init__(self, nazwa, latitude, longitude, zaklad):
        self.id = Pracownik._next_id
        Pracownik._next_id += 1
        self.nazwa = nazwa
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.zaklad = zaklad  # referencja do obiektu ZakladEnergetyczny

    def __repr__(self):
        return f"<Pracownik id={self.id} nazwa={self.nazwa} zaklad_id={self.zaklad.id}>"

class Klient:
    """Model danych dla klienta zakładu energetycznego."""
    _next_id = 1

    def __init__(self, nazwa, latitude, longitude, zaklad):
        self.id = Klient._next_id
        Klient._next_id += 1
        self.nazwa = nazwa
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.zaklad = zaklad  # referencja do obiektu ZakladEnergetyczny

    def __repr__(self):
        return f"<Klient id={self.id} nazwa={self.nazwa} zaklad_id={self.zaklad.id}>"

