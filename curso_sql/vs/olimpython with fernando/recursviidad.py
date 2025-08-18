def sumar(n):
    if n == 1:
        print(n,end="")
        return 1
    else:
        print(n,end=" + ")
        return n  + sumar(n-1)
    

print(f" = {sumar(5)}")