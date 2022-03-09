game_map = input("Please enter feeding map as a list:\n").strip()
dogukan6 = eval(game_map)
def map_print(x):
    for y in x:
        print(*y)
move_list = str(input("Please enter direction of movements as a list:\n")).strip()
dogukan4 = eval(move_list)
print("Your board is:")
map_print(dogukan6)
point = 0
for d in dogukan4:
    linecounter = 0
    for i in dogukan6:
        if "*" in i:
            index = i.index("*")
            break
        else:
            linecounter += 1
    if d == "U":
        if linecounter > 0 and dogukan6[linecounter-1][index] != "W":
            if dogukan6[linecounter-1][index] == "C":
                dogukan6[linecounter-1][inadex] = "*"
                dogukan6[linecounter][index] = "X"
                point += 10
            elif dogukan6[linecounter-1][index] == "A":
                dogukan6[linecounter-1][index] = "*"
                dogukan6[linecounter][index] = "X"
                point += 5
            elif dogukan6[linecounter-1][index] == "M":
                dogukan6[linecounter-1][index] = "*"
                dogukan6[linecounter][index] = "X"
                point += -5
            elif dogukan6[linecounter-1][index] == "P":
                dogukan6[linecounter-1][index] = "*"
                dogukan6[linecounter][index] = "X"
                break
            else:
                dogukan6[linecounter-1][index] = "*"
                dogukan6[linecounter][index] = "X"
        else:
            continue
    elif d == "D":
        if linecounter < len(dogukan6)-1 and dogukan6[linecounter+1][index] != "W":
            if dogukan6[linecounter+1][index] == "C":
                dogukan6[linecounter+1][index] = "*"
                dogukan6[linecounter][index] = "X"
                point += 10
            elif dogukan6[linecounter+1][index] == "A":
                dogukan6[linecounter+1][index] = "*"
                dogukan6[linecounter][index] = "X"
                point += 5
            elif  dogukan6[linecounter+1][index] == "M":
                dogukan6[linecounter+1][index] = "*"
                dogukan6[linecounter][index] = "X"
                point += -5
            elif dogukan6[linecounter+1][index] == "P":
                dogukan6[linecounter+1][index] = "*"
                dogukan6[linecounter][index] = "X"
                break
            else:
                dogukan6[linecounter+1][index] = "*"
                dogukan6[linecounter][index] = "X"
        else:
            continue
    elif d == "R":
        if index < len(dogukan6[1])-1 and dogukan6[linecounter][index + 1] != "W":
            if dogukan6[linecounter][index + 1] == "C":
                dogukan6[linecounter][index + 1] = "*"
                dogukan6[linecounter][index] = "X"
                point += 10
            elif dogukan6[linecounter][index + 1] == "A":
                dogukan6[linecounter][index + 1] = "*"
                dogukan6[linecounter][index] = "X"
                point += 5
            elif dogukan6[linecounter][index + 1] == "M":
                dogukan6[linecounter][index + 1] = "*"
                dogukan6[linecounter][index] = "X"
                point += -5
            elif dogukan6[linecounter][index + 1] == "P":
                dogukan6[linecounter][index + 1] = "*"
                dogukan6[linecounter][index] = "X"
                break
            else:
                dogukan6[linecounter][index + 1] = "*"
                dogukan6[linecounter][index] = "X"
        else:
            continue
    elif d == "L":
        if index > 0 and dogukan6[linecounter][index - 1] != "W":
            if dogukan6[linecounter][index - 1] == "C":
                dogukan6[linecounter][index - 1] = "*"
                dogukan6[linecounter][index] = "X"
                point += 10
            elif dogukan6[linecounter][index - 1] == "A":
                dogukan6[linecounter][index - 1] = "*"
                dogukan6[linecounter][index] = "X"
                point += 5
            elif dogukan6[linecounter][index - 1] == "M":
                dogukan6[linecounter][index - 1] = "*"
                dogukan6[linecounter][index] = "X"
                point += -5
            elif dogukan6[linecounter][index - 1] == "P":
                dogukan6[linecounter][index - 1] = "*"
                dogukan6[linecounter][index] = "X"
                break
            else:
                dogukan6[linecounter][index - 1] = "*"
                dogukan6[linecounter][index] = "X"
        else:
            continue
print()
print("Your output should be like this:")
map_print(dogukan6)
print("Your score:", point)
