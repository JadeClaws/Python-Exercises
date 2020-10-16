def jcCodeBreaker():
    print("\n~JC_C0d3br34k3r~")
    code = str(input("insert code: "))
    
    if (len(code) < len(externalCode)):
        print("JCCB: given code is too short")
    
    if (len(code) > len(externalCode)):
        print("JCCB: given code is too long")
        return
    
    extCodeList = list(externalCode)
    codeList    = list(code)
    retInfo = ""
    
    i = 0
    for digit in codeList:
        try:
            idx = extCodeList.index(digit)
            if (idx == i):
                retInfo += "G"
            else:
                retInfo += "Y"
        except:
            retInfo += "R"     
            
        i += 1
    
    print("JCCB: response: ", retInfo)
    
    return retInfo

externalCode = "381592"
tries = 0

while True:
    tries += 1
    ret = jcCodeBreaker()
    
    if (ret == "GGGGGG"):
        print("access granted")
        break
    else:
        print("access denied!")
        
    if (tries >= 5):
        print("device blocked!")
        break