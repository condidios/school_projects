import sys

S = sys.argv[1]
S = S.split(",")
for y in range(0, len(S)):
    S[y] = int(S[y])

e = []
sum = 0
for x in S:
   if x > 0:
       e.append(x)
       sum = sum + x

k = []
csum = 0
for x in e:
    if x % 2 == 0:
        k.append(x)
        csum = csum + x
b = ""
for x in k:
    b += ',' + str(x)
b = b.lstrip(",")
print("Even Numbers: ", "\"", b, "\"", sep = "")
print("Sum of Even Numbers:", csum)
rate = csum / sum
rate = round(rate, 3)
print("Even Number Rate:", rate)






