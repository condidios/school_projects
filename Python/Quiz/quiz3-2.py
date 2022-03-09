import sys
list = sys.argv[1]
list = list.split(",")
list2 = [int(s) for s in list]
list3 = []
list4 = []
list5 = []
for x in list2:
      if x > 0:
            list3.append(x)
for k in list3:
      if k % 2 == 1:
            list4.append(k)
s = 1
while True:
      if (s-1) < len(list4)-1:
            k = list4[s]
            for x in list4:
                  t = list4.index(x)
                  if (t+1) % k != 0:
                        list5.append(x)
            s += 1
            list4 = list5.copy()
            list5 = []
      else:
            break
print("Output : ", end="")
print(*list4, sep=" ")






