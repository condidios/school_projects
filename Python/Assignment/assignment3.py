import sys
f=open(sys.argv[1],"r")
commands=[[line.split()] for line in f.readlines()]
f.close()
whitepieces = ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "b1", "b2", "n1", "n2", "r1", "r2", "qu", "ki", "KI"]
blackpieces = ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "B1", "B2", "N1", "N2", "R2", "R1", "QU", "KI", "ki"]
whitepawns = ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"]
blackpawns = ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"]
whiteelephants = ["b1", "b2"]
blackelephants = ["B1", "B2"]
whitehorses = ["n1", "n2"]
blackhorses = ["N1", "N2"]
whitecastles = ["r1", "r2"]
blackcastles = ["R2", "R1"]
whitequeen = ["qu"]
blackqueen = ["QU"]
whiteking = ["ki"]
blackking = ["KI"]
coords = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
reverseCoords = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5 : "f", 6: "g", 7: "h"}
board = [["R1", "N1" ,"B1", "QU", "KI", "B2", "N2", "R2"],
         ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"],
         ["r1", "n1", "b1", "qu", "ki", "b2", "n2", "r2"]]
index = 0
def findIndex(x):
    global board
    global coords
    global linecounter
    linecounter = 0
    global index
    for i in board:
        if x in i:
            index = i.index(x)
            break
        else:
            linecounter += 1
    return index, linecounter
def initialize():
    print("> initialize")
    print("OK")
    print("-----------------------")
    global board
    board = [["R1", "N1" ,"B1", "QU", "KI", "B2", "N2", "R2"],
             ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"],
             ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
             ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
             ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
             ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
             ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"],
             ["r1", "n1", "b1", "qu", "ki", "b2", "n2", "r2"]]
    for x in board:
        print(*x)
    print("-----------------------")
def appendCoord(x,y):
    global t
    k = reverseCoords[y]+str(8-x)
    t.append(k)
def sagduz(x):
    global t
    global board
    global whitepieces
    global blackpieces
    sutun, satir = findIndex(x)
    while sutun < 7:
        if x in whitepieces:
            if board[satir][sutun+1] in whitepieces:
                break
            elif board[satir][sutun+1] in blackpieces:
                appendCoord(satir,sutun+1)
                break
            elif board[satir][sutun+1] == "  ":
                appendCoord(satir,sutun+1)
                sutun += 1
        elif x in blackpieces:
            if board[satir][sutun+1] in blackpieces:
                break
            elif board[satir][sutun+1] in whitepieces:
                appendCoord(satir,sutun+1)
                break
            elif board[satir][sutun+1] == "  ":
                appendCoord(satir,sutun+1)
                sutun += 1
def solduz(x):
    global t
    global board
    global whitepieces
    global blackpieces
    sutun, satir = findIndex(x)
    while sutun > 0:
        if x in whitepieces:
            if board[satir][sutun-1] in whitepieces:
                break
            elif board[satir][sutun-1] in blackpieces:
                appendCoord(satir,sutun-1)
                break
            elif board[satir][sutun-1] == "  ":
                appendCoord(satir,sutun-1)
                sutun -= 1
        elif x in blackpieces:
            if board[satir][sutun-1] in blackpieces:
                break
            elif board[satir][sutun-1] in whitepieces:
                appendCoord(satir,sutun-1)
                break
            elif board[satir][sutun-1] == "  ":
                appendCoord(satir,sutun-1)
                sutun -= 1
def ust(x):
    global t
    global board
    global whitepieces
    global blackpieces
    sutun, satir = findIndex(x)
    while satir > 0:
        if x in whitepieces:
            if board[satir-1][sutun] in whitepieces:
                break
            elif board[satir-1][sutun] in blackpieces:
                appendCoord(satir-1,sutun)
                break
            elif board[satir-1][sutun] == "  ":
                appendCoord(satir-1,sutun)
                satir -= 1
        elif x in blackpieces:
            if board[satir-1][sutun] in blackpieces:
                break
            elif board[satir-1][sutun] in whitepieces:
                appendCoord(satir-1,sutun)
                break
            elif board[satir-1][sutun] == "  ":
                appendCoord(satir-1,sutun)
                satir -= 1
