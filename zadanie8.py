def pytaj_o_pogode():
    liczba_nie = 0  # Licznik odpowiedzi "nie"
    
    while True:
        odpowiedz = input("Czy pada deszcz? (tak/nie/nie wiem): ").lower()
        
        if odpowiedz == "tak":
            print(f"Zakończono. Udzielono {liczba_nie} odpowiedzi 'nie'.")
            break
        elif odpowiedz == "nie":
            liczba_nie += 1
        elif odpowiedz == "nie wiem":
            print("To wyjdź na zewnątrz i się dowiedz.")
        else:
            print("Proszę odpowiedzieć 'tak', 'nie' lub 'nie wiem'.")

# Uruchomienie programu
pytaj_o_pogode()
