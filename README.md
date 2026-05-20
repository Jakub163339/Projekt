# Projekt Automatyzacja
Praca nad projektem (Zespołowy projekt bezpieczeństwa I)

1. Skład zespołu

Kacper Borowski – Team Leader / DevSecOps
Odpowiedzialny za integrację narzędzi, konfigurację środowiska oraz koordynację projektu

Jakub Paszylka – Security Analyst
Odpowiedzialny za analizę podatności i interpretację wyników skanowania

Jakub Sierawski – Backend Developer
Odpowiedzialny za implementację logiki skanera w Pythonie

Przemysław Najduk – Documentation / QA
Odpowiedzialny za dokumentację, testy oraz przygotowanie raportów

2. Temat projektu
Projekt polega na stworzeniu narzędzia do automatycznego skanowania systemu, sieci lub plików oraz generowania raportu bezpieczeństwa w celu usprawnienia analizy podatności.


3. Plan działania:

  1. Projekt zakłada stworzenie narzędzia w Pythonie i Bashu do automatycznej analizy bezpieczeństwa systemu.

  2. W pierwszym etapie zespół przeprowadzi analizę wymagań oraz wybierze technologie i narzędzia, takie jak Nmap do skanowania sieci oraz grep do filtrowania   wyników. Nastąpi także podział obowiązków.

  3. W drugim etapie  zostanie zaimplementowany główny skrypt w Pythonie, który będzie wywoływał skanowanie przy użyciu Nmap oraz zapisywał wyniki do plików           (JSON/CSV). Równolegle powstaną skrypty Bash automatyzujące proces.

  4. W trzecim etapie  zespół zajmie się przetwarzaniem wyników – parsowaniem danych oraz ich filtrowaniem w celu wyodrębnienia istotnych informacji o               potencjalnych zagrożeniach.

  5. W czwartym etapie  przeprowadzone zostaną testy działania narzędzia oraz poprawki błędów.

  6.W ostatnim etapie  przygotowana zostanie dokumentacja projektu oraz końcowy raport bezpieczeństwa.

  4. Link do repozytorium
  https://github.com/Jakub163339/Projekt.git

  5. Screenshoty środowiska

Część 2

Test: Przeprowadzony test w wyniku którego spradziliśmy skanowanie portów TCP na lokalnym hoscie testowym przy użyciu autorskiego skryptu Python integrującego bibliotekę subprocess i Nmap. 

Wnioski:
Weryfikacja integracji: Skrypt poprawnie inicjuje proces Nmap i bezstratnie przechwytuje strumień danych (stdout), co pozwala na dalszą automatyzację obróbki wyników.
Wydajność: Wykorzystanie flagi -F znacząco skraca czas skanowania, co jest optymalne dla szybkich testów diagnostycznych, ale może pomijać mniej popularne usługi.
Formatowanie danych: Surowy format tekstowy z Nmapa jest trudny do analizy przez inne systemy. Wniosek: W kolejnym kroku należy wdrożyć eksport do formatu JSON.

Część 3: 
Wdrażanie poprawek i ponowne testy (Retest)

W trakcie dalszych prac nad naszym skanerem zrobiliśmy audyt własnego kodu. Zauważyliśmy, że nasz skrypt z części drugiej działał dobrze, ale miał dwie niebezpieczne luki, które pozwalały na przejęcie nad nim kontroli. 

Wykryte błędy w kodzie:
1. Wstrzykiwanie obcych poleceń: Nasz program za bardzo ufał użytkownikowi. Jeśli ktoś zamiast zwykłego adresu IP wpisał złośliwą komendę systemową, skrypt uruchamiał ją w tle bez żadnego sprawdzania.
2. Nadpisywanie plików w systemie: Przy tworzeniu raportu można było wpisać nazwę pliku zawierającą ukośniki. To pozwalało na "wyjście" z folderu projektu i podmianę dowolnego pliku na komputerze.

Co dokładnie naprawiliśmy:
Twarda weryfikacja IP: Dodaliśmy do Pythona wbudowaną bibliotekę "ipaddress". Dzięki temu skrypt najpierw analizuje wpisany tekst i jeśli nie jest to w 100% poprawny adres IP, natychmiast blokuje dalsze działanie.
Czyszczenie nazw plików: Zabezpieczyliśmy proces zapisu raportów. Użyliśmy funkcji ".replace()", która automatycznie filtruje i wycina wszystkie ukośniki z nazwy podanej przez użytkownika. Raport zawsze zapisze się bezpiecznie tam, gdzie powinien.
Zmiana wywołania: Poprawiliśmy sposób, w jaki Python komunikuje się z Nmapem, aby zablokować możliwość przemycania ukrytych komend.

Wyniki ponownych testów:
Po wdrożeniu poprawek przeprowadziliśmy test, próbując celowo "zhakować" nasze narzędzie. Wpisaliśmy złośliwy kod podszywający się pod adres IP. 
Efekt: Skrypt zadziałał bezbłędnie. Od razu wykrył nieprawidłowy format, zablokował próbę ataku i bezpiecznie zamknął program. Luki zostały całkowicie załatane.

