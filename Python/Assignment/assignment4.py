import sys
try:
    f = open(sys.argv[2], "r")
except IOError:
    print("Key file not found")
    sys.exit()
try:
    n = open(sys.argv[3], "r")
except IOError:
    print("Input file not found")
    sys.exit()
class ParameterNumber(Exception):
    pass
class UndefinedParameter(Exception):
    pass
class CouldNotBeRead(Exception):
    pass
class  InputFileEmpty(Exception):
    pass
class InvalidCharacter(Exception):
    pass
class KeyFileCantRead(Exception):
    pass
class KeyFileEmpty(Exception):
    pass
class InvalidCharacterInKey(Exception):
    pass
inputText = n.read()
keyDeneme = [i.rstrip("\n") for i in f.readlines()]
keySplitted = [i.split(",") for i in keyDeneme]
allowedCharactersInput = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
try:       #The part for error handling
    if len(sys.argv) != 5:
        raise ParameterNumber
    if sys.argv[1] != "enc" and sys.argv[1] != "dec":
        raise UndefinedParameter
    if sys.argv[3][-3:] != "txt":
        raise CouldNotBeRead
    if len(inputText) == 0:
        raise InputFileEmpty
    for i in n:
        if i not in allowedCharactersInput:
            raise InvalidCharacter
    if sys.argv[2][-3:] != "txt":
        raise KeyFileCantRead
    if len(keyDeneme) == 0:
        raise KeyFileEmpty
    k = []
    for i in keySplitted:
        for c in i:
            k.append(int(c))
    for i in k:
        if type(i) != int:
            raise InvalidCharacterInKey
except InvalidCharacterInKey:
    print("Invalid character in key file")
    sys.exit()
except ParameterNumber:
    print("Parameter number error")
    sys.exit()
except UndefinedParameter:
    print("Undefined parameter")
    sys.exit()
except CouldNotBeRead:
    print("Input file could not be read")
    sys.exit()
except InputFileEmpty:
    print("Input file is empty")
    sys.exit()
except InvalidCharacter:
    print("Invalid character in input file")
    sys.exit()
except KeyFileCantRead:
    print("Key file could not be read")
    sys.exit()
except KeyFileEmpty:
    print("Key file is empty")
    sys.exit()
except InvalidCharacterInKey:
    print("Invalid Character in key file")
    sys.exit()
letterToCodes = {"A" : 1 ,"a" : 1, "B" : 2,"b" : 2, "C" : 3,"c" : 3, "D" : 4,"d" : 4 ,"E" : 5,"e" : 5 ,"F" : 6,"f" : 6, "G" : 7,"g" : 7, "H" : 8,"h" : 8, "I" : 9,"i" : 9,
               "J" : 10,"j" : 10, "K" : 11,"k" : 11, "L" : 12,"l" : 12, "M" : 13,"m" : 13, "N" : 14,"n" : 14, "O" : 15,"o" : 15, "P" : 16,"p" : 16, "Q" : 17,"q" : 17,
               "R" : 18,"r" : 18, "S" : 19,"s" : 19, "T" : 20,"t" : 20, "U" : 21,"u" : 21, "V" : 22,"v" : 22, "W" : 23,"w" : 23, "X" : 24,"x" : 24, "Y" : 25,"y" : 25,
               "Z" : 26,"z" : 26, " " : 27}
reutrn = []
codeToLetters = {v:k for (k, v) in letterToCodes.items()}
def determinant2(x):                                        #The function for finding the determinant of a n*n matrix
    determinant = x[0][0] * x[1][1] - x[0][1] * x[1][0]
    return determinant
def matrixOfMinors(x):
    minor = []
    for i in range(len(x[0])):
        for j in range(len(x[0])):
            satır2 = []
            for a in range(len(x[0])):
                if a != i:
                    satır = []
                    for k in range(len(x[0])):
                        if k != j:
                            satır.append(x[a][k])
                    satır2.append(satır)
            minor.append(satır2)
    global reutrn
    for i in minor:
        if len(i) == 2:
            reutrn.append(i)
        else:
            matrixOfMinors(i)
    return reutrn
