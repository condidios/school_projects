import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
x = str(a**b)
if int(x) <= 9:
      print("Output :", str(a) + "^" + str(b), "=", x)
else:
      c = 0
      s = 0
      z = 0
      t = ""
      y = ""
      r = ""
      for k in x:
            t += " " + "+" + " " + k
            k = int(k)
            c += k
      if len(str(c)) > 1:
            for u in str(c):
                  y += " " + "+" + " " + u
                  u = int(u)
                  s += u
            y = y.lstrip(" + ")
            t = t.lstrip(" + ")

            if len(str(s)) > 1:
                  for d in str(s):
                        r += " " + "+" + " " + d
                        d = int(d)
                        z += d
                  y = y.lstrip(" + ")
                  t = t.lstrip(" + ")
                  r = r.lstrip(" + ")
                  print("Output :",str(a) + "^" + str(b), "=", x, "=", t, "=",c, "=", y, "=",s, "=", r, "=", z )
            else:
                  print("Output :", str(a) + "^" + str(b), "=", x, "=", t, "=",c, "=", y, "=",s )
      else:
            t = t.lstrip(" + ")
            print("Output :",str(a) + "^" + str(b), "=", x, "=", t, "=",c )







