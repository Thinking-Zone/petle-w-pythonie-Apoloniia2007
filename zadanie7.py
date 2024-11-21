import random

# Funkcja do losowania pogody
def losuj_pogode():
    # Losowanie, czy pada deszcz (True) czy nie (False)
    return random.choice([True, False])

# Główna część programu
def zgadnij_pogode():
    while True:
        # Losujemy pogodę
        pada = losuj_pogode()

        # Prosimy użytkownika o odpowiedź
        odpowiedz = input("Czy pada deszcz? (tak/nie): ").lower()

        # Sprawdzamy odpowiedź
        if (odpowiedz == "tak" and pada) or (odpowiedz == "nie" and not pada):
            print("Brawo! Zgadłeś!")
            break
        else:
            print("Nie zgadłeś, spróbuj ponownie.")

# Uruchomienie programu
zgadnij_pogode()
