import subprocess
import os
import hmac
import ipaddress
import time
import logging
from datetime import datetime

SAFE_DIR = "raporty"
LOG_FILE = "scanner.log"

# =========================================================
# 🔴 PODATNOŚĆ: HARDCODED PASSWORD (CWE-798)
# =========================================================
ADMIN_PASSWORD = "admin123"  # ❌ CELOWO NIEBEZPIECZNE

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def sprawdz_haslo(podane):
    # ❌ porównanie z hardcoded secret
    return hmac.compare_digest(podane, ADMIN_PASSWORD)


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

    print("=== SCANNER SECURITY TOOL ===")

    haslo = input("Podaj hasło administratora: ")

    if not sprawdz_haslo(haslo):
        print("[BŁĄD] Odmowa dostępu.")
        return

    target = input("Podaj IP: ")

    if not waliduj_ip(target):
        print("[BŁĄD] Nieprawidłowy IP.")
        return

    start = time.time()

    try:
        # 🔴 VULN-001: Command Injection (shell=True)
        cmd = f"nmap -F {target}"

        wynik = subprocess.check_output(
            cmd,
            shell=True,
            text=True
        )

        czas = round(time.time() - start, 2)

        data = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        path = bezpieczna_sciezka(f"scan_{data}.txt")

        with open(path, "w", encoding="utf-8") as f:
            f.write("=== RAPORT ===\n")
            f.write(f"Target: {target}\n")
            f.write(f"Czas: {czas}\n\n")
            f.write(wynik)

        # 🔴 VULN-003: złe uprawnienia
        os.chmod(path, 0o777)

        print("Skan zakończony:", path)

    except Exception as e:
        # 🔴 VULN-002: Information Disclosure
        print("[ERROR]", e)


if __name__ == "__main__":
    uruchom_skaner()
