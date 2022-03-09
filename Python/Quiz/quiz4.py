import sys
f = open(sys.argv[1], "r")
lines = f.read().strip("\n").split("\n")
f.close()
k = [x.split("\t") for x in lines]
for x in range(0,len(lines)):
    k[x][0] = int(k[x][0])
    k[x][1] = int(k[x][1])
sorted_list = sorted(k, key = lambda x: (x[0], x[1]))
t = sorted_list.copy()
y = 0
counter = 1
for x in range(1, len(k)):
    if sorted_list[x][0] != sorted_list[x-1][0]:
        counter += 1
        p = ["Message "+ str(counter),"",""]
        t.insert(x+y, p)
        y += 1
with open(sys.argv[2], "w") as k:
    k.write("Message 1\n")
    for i in t:
        k.write("{}"" ""{}"" ""{}"" ""\n".format(i[0],i[1],i[2]))
k.close()




