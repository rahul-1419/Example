def pattern (n):
    for i in range (n):
        for j in range(i*2-1):
            #print(" ", end="")
            print("*",end="")
            print(" ", end="")
        print()
# Example
n=5
pattern(n)