def alt(x):
    global t
    global board
    global whitepieces
    global blackpieces
    sutun, satir = findIndex(x)
    while satir < 7:
        if x in whitepieces:
            if board[satir+1][sutun] in whitepieces:
                break
            elif board[satir+1][sutun] in blackpieces:
                appendCoord(satir+1,sutun)
                break
            elif board[satir+1][sutun] == "  ":
                appendCoord(satir+1,sutun)
                satir += 1
        elif x in blackpieces:
            if board[satir+1][sutun] in blackpieces:
                break
            elif board[satir+1][sutun] in whitepieces:
                appendCoord(satir+1,sutun)
                break
            elif board[satir+1][sutun] == "  ":
                appendCoord(satir+1,sutun)
                satir += 1
def solUst(x):
    global t
    global board
    global whitepieces
    global blackpieces
    sutun, satir = findIndex(x)
    while satir > 0 and sutun > 0:
        if x in whitepieces:
            if board[satir-1][sutun-1] in whitepieces:
                break
            elif board[satir-1][sutun-1] in blackpieces:
                appendCoord(satir-1,sutun-1)
                break
            elif board[satir-1][sutun-1] == "  ":
                appendCoord(satir-1,sutun-1)
                satir -= 1
                sutun -= 1
        elif x in blackpieces:
            if board[satir-1][sutun-1] in blackpieces:
                break
            elif board[satir-1][sutun-1] in whitepieces:
                appendCoord(satir-1,sutun-1)
                break
            elif board[satir-1][sutun-1] == "  ":
                appendCoord(satir-1,sutun-1)
                satir -= 1
                sutun -= 1
def solAlt(x):
    global t
    global board
    global whitepieces
    global blackpieces
    sutun, satir = findIndex(x)
    while satir < 7 and sutun > 0:
        if x in whitepieces:
            if board[satir+1][sutun-1] in whitepieces:
                break
            elif board[satir+1][sutun-1] in blackpieces:
                appendCoord(satir+1,sutun-1)
                break
            elif board[satir+1][sutun-1] == "  ":
                appendCoord(satir+1,sutun-1)
                satir += 1
                sutun -= 1
        elif x in blackpieces:
            if board[satir+1][sutun-1] in blackpieces:
                break
            elif board[satir+1][sutun-1] in whitepieces:
                appendCoord(satir+1,sutun-1)
                break
            elif board[satir+1][sutun-1] == "  ":
                appendCoord(satir+1,sutun-1)
                satir += 1
                sutun -= 1
def sagUst(x):
    global t
    global board
    global whitepieces
    global blackpieces
    sutun, satir = findIndex(x)
    while satir > 0 and sutun < 7:
        if x in whitepieces:
            if board[satir-1][sutun+1] in whitepieces:
                break
            elif board[satir-1][sutun+1] in blackpieces:
                appendCoord(satir-1,sutun+1)
                break
            elif board[satir-1][sutun+1] == "  ":
                appendCoord(satir-1,sutun+1)
                satir -= 1
                sutun += 1
        elif x in blackpieces:
            if board[satir-1][sutun+1] in blackpieces:
                break
            elif board[satir-1][sutun+1] in whitepieces:
                appendCoord(satir-1,sutun+1)
                break
            elif board[satir-1][sutun-1] == "  ":
                appendCoord(satir-1,sutun+1)
                satir -= 1
                sutun += 1
def sagAlt(x):
    global t
    global board
    global whitepieces
    global blackpieces
    sutun, satir = findIndex(x)
    while satir < 7 and sutun < 7:
        if x in whitepieces:
            if board[satir+1][sutun+1] in whitepieces:
                break
            elif board[satir+1][sutun+1] in blackpieces:
                appendCoord(satir+1,sutun+1)
                break
            elif board[satir+1][sutun+1] == "  ":
                appendCoord(satir+1,sutun+1)
                satir += 1
                sutun += 1
        elif x in blackpieces:
            if board[satir+1][sutun+1] in blackpieces:
                break
            elif board[satir+1][sutun+1] in whitepieces:
                appendCoord(satir+1,sutun+1)
                break
            elif board[satir+1][sutun+1] == "  ":
                appendCoord(satir+1,sutun+1)
                satir += 1
                sutun += 1

