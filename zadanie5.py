# Inicjalizacja sumy
suma = 0

# Pętla do iteracji po liczbach od 1 do 100
for liczba in range(1, 101, 2):  # range(1, 101, 2) pozwala na przejście tylko przez liczby nieparzyste
    suma += liczba

# Wyświetlenie wyniku
print("Suma liczb nieparzystych od 1 do 100 wynosi:", suma)
