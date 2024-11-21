# Pętla do iteracji po liczbach od 1 do 100
for liczba in range(1, 101):
    if liczba % 7 == 0:  # Sprawdzamy, czy liczba jest podzielna przez 7
        print("Pierwsza liczba podzielna przez 7 to:", liczba)
        break  # Zakończenie pętli po znalezieniu pierwszej liczby podzielnej przez 7