def showMoves2(x):
    global whitepieces
    global blackpieces
    global board
    global whitecastles
    global whiteelephants
    global whitehorses
    global whiteking
    global whitepawns
    global whitequeen
    global blackpawns
    global blackcastles
    global blackelephants
    global blackking
    global blackhorses
    global blackqueen
    global coords
    global reverseCoords
    global t
    t=[]
    sutun, satir = findIndex(x)
    if x in whitepawns:
        if board[satir-1][sutun] == "  " or board[satir-1][sutun] in blackpieces:
            t.append(reverseCoords[sutun] + str(9-satir))
    if x in blackpawns:
        if board[satir+1][sutun] == "  " or board[satir+1][sutun] in whitepieces:
            t.append(reverseCoords[sutun] + str(9-satir))
    if x in blackcastles or x in whitecastles:
        ust(x)
        alt(x)
        sagduz(x)
        solduz(x)
    if x in whitequeen or x in blackqueen:
        ust(x)
        alt(x)
        sagduz(x)
        solduz(x)
        sagAlt(x)
        sagUst(x)
        solAlt(x)
        solUst(x)
    if x in whiteelephants:
        solUst(x)
        sagUst(x)
    if x in blackelephants:
        solAlt(x)
        sagAlt(x)
    if x in whiteking:
        g = [(satir+1,sutun+1), (satir+1,sutun),(satir+1,sutun-1),(satir,sutun+1),(satir,sutun-1),(satir-1,sutun+1),(satir-1,sutun),(satir-1,sutun-1)]
        for i in g:
            if inBoard(i[0],i[1]) == True and board[i[0]][i[1]] not in whitepieces:
                t.append(reverseCoords[i[1]] + str(8-i[0]))
    if x in blackking:
        g = [(satir+1,sutun+1), (satir+1,sutun),(satir+1,sutun-1),(satir,sutun+1),(satir,sutun-1),(satir-1,sutun+1),(satir-1,sutun),(satir-1,sutun-1)]
        for i in g:
            if inBoard(i[0],i[1]) == True and board[i[0]][i[1]] not in blackpieces:
                t.append(reverseCoords[i[1]] + str(8-i[0]))
    if x in whitehorses:
        g = [(satir+1,sutun+2), (satir+1,sutun-2),(satir+2,sutun-1),(satir+2,sutun+1),(satir-1,sutun-2),(satir-1,sutun+2),(satir-2,sutun+1),(satir-2,sutun-1)]
        h = [(satir+1,sutun+1),(satir+1,sutun-1),(satir-1,sutun+1),(satir-1,sutun-1)]
        for i in g:
            if inBoard(i[0],i[1]) == True and board[i[0]][i[1]] not in whitepieces:
                t.append(reverseCoords[i[1]] + str(8-i[0]))
        for i in h:
            if inBoard(i[0],i[1]) == True and board[i[0]][i[1]] not in whitepieces:
                t.append(reverseCoords[i[1]] + str(8-i[0]))
    if x in blackhorses:
        g = [(satir+1,sutun+2), (satir+1,sutun-2),(satir+2,sutun-1),(satir+2,sutun+1),(satir-1,sutun-2),(satir-1,sutun+2),(satir-2,sutun+1),(satir-2,sutun-1)]
        h = [(satir+1,sutun+1),(satir+1,sutun-1),(satir-1,sutun+1),(satir-1,sutun-1)]
        for i in g:
            if inBoard(i[0],i[1]) == True and board[i[0]][i[1]] not in blackpieces:
                t.append(reverseCoords[i[1]] + str(8-i[0]))
        for i in h:
            if inBoard(i[0],i[1]) == True and board[i[0]][i[1]] not in blackpieces:
                t.append(reverseCoords[i[1]] + str(8-i[0]))
    return t

