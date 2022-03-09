import sys
try:
    f = open(sys.argv[1], "r")
except IOError:
    print("IOError: cannot open",sys.argv[1])
    print(" ")
    print("˜ Game Over ˜")
    sys.exit()
except IndexError:
    print("IndexError: number of input files less than expected.")
    print(" ")
    print("˜ Game Over ˜")
    sys.exit()
try:
    n = open(sys.argv[2], "r")
except IOError:
    print("IOError: cannot open",sys.argv[2])
    print(" ")
    print("˜ Game Over ˜")
    sys.exit()
except IndexError:
    print("IndexError: number of input files less than expected.")
    print(" ")
    print("˜ Game Over ˜")
    sys.exit()
inputtxt = f.read().split("\n")
inputlast = [k.strip() for k in inputtxt]
compare = n.read().split("\n")
comparelast = [k.strip() for k in compare]
class MoreOperands(Exception):
    pass
try:
    for i in range(0, len(inputlast)):
        n = inputlast[i].split(" ")
        try:
            y = [float(k) for k in n]
            if len(n) < 4:
                raise IndexError
            elif len(n) > 4:
                raise MoreOperands
            else:
                try:
                    k = " "
                    for x in range(int(y[2]),int(y[3])+1):
                        if x % int(y[0]) == 0 and x % int(y[1]) != 0:
                            k += str(x) + " "
                    if k.strip(" ") != comparelast[i]:
                        raise AssertionError
                    else:
                        print("------------")
                        print("My Results:          ",k)
                        print("Results to compare:   ",comparelast[i])
                        print("Goool!!!")
                except AssertionError:
                    print("------------")
                    print("My Results:          ",k)
                    print("Results to compare:   ",comparelast[i])
                    print("AssertionError: results don't match")
        except MoreOperands:
            print("------------")
            print("kaBOOM: run for your life!")
        except ValueError:
            print("------------")
            print("ValueError: only numeric input is expected")
            print("Given input:",inputlast[i])
        except IndexError:
            print("------------")
            print("IndexError: number of operands less than expected.")
            print("Given input:",inputlast[i])
        except ZeroDivisionError:
            print("------------")
            print("ZeroDivisionError: You can't divide by 0.")
            print("Given input:",inputlast[i])
        except:
            print("------------")
            print("kaBOOM: run for your life!")
finally:
    print(" ")
    print("˜ Game Over ˜")


