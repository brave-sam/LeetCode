def starPattern(n):
    print("Star pattern")
    for i in range(0,n):
        for k in range(n):
            print("* ",end="")
        print("\r")
starPattern(2)
  
def pyramidPattern(n):
    print("pyramidPattern")
    for i in range(0,n):
        for k in range(0,i+1):
            print("* ",end="")

        print("\r")
pyramidPattern(5)

def pyramidrotPattern(n):
    print("pyramidrotPattern")
    for i in range(0,n):
        for k in range(n,i,-1):
            print("* ",end="")

        print("\r")
pyramidrotPattern(5)

#After180 degree roTation
def pyramid180Pattern(n):
    print("pyramid180Pattern")
    k = 2*n-2
    for i in range(0,n):
        for j in range(0,k):
            print(" ",end="")
        k=k-2
        for j in range(0,i+1):
            print("* ",end="")

        print("\r")
pyramid180Pattern(5)

def reverseFullPyramidPattern(n):
    print("reverseFullPyramidPattern")
    for i in range(0,n):
        for k in range(i):
            print(" ",end="")
        for j in range(0,(n-i)):
            print("* ",end="")
        print()

reverseFullPyramidPattern(6)

def fullPyramidPattern(n):
    print("fullPyramidPattern")
    c=n-1
    for i in range(0,n):
        for j in range(0,c):
            print(end=" ")
        c=c-1
        for k in range(0,i+1):
            print("* ",end="")
        print()

fullPyramidPattern(7)

