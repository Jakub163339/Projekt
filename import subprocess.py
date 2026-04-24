import subprocess

def uruchom_skaner():
    print("=== ZAAWANSOWANY SKANER SIECIOWY v2.0 ===")
    
    # --- LUKA 1: Zabezpieczenie dostępowe ---
    haslo = input("Wprowadź hasło administratora: ")
    if haslo != "Admin123!":
        print("[BŁĄD] Odmowa dostępu. Złe hasło!")
        return

    print("Zalogowano pomyślnie.\n")
    
    # --- LUKA 2: Walidacja adresu IP ---
    target = input("Podaj adres IP do przeskanowania (np. 127.0.0.1): ")
    
    # "Zabezpieczenie": Skrypt sprawdza, czy wpisano chociaż jedną kropkę
    if "." not in target:
        print("[BŁĄD] Nieprawidłowy format IP! Adres musi zawierać kropki.")
        return

    print(f"Rozpoczynam skanowanie celu: {target}...")

    try:
        # --- LUKA 3: Wykonanie komendy systemowej ---
        # Tworzymy komendę z podanego przez użytkownika tekstu i uruchamiamy w powłoce
        komenda = f"nmap -F {target}"
        wynik_skanowania = subprocess.check_output(komenda, shell=True).decode('utf-8')
        
        # --- LUKA 4: Zapis raportu ---
        nazwa_pliku = input("Podaj nazwę dla pliku z raportem (np. raport1.txt): ")
        
        with open(nazwa_pliku, 'w', encoding='utf-8') as plik:
            plik.write("=== RAPORT SKANOWANIA ===\n")
            plik.write(wynik_skanowania)
            
        print(f"Skanowanie zakończone. Wynik zapisany jako: {nazwa_pliku}")
        
    except Exception as e:
        print(f"[BŁĄD] Skrypt napotkał problem: {e}")

# Uruchomienie głównej funkcji
if __name__ == "__main__":
    uruchom_skaner()