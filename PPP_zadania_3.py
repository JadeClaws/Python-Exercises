def zad1():
    try:
        f = open("PPP_zadania_3_data1.txt")
    except FileNotFoundError:
        print("Nie odnaleziono takiego pliku")
        return
    
    data = f.read()
    print(data)   
    f.close()
    return

def zad2():
    try:
        f = open("PPP_zadania_3_data1.txt")
    except FileNotFoundError:
        print("Nie odnaleziono takiego pliku")
        return
    
    while True:
        line = f.readline()
        if (line == ""):
            break
        print(line)
    f.close()
    return

def zad3():
    data = []
    
    try:
        f = open("PPP_zadania_3_data2.txt")
    except FileNotFoundError:
        print("Nie odnaleziono takiego pliku")
        return
    
    for i in f.read().replace(" ", "").split(";"):
        try:
            data.append(int(i))
        except ValueError:
            print("Nie można skonwertować {} na int".format(i))
    
    print(data)
    f.close()
    return

def zad4():
    try:
        f = open("PPP_zadania_3_data4.txt", "x")
    except FileExistsError:
        f = open("PPP_zadania_3_data4.txt", "w")
        
    f.write("abcd_1234_defg_5678")
    
    f.close()
    return

def zad5():
    fileName = "PPP_zadania_3_data5.txt"
    
    #l = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    l = ["ax1", "bbb2", "cz3", "dt4", "ea5"]
      
    try:
        f = open(fileName, "x")
    except FileExistsError:
        f = open(fileName, "w")
    
    for i in l:
        f.write(str(i)+"\n")
    
    f.close()
    return

def zad6():
    fileNameIn  = "PPP_zadania_3_data6a.txt"
    fileNameOut = "PPP_zadania_3_data6b.txt"
    dataIn = []
    dataOut = []
    
    # read file
    try:
        f = open(fileNameIn)
    except FileNotFoundError:
        print("Nie odnaleziono pliku: {}".format(fileNameIn))
        return
       
    while True:
        line = f.readline()
        
        if (line == ""):
            break
        
        dataIn.append(line)
   
    f.close()

    # prepare output data
    for i in dataIn:
        listTmp = i.strip().replace(" ", "").split(";")
        
        try:
            a = int(listTmp[0])
            b = int(listTmp[1])
        except ValueError:
            dataOut.append("{}; {}; {}".format(listTmp[0], listTmp[1], "niepoprawne_dane"))
            continue
        
        dataOut.append("{}; {}; {}".format(a, b, a ** b))

    # write file
    try:
        f = open(fileNameOut, "x")
    except FileExistsError:
        f = open(fileNameOut, "w")
    
    for i in dataOut:
        f.write(i + "\n")

    f.close()            
    return

def zad7(mode = ""):
    fileName = "PPP_zadania_3_data7.txt"
    targetStr = ""
    resultIdx = []
    
    if (mode == ""):
        print("Okresl tryb wywolania (a, b, c). Przerywam.")
        return
    elif (mode == "a"):
        print("Wyszukiwanie spacji")
        targetStr = " "
    elif (mode == "b"):
        print("Wyszukiwanie zadanego ciągu znaków")
        targetStr = input("Podaj ciąg: ")
    elif (mode == "c"):
        print("Wyszukiwanie znaków przejsć do następnej linii")
        targetStr = "\n"
        
    try:
        f = open(fileName)
    except FileNotFoundError:
        print("Nie odnaleziono pliku: {}".format(fileName))
        return
    
    data = f.read()
    
    pos = 0
    while True:
        tmp = data.find(targetStr, pos)
        
        if (tmp == -1 or tmp == pos):
            break
        
        resultIdx.append(tmp + 1)
        pos = tmp + len(targetStr)
    
    if (len(resultIdx) > 0):
        targetStr = (targetStr, "\\n")[targetStr == "\n"]
        print("Odnaleziono {} \"{}\" na pozycjach {}".format(len(resultIdx), targetStr, resultIdx))
    else:
        print("Nie odnaleziono zadanych wartosci")    
    return

# 1.Napisz program otwierający plik "data1.txt" i wyświetlający jego zawartość.
# 1.Write a program that opens file "data1.txt" and display its content
#zad1()

# 2.Napisz program otwierający plik "data1.txt" i odczytujący z niego dane 
# linia po linii.
# 2.Write a program that opens file "data1.txt" and reads its content line by 
# line
#zad2()

# 3.Napisz program odczytujący plik tekstowy "data2.txt" o podanym formacie:
# 1; 2; 3; 4; 5
# i zapisujący znajdujące się w nim liczby w liście ([1,2,3,4,5]).
# 3.Write a program that reads text file "data2.txt" in given format:
# 1; 2; 3; 4; 5
# and inserts these numbers to the list ([1,2,3,4,5])
#zad3()

# 4.Napisz program zapisujący dowolny ciąg znaków w pliku "data4.txt".
# 4.Write a program that writes any string to file "data4.txt".
#zad4()

# 5.Napisz program zapisujący dowolną listę (napisów, liczb) w pliku 
# "data5.txt", tak aby każdy element był w osobnej linii.
# 5.Write a program that writes any list (strings, ints etc) to a file
# "data5.txt", each element should be in separate line
#zad5()

# 6.Napisz program odczytujący plik tekstowy "data6a.txt" o podanym formacie:
# 5; 2
# 3; 5
# 2; 10
# i przepisz te liczby do pliku "data6b.txt" wraz z wynikiem potęgowania:
# 5; 2; 25
# 3; 5; 243
# 2; 10; 1024
# 6.Write a program that reads text file "data6a.txt" with given format:
# 5; 2
# 3; 5
# 2; 10
# and writes these number into "data6b.txt" including result of power:
# 5; 2; 25
# 3; 5; 243
# 2; 10; 1024
#zad6()

# 7.Napisz program wyszukujący w pliku Dane1.txt tekstowym liczbę:
#a) spacji,
#b) zadanego ciągu znaków,
#c) znaków przejść do następnej linii.
# 7.Write a program that find given substring, space or newline sign in file
zad7("b")