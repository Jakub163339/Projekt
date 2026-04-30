import subprocess
import os
import hmac
import ipaddress

SAFE_DIR = "raporty"  # FIX#004: ograniczenie zapisu do bezpiecznego katalogu


# FIX#001: usunięcie hardcoded password + bezpieczne porównanie
def sprawdz_haslo(podane):
    poprawne = os.getenv("ADMIN_PASSWORD")
    if poprawne is None:
        print("[BŁĄD] Brak ustawionego hasła w zmiennej środowiskowej ADMIN_PASSWORD!")
        return False
    return hmac.compare_digest(podane, poprawne)


# FIX#002: poprawna walidacja adresu IP
def waliduj_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


# FIX#004: zabezpieczenie przed path traversal
def bezpieczna_sciezka(nazwa):
    nazwa = os.path.basename(nazwa)  # usuwa ../
    return os.path.join(SAFE_DIR, nazwa)


def uruchom_skaner():
    print("=== ZAAWANSOWANY SKANER SIECIOWY v3.0 ===")

    # FIX#004: tworzenie katalogu na raporty
    os.makedirs(SAFE_DIR, exist_ok=True)

    # Logowanie
    haslo = input("Wprowadź hasło administratora: ")
    if not sprawdz_haslo(haslo):
        print("[BŁĄD] Odmowa dostępu.")
        return

    print("Zalogowano pomyślnie.\n")

    # Pobranie IP
    target = input("Podaj adres IP do przeskanowania (np. 127.0.0.1): ")

    if not waliduj_ip(target):
        print("[BŁĄD] Nieprawidłowy adres IP!")
        return

    print(f"Rozpoczynam skanowanie celu: {target}...")

    try:
        # FIX#003: usunięcie shell=True (ochrona przed command injection)
        wynik_skanowania = subprocess.check_output(
            ["nmap", "-F", target],  # argumenty jako lista
            text=True
        )

        # Nazwa pliku
        nazwa_pliku = input("Podaj nazwę dla pliku z raportem (np. raport1.txt): ")
        sciezka = bezpieczna_sciezka(nazwa_pliku)  # FIX#004

        # Zapis raportu
        with open(sciezka, 'w', encoding='utf-8') as plik:
            plik.write("=== RAPORT SKANOWANIA ===\n")
            plik.write(wynik_skanowania)

        print(f"Skanowanie zakończone. Wynik zapisany jako: {sciezka}")

    except FileNotFoundError:
        print("[BŁĄD] Narzędzie 'nmap' nie jest zainstalowane w systemie.")
    except Exception as e:
        print(f"[BŁĄD] Skrypt napotkał problem: {e}")


# Uruchomienie programu
if __name__ == "__main__":
    uruchom_skaner()
