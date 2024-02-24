def numberFunction(n):
    for i in range(1,n):
        for j in range(1,i):
            print(j,end=" ")
        print()
numberFunction(7)

def numberFunction2(n):
    for i in range(1,n):
        for k in range(1,i+1):
            print(i,end=" ")
        print()

numberFunction2(7)

def numberFunction3(n):
    for i in range(1,n):
        for j in range(1,n-i):
            print(j,end=" ")
        print()
numberFunction3(7)