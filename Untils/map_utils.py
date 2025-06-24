# map_utils.py
import tkintermapview  # Uwaga: upewnij się, że pakiet "tkintermapview" jest zainstalowany

# Kolory markerów dla różnych typów obiektów
KOLOR_ZAKLAD_KOLO = "black"
KOLOR_ZAKLAD_OBR  = "gray40"
KOLOR_PRAC_KOLO   = "blue"
KOLOR_PRAC_OBR    = "darkblue"
KOLOR_KLIENT_KOLO = "green"
KOLOR_KLIENT_OBR  = "darkgreen"

def aktualizuj_mape(map_widget, controller, wybrany_zaklad=None, marker_click_callback=None):
    """Zaktualizuj widok mapy, dodając markery dla zakładów, pracowników i klientów."""
    # Usuń istniejące markery z mapy
    map_widget.delete_all_marker()
    # Dodaj markery wszystkich zakładów energetycznych (czarne znaczniki)
    for zaklad in controller.zaklady:
        map_widget.set_marker(zaklad.latitude, zaklad.longitude,
                               text=f"Zakład: {zaklad.nazwa}",
                               marker_color_circle=KOLOR_ZAKLAD_KOLO,
                               marker_color_outside=KOLOR_ZAKLAD_OBR,
                               data=zaklad,
                               command=(lambda m: marker_click_callback(m)) if marker_click_callback else (lambda m: aktualizuj_mape(map_widget, controller, wybrany_zaklad=m.data)))
    # Jeśli nie wybrano konkretnego zakładu (widok globalny) – pokaż wszystkich pracowników
    if wybrany_zaklad is None:
        for prac in controller.pracownicy:
            map_widget.set_marker(prac.latitude, prac.longitude,
                                   text=f"Pracownik: {prac.nazwa}",
                                   marker_color_circle=KOLOR_PRAC_KOLO,
                                   marker_color_outside=KOLOR_PRAC_OBR)
    # Jeśli wybrano konkretny zakład – pokaż TYLKO pracowników i klientów tego zakładu
    else:
        # Markery pracowników wybranego zakładu (niebieskie znaczniki)
        for prac in controller.get_pracownicy_dla_zakladu(wybrany_zaklad):
            map_widget.set_marker(prac.latitude, prac.longitude,
                                   text=f"Pracownik: {prac.nazwa}",
                                   marker_color_circle=KOLOR_PRAC_KOLO,
                                   marker_color_outside=KOLOR_PRAC_OBR)
        # Markery klientów wybranego zakładu (zielone znaczniki)
        for kli in controller.get_klienci_dla_zakladu(wybrany_zaklad):
            map_widget.set_marker(kli.latitude, kli.longitude,
                                   text=f"Klient: {kli.nazwa}",
                                   marker_color_circle=KOLOR_KLIENT_KOLO,
                                   marker_color_outside=KOLOR_KLIENT_OBR)
    # Ustawienie mapy tak, aby objąć wszystkie widoczne punkty (dopasowanie przybliżenia)
    all_latitudes = []
    all_longitudes = []
    # Wszystkie zakłady są zawsze widoczne (dodaj ich współrzędne)
    for z in controller.zaklady:
        all_latitudes.append(z.latitude)
        all_longitudes.append(z.longitude)
    if wybrany_zaklad is None:
        # Widok "Wszystkie": uwzględnij wszystkich pracowników
        for p in controller.pracownicy:
            all_latitudes.append(p.latitude)
            all_longitudes.append(p.longitude)
    else:
        # Widok wybranego zakładu: uwzględnij tylko pracowników i klientów tego zakładu
        for p in controller.get_pracownicy_dla_zakladu(wybrany_zaklad):
            all_latitudes.append(p.latitude)
            all_longitudes.append(p.longitude)
        for k in controller.get_klienci_dla_zakladu(wybrany_zaklad):
            all_latitudes.append(k.latitude)
            all_longitudes.append(k.longitude)
    # Dopasuj przybliżenie i pozycję mapy do zakresu współrzędnych
    if all_latitudes and all_longitudes:
        min_lat = min(all_latitudes); max_lat = max(all_latitudes)
        min_lon = min(all_longitudes); max_lon = max(all_longitudes)
        if min_lat == max_lat and min_lon == max_lon:
            # Tylko jeden punkt na mapie – ustaw stałe przybliżenie
            map_widget.set_position(min_lat, min_lon)
            map_widget.set_zoom(12)
        else:
            map_widget.fit_bounding_box((min_lat, min_lon), (max_lat, max_lon))