def showMoves(x):
    global whitepieces
    global blackpieces
    global board
    global whitecastles
    global whiteelephants
    global whitehorses
    global whiteking
    global whitepawns
    global whitequeen
    global blackpawns
    global blackcastles
    global blackelephants
    global blackking
    global blackhorses
    global blackqueen
    global coords
    global reverseCoords
    global t
    print("> showmoves",x)
    t=[]
    sutun, satir = findIndex(x)
    if x in whitepawns:
        if board[satir-1][sutun] == "  " or board[satir-1][sutun] in blackpieces:
            t.append(reverseCoords[sutun] + str(9-satir))
    if x in blackpawns:
        if board[satir+1][sutun] == "  " or board[satir+1][sutun] in whitepieces:
            t.append(reverseCoords[sutun] + str(9-satir))
    if x in blackcastles or x in whitecastles:
        ust(x)
        alt(x)
        sagduz(x)
        solduz(x)
    if x in whitequeen or x in blackqueen:
        ust(x)
        alt(x)
        sagduz(x)
        solduz(x)
        sagAlt(x)
        sagUst(x)
        solAlt(x)
        solUst(x)
    if x in whiteelephants:
        solUst(x)
        sagUst(x)
    if x in blackelephants:
        solAlt(x)
        sagAlt(x)
    if x in whiteking:
        g = [(satir+1,sutun+1), (satir+1,sutun),(satir+1,sutun-1),(satir,sutun+1),(satir,sutun-1),(satir-1,sutun+1),(satir-1,sutun),(satir-1,sutun-1)]
        for i in g:
            if inBoard(i[0],i[1]) == True and board[i[0]][i[1]] not in whitepieces:
                t.append(reverseCoords[i[1]] + str(8-i[0]))
    if x in blackking:
        g = [(satir+1,sutun+1), (satir+1,sutun),(satir+1,sutun-1),(satir,sutun+1),(satir,sutun-1),(satir-1,sutun+1),(satir-1,sutun),(satir-1,sutun-1)]
        for i in g:
            if inBoard(i[0],i[1]) == True and board[i[0]][i[1]] not in blackpieces:
                t.append(reverseCoords[i[1]] + str(8-i[0]))
    if x in whitehorses:
        g = [(satir+1,sutun+2), (satir+1,sutun-2),(satir+2,sutun-1),(satir+2,sutun+1),(satir-1,sutun-2),(satir-1,sutun+2),(satir-2,sutun+1),(satir-2,sutun-1)]
        h = [(satir+1,sutun+1),(satir+1,sutun-1),(satir-1,sutun+1),(satir-1,sutun-1)]
        for i in g:
            if inBoard(i[0],i[1]) == True and board[i[0]][i[1]] not in whitepieces:
                t.append(reverseCoords[i[1]] + str(8-i[0]))
        for i in h:
            if inBoard(i[0],i[1]) == True and board[i[0]][i[1]] not in whitepieces:
                t.append(reverseCoords[i[1]] + str(8-i[0]))
    if x in blackhorses:
        g = [(satir+1,sutun+2), (satir+1,sutun-2),(satir+2,sutun-1),(satir+2,sutun+1),(satir-1,sutun-2),(satir-1,sutun+2),(satir-2,sutun+1),(satir-2,sutun-1)]
        h = [(satir+1,sutun+1),(satir+1,sutun-1),(satir-1,sutun+1),(satir-1,sutun-1)]
        for i in g:
            if inBoard(i[0],i[1]) == True and board[i[0]][i[1]] not in blackpieces:
                t.append(reverseCoords[i[1]] + str(8-i[0]))
        for i in h:
            if inBoard(i[0],i[1]) == True and board[i[0]][i[1]] not in blackpieces:
                t.append(reverseCoords[i[1]] + str(8-i[0]))
    if len(t) == 0:
        print("FAILED")
    else:
        t = sorted(t)
        print(*t)

