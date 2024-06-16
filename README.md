# cwiczenia3

# API Endpoint Tester

Skrypt napisany w języku Python, który automatycznie
testuje różne endpointy API przy użyciu narzędzia curl. Skrypt wysyła żądania
HTTP do wybranej publicznej API (w tym przypadku do JSONPlaceholder) i
sprawdza, czy odpowiedzi są poprawne (statusy HTTP i kluczowe elementy w
odpowiedziach JSON takie jak "id", "userId", "title"). Dodatkowo dodany plik Makeflie który zautomatyzuje procesy testowania i
uruchamiania aplikacji.

## Wymagania

- Python 3.x
- curl
- make

## Instalacja

1. Upewnij się, że masz zainstalowanego Pythona i curl na swoim komputerze oraz Git Bash.
2. Pobierz to repo na swój komputer lub pliki "main.py", "aplikacja1.py", "test.py", "requirements.txt"

## Użycie

1. Otwórz skrypt "main.py" w dowolnym interpretrze Pythona i go odpal.
2. Otwórz git busha przejdz do katalogu w którym znajduję się repo z plikami które wcześniej pobierałes i wpisz komendy:
make install
make test
make run