def cofactor(y):                                        #The function which does the required calculations for finding the cofactor of the given matrix
    for i in range(len(y)):
        for x in range(len(y[0])):
            if i % 2 == 0 and x % 2 == 1:
                y[i][x] = -y[i][x]
            elif i % 2  == 1 and x % 2 == 0:
                y[i][x] = -y[i][x]
    return y
def adJoint(y):                                         #The function which finds the transpose of the given matrix
    transpose = list(map(list,zip(*y)))
    return transpose
def matrixMul(x,y):                                     #The function which multiplies any given matrix with an 1*n matrix
    result = []
    for k in range(len(y)):
        result.append(0)
    for i in range(len(y)):
        for c in range(len(y)):
            result[i] += x[i][c] * y[c]
    return result
def matrixInverse2(x):                                 #The function which takes the inverse of a 2*2 matrix
    determinant = x[0][0] * x[1][1] - x[0][1] * x[1][0]
    a = x[0][0]
    b = x[1][1]
    x[0][1] = -x[0][1] / determinant
    x[1][0] = -x[1][0] / determinant
    x[0][0] = b / determinant
    x[1][1] = a / determinant
    return x
if sys.argv[1] == "enc":                            #Encoding part
    keyMatrix = []
    for i in keySplitted:
        for c in i:
            keyMatrix.append(int(c))
    matrix1 = [keyMatrix[i:i+len(keyDeneme)] for i in range(0, len(keyMatrix),len(keyDeneme))]
    letters = [i for i in inputText]
    while len(letters) % len(keySplitted) != 0:
        letters.append(" ")
    codedLetters =[]
    for i in letters:
        codedLetters.append(letterToCodes[i])
    matrix2 = [codedLetters[i:i+len(keyDeneme)] for i in range(0, len(codedLetters),len(keyDeneme))]
    encrypted = []
    for x in range(len(matrix2)):
        encrypted += matrixMul(matrix1, matrix2[x])
    last = ""
    for i in encrypted:
        last += str(i) + ","
    last2 = last.rstrip(",")
    with open(sys.argv[4],"w") as dd:
        dd.write(last2)
    dd.close()
elif sys.argv[1] == "dec":                      #Decoding part
    keyMatrix = []
    for i in keySplitted:
        for c in i:
            keyMatrix.append(int(c))
    matrix1 = [keyMatrix[i:i+len(keyDeneme)] for i in range(0, len(keyMatrix),len(keyDeneme))]
    if len(matrix1[0]) == 2:
        matrixInverse = matrixInverse2(matrix1)
    elif len(matrix1[0]) > 2:
        u = []
        for x in matrixOfMinors(matrix1):
            u.append(determinant2(x))
        list1 = [u[i:i+len(matrix1)] for i in range(0, len(u),len(matrix1))]
        matrixInverse = adJoint(cofactor(list1))
        a = 0
        for i in range(len(matrix1)):
            a += matrix1[0][i] * matrixInverse[i][0]
        for i in range(len(matrixInverse)):
            for k in range(len(matrixInverse)):
                matrixInverse[i][k] = matrixInverse[i][k] / a
    inputList = inputText.split(",")
    matrix2 = []
    for i in inputList:
        matrix2.append(int(i))
    matrix2 = [matrix2[i:i+len(keyDeneme)] for i in range(0, len(matrix2),len(keyDeneme))]
    decrypted = []
    for x in range(len(matrix2)):
        decrypted.append(matrixMul(matrixInverse,matrix2[x]))
    floatToInt = []
    for i in decrypted:
        for x in i:
            floatToInt.append(int(x))
    decodedLetters = []
    for i in floatToInt:
        decodedLetters.append(codeToLetters[i])
    command = ""
    for i in decodedLetters:
        command += i
    with open(sys.argv[4], "w") as dd:
        dd.write(command)
    dd.close()
