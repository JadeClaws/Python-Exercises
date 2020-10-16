def zad1():
    for i in range(10):
        print("napis - ", i + 1)        
    return

def zad2():
    for i in range(0, 1001, 50):
        print(i)        
    return

def zad3():
    
    try:
        number = float(input("Podaj liczbe: "))
    except ValueError:
        print("To nie jest liczba")
        return
        
    if (number > 5):
         print("Liczba wieksza od 5")
    else:
         print("Liczba niewieksza od 5")          
    return

def zad4():
    dictDayNames = {1: "Poniedziałek",
                    2: "Wtorek",
                    3: "Środa",
                    4: "Czwartek",
                    5: "Piątek",
                    6: "Sobota",
                    7: "Niedziela"}
    
    try:
        weekDayNo = int(input("Podaj numer dnia tygodnia: "))               
    except ValueError:
        print("Nie podano liczby")
        return
    
    if (weekDayNo in range(1,8)):
        print(dictDayNames.get(weekDayNo))
    else:
        print("Nie ma takiego dnia")           
    return

def zad5():
    try:
        n = int(input("Podaj liczbe całkowitą: "))
        w = 0
        
        for i in range(1, n + 1):
            w += i
            
        print("suma 1 + ... + n (dla n={}) = {}".format(n, w))
    except ValueError:
        print("Nie podano liczby całkowitej")
        return   
    return

def zad6():
    
    while True:
        try:
            n = float(input("Podaj liczbe (4 - koniec): "))
            
            print("Podano liczbe: ", n)
            
            if (n == 4.0):
                print("Przerywam!")
                break
        except ValueError:
            print("To nie jest liczba!")            
    return

def zad7():
    total = 0
    
    while True:
        try:
            n = float(input("Podaj liczbe (0 - koniec): "))
            
            total += n
            
            if (n == 0):
                print("Suma: ", total)
                break
        except:
            print("To nie jest liczba!")    
    return

def zad8():
    listIndices = []
    
    text = input("Podaj tekst: ")
    char = input("Podaj pojedyńczy znak do znalezienia: ")
    
    if (len(char) != 1):
        print("Nie podano pojedyńczego znaku")
        return
    
    for i in range(0, len(text)):
        if (text[i] == char):
            listIndices.append(i + 1)
    
    if (listIndices != []):
        print("Podany znak ({}) znajduje się na pozycjach: {}".format(char, listIndices))
    return

# WYKONANIE

# 1.Napisz program wyswietlajacy 10 razy dowolny napis.
zad1()

# 2.Napisz program wyświetlający liczby od 0 do 1000 co 50 za pomocą jednej 
# pętli for.
zad2()

# 3.Napisz program pobierający liczbę od użytkownika i sprawdzający, czy jest 
# ona większa od 5. Program powinien wyświetlić odpowiedni komunikat.
zad3()

# 4.Napisz program wyświetlający nazwę dnia tygodnia zależnie od liczby 
# wprowadzonej przez użytkownika (1 – poniedziałek ,…, 7 – niedziela, 
# inna – „nie ma takiego dnia”).
zad4()

# 5.Napisz program pobierający od użytkownika liczbę n i wyświetlający wartość 
# sumy 1 + 2 + 3 + … + n.
zad5()

# 6.Napisz program pobierający liczby od użytkownika. Jeżeli zostanie podana 
# liczba 4 to program ma zakończyć swoje działanie.
zad6()

# 7.Napisz program pobierający liczby od użytkownika tak długo, aż zostanie 
# podana liczba 0. Po odczytaniu 0 wyświetl sumę podanych przez użytkownika 
# liczb.
zad7()

# 8.Napisz program pobierający napis oraz znak od użytkownika i sprawdzający, 
# czy w napisie znajduje się podany znak. Jeżeli tak – wyświetl indeksy 
# występowania, jeżeli nie – stosowny komunikat.
zad8()