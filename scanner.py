import subprocess
import os
import hmac
import ipaddress
import time
from datetime import datetime

SAFE_DIR = "raporty"


def sprawdz_haslo(podane):
    poprawne = os.getenv("ADMIN_PASSWORD")
    if poprawne is None:
        print("[BŁĄD] Brak zmiennej środowiskowej ADMIN_PASSWORD.")
        return False
    return hmac.compare_digest(podane, poprawne)


def waliduj_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


def bezpieczna_sciezka(nazwa):
    nazwa = os.path.basename(nazwa)
    return os.path.join(SAFE_DIR, nazwa)


def uruchom_skaner():
    os.makedirs(SAFE_DIR, exist_ok=True)

    print("=== AUTOMATYCZNY SKANER BEZPIECZEŃSTWA ===")

    haslo = input("Wprowadź hasło administratora: ")
    if not sprawdz_haslo(haslo):
        print("[BŁĄD] Odmowa dostępu.")
        return

    target = input("Podaj adres IP do przeskanowania, np. 127.0.0.1: ")

    if not waliduj_ip(target):
        print("[BŁĄD] Nieprawidłowy adres IP.")
        return

    start = time.time()

    try:
        wynik = subprocess.check_output(
            ["nmap", "-F", target],
            text=True
        )

        koniec = time.time()
        czas = round(koniec - start, 2)

        data = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nazwa_pliku = f"scan_report_{data}.txt"
        sciezka = bezpieczna_sciezka(nazwa_pliku)

        with open(sciezka, "w", encoding="utf-8") as plik:
            plik.write("=== RAPORT SKANOWANIA ===\n")
            plik.write(f"Cel skanowania: {target}\n")
            plik.write(f"Czas wykonania skryptu: {czas} s\n\n")
            plik.write(wynik)

        print(f"Skanowanie zakończone.")
        print(f"Czas wykonania: {czas} s")
        print(f"Raport zapisany: {sciezka}")

    except FileNotFoundError:
        print("[BŁĄD] Narzędzie nmap nie jest zainstalowane.")
    except Exception as e:
        print(f"[BŁĄD] Wystąpił problem: {e}")


if __name__ == "__main__":
    uruchom_skaner()