def move(x,y):
    global whitepieces
    global blackpieces
    global board
    global whitecastles
    global whiteelephants
    global whitehorses
    global whiteking
    global whitepawns
    global whitequeen
    global blackpawns
    global blackcastles
    global blackelephants
    global blackking
    global blackhorses
    global blackqueen
    global coords
    print("> move", x, y)
    k = []
    for i in y:
        k.append(i)
    hedefsutun = coords[k[0]]
    hedefsatir = 8 - int(k[1])
    sutun, satir = findIndex(x)
    if x in whitepawns:
        if satir - hedefsatir != 1:
            print("FAILED")
        elif hedefsutun != sutun:
            print("FAILED")
        elif board[hedefsatir][hedefsutun] in whitepieces:
            print("FAILED")
        elif hedefsatir > satir:
            print("FAILED")
        else:
            board[satir-1][sutun] = x
            board[satir][sutun] = "  "
            print("OK")
    if x in blackpawns:
        if hedefsatir - satir != 1:
            print("FAILED")
        if hedefsutun != sutun:
            print("FAILED")
        elif board[hedefsatir][hedefsutun] in blackpieces:
            print("FAILED")
        elif hedefsatir < satir:
            print("FAILED")
        else:
            board[satir+1][sutun] = x
            board[satir][sutun] = "  "
            print("OK")
    if x in whitecastles:
        sutun, satir = findIndex(x)
        if y in showMoves2(x):
            board[hedefsatir][hedefsutun] = x
            board[satir][sutun] = "  "
            print("OK")
        else:
            print("FAILED")
    if x in blackcastles:
        sutun, satir = findIndex(x)
        if y in showMoves2(x):
            board[hedefsatir][hedefsutun] = x
            board[satir][sutun] = "  "
            print("OK")
        else:
            print("FAILED")
    if x in whiteking:
        if abs(hedefsutun-sutun) > 1 or abs(hedefsutun-sutun) < 0 or abs(hedefsatir-satir) > 1 or abs(hedefsatir-satir) < 0:
            print("FAILED")
        elif board[hedefsatir][hedefsutun] in whitepieces:
            print("FAILED")
        else:
            board[hedefsatir][hedefsutun] = x
            board[satir][sutun] = "  "
            print("OK")
    if x in blackking:
        if abs(hedefsutun-sutun) > 1 or abs(hedefsutun-sutun) < 0 or abs(hedefsatir-satir) > 1 or abs(hedefsatir-satir) < 0:
            print("FAILED")
        elif board[hedefsatir][hedefsutun] in blackpieces:
            print("FAILED")
        else:
            board[hedefsatir][hedefsutun] = x
            board[satir][sutun] = "  "
            print("OK")
    if x in whitehorses:
        sutun, satir = findIndex(x)
        if y in showMoves2(x):
            board[hedefsatir][hedefsutun] = x
            board[satir][sutun] = "  "
            print("OK")
        else:
            print("FAILED")
    if x in blackhorses:
        sutun, satir = findIndex(x)
        if y in showMoves2(x):
            board[hedefsatir][hedefsutun] = x
            board[satir][sutun] = "  "
            print("OK")
        else:
            print("FAILED")
    if x in whiteelephants:
        sutun, satir = findIndex(x)
        if y in showMoves2(x):
            board[hedefsatir][hedefsutun] = x
            board[satir][sutun] = "  "
            print("OK")
        else:
            print("FAILED")
    if x in blackelephants:
        sutun, satir = findIndex(x)
        if y in showMoves2(x):
            board[hedefsatir][hedefsutun] = x
            board[satir][sutun] = "  "
            print("OK")
        else:
            print("FAILED")
    if x in whitequeen:
        sutun, satir = findIndex(x)
        if y in showMoves2(x):
            board[hedefsatir][hedefsutun] = x
            board[satir][sutun] = "  "
            print("OK")
        else:
            print("FAILED")
    if x in blackqueen:
        sutun, satir = findIndex(x)
        if y in showMoves2(x):
            board[hedefsatir][hedefsutun] = x
            board[satir][sutun] = "  "
            print("OK")
        else:
            print("FAILED")
def inBoard(x,y):
    if 0 <= x <= 7 and 0 <= y <= 7:
        return True
    else:
        return False
def pirtnBoard():
    global board
    print("> print")
    print("-----------------------")
    for i in board:
        print(*i)
    print("-----------------------")
for x in commands:
    for i in x:
        if i[0] == "move" :
            move(i[1],i[2])
        elif i[0] == "initialize":
            initialize()
        elif i[0] == "showmoves":
            showMoves(i[1])
        elif i[0] == "print":
            pirtnBoard()
        elif i[0] == "exit":
            print("> exit")
            exit()