Część 4:

Celem projektu było zautomatyzowanie czynności, która wcześniej była wykonywana ręcznie: skanowania hosta za pomocą narzędzia `nmap` oraz zapisywania wyniku do pliku raportu.

Automatyzacja pozwala szybciej wykonać skan, zmniejsza ryzyko błędów użytkownika i zapisuje wynik w uporządkowany sposób.

## Opis działania

Skrypt Python:

1. Sprawdza hasło administratora ze zmiennej środowiskowej `ADMIN_PASSWORD`.
2. Pobiera adres IP do przeskanowania.
3. Waliduje adres IP przy użyciu biblioteki `ipaddress`.
4. Uruchamia skanowanie `nmap -F`.
5. Zapisuje wynik skanowania do katalogu `raporty`.
6. Chroni przed:
   - command injection,
   - hardcoded password,
   - path traversal,
   - błędnymi danymi wejściowymi.

## Wymagania

- Python 3
- Zainstalowany `nmap`
- Ustawiona zmienna środowiskowa `ADMIN_PASSWORD`

## Uruchomienie lokalne

### Linux/macOS

Część 5:

# 1. EXECUTIVE SUMMARY

Celem projektu było przeprowadzenie automatycznego testu bezpieczeństwa systemu
z wykorzystaniem narzędzia skanującego opartego o Nmap oraz Python.

W trakcie analizy wykryto trzy krytyczne podatności:

- CWE-78: OS Command Injection
- CWE-209: Information Disclosure
- CWE-798: Hardcoded Credentials

Ogólny poziom bezpieczeństwa systemu oceniono jako:

**NISKI / WYMAGAJĄCY POPRAWY**

Zidentyfikowane problemy umożliwiają potencjalne:
- wykonanie nieautoryzowanych komend systemowych,
- ujawnienie informacji o błędach systemowych,
- kompromitację danych uwierzytelniających.

---

# 2. ZAKRES I METODOLOGIA

## Zakres testów
- Skanowanie portów TCP
- Identyfikacja usług sieciowych
- Analiza podatności aplikacji skanującej

## Środowisko testowe
- Python 3.x
- System operacyjny: Linux / Windows
- Narzędzie: Nmap

## Użyte narzędzia
- Python subprocess
- Python logging
- Nmap

## Czas trwania testów
- 1–3 sekundy na skan

## Ograniczenia
- Brak skanowania UDP
- Brak testów aplikacyjnych (web exploit)
- Brak brute force / fuzzing

---

# 3. WYKRYTE PODATNOŚCI

---

## VULN-001 — CWE-78: OS Command Injection

### Opis
Aplikacja wykorzystuje `subprocess.check_output()` z `shell=True`,
co umożliwia wykonanie dowolnych poleceń systemowych.

### Kroki reprodukcji
1. Uruchomić aplikację
2. Wprowadzić payload:


### Dowody
Fragment kodu:

``python
subprocess.check_output(cmd, shell=True)


Analiza ryzyka
możliwość wykonania dowolnych komend systemowych
pełna kompromitacja systemu
Rekomendacja
usunąć shell=True
używać listy argumentów:
["nmap", "-F", target]


#VULN-002 — CWE-209: Information Disclosure
Opis

Aplikacja ujawnia szczegóły błędów użytkownikowi końcowemu.

Kroki reprodukcji
wywołać błąd (np. błędne dane wejściowe)
Dowody
print(f"[ERROR] {e}")
Analiza ryzyka
ujawnienie struktury systemu
ułatwienie rekonesansu atakującemu
Rekomendacja
ukryć błędy przed użytkownikiem
logować je tylko do pliku


#VULN-003 — CWE-798: Hardcoded Credentials
Opis

Hasło administratora zapisane jest bezpośrednio w kodzie źródłowym.

Kroki reprodukcji
otworzyć plik źródłowy
ADMIN_PASSWORD = "admin123"
Dowody

Kod źródłowy zawiera jawne hasło.

Analiza ryzyka
każdy z dostępem do kodu zna hasło
pełna kompromitacja uwierzytelnienia
Rekomendacja
przenieść do zmiennych środowiskowych
użyć .env lub systemu sekretów
4. DOWODY TECHNICZNE
Payloady testowe
Command Injection
Logi

Plik:

scanner.log

Przykładowy wpis:

2026-05-20 | INFO | Skan zakończony
Wyniki skanowania

Pliki:
scanner.log

5. PLAN POPRAWEK
Krytyczne poprawki
usunięcie shell=True
przeniesienie haseł do zmiennych środowiskowych
zmiana uprawnień plików na 600
Dodatkowe ulepszenia
walidacja input (whitelist)
lepsze logowanie bezpieczeństwa
szyfrowanie raportów

6. ZAŁĄCZNIKI
Narzędzia użyte w analizie
Nmap
Python logging
subprocess
Narzędzia rekomendowane
Lynis (audyt systemu)
OWASP ZAP (testy aplikacji web)
Nmap (skan sieci)
Pliki wynikowe
scanner.py
scanner.log
raporty/*.txt



