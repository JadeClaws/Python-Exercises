def zad1():
    print("downolny napis")
    return

def zad2():
    name = input("Podaj imie: ")
    print("Czesc ", name)
    return

def zad3():
    print("Czesc {}".format(input("Podaj imie: ")))
    return

def zad4():
    text = " To jest tekst "
    
    print("original variable text: \"{}\"".format(text))
    print("len(text): ", len(text))
    print("text.upper(): ", text.upper())
    print("text.lower(): ", text.lower())
    print("text.strip(): ", text.strip())
    print("text.split(\" \"): ", text.split(" "))
    print("text.startswith(\"jest\"): ", text.startswith("jest"))
    print("text.endswith(\"kst \"): ", text.endswith("kst "))
    print("text.count(\"t\"): ", text.count("t"))
    print("text.index(\"t\"): ", text.index("t"))
    print("text[0]: ", text[0])
    print("text[0:5]: ", text[0:5])
    print("\"jest\" in text: ", "jest" in text)
    print("text.replace(\"tekst\", \"napis\"): ", text.replace("tekst", "napis"))
    print("text + 2: ", "<error>") #print(text + 2)
    print("text + str(2): ", text + str(2))
    print("text * 2: ", text * 2)
    return

def zad5():
    listStr = ["napis_1", "string2", "tExT#3", "scriptNo4"]
    print("nowy_napis".join(listStr))
    listStr.append("nowy_napis2")
    print(listStr)
    listStr.remove("string2")
    print(listStr)
    return

def zad6():
    a = "abcd"
    b = 2
    c = 2.3
    
    for i in [a, b, c]:
        print("type({}): ".format(i), type(i))
        print("type(str({})): ".format(i), type(str(i)))
    return

# WYKONANIE:

# 1.Wyswietl dowolny napis
#zad1()

# 2.Pobierz od uzytkownika imie i wyswietl "Czesc <imie>"
#zad2()

# 3.Uzyj metody format dla polecenia z zadania 2
#zad3()

# 4.Stwórz zmienną zawierającą napis " To jest tekst " (spacje zostawiamy!) i
# zinterpretuj wyniki wykonania zadanych poleceń:
zad4()

# 5.Napisz program inicjalizujacy liste napisow i:
# a) wyswietl jej drugi element
# b) sprawdz dzialanie polecen: join(), append(), remove()
#zad5()

# 6.Utworz 3 zmienne, zainicjalizuj wartosciami "abcd", 2, 2.3 i sprawdz wynik
# dzialania type() i type(str())
#zad6()