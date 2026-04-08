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


