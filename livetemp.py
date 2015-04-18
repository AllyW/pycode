def f7(n):
    while(n > 0):
        n = n / 10
        print (n %10)


def f8(n):
    i = 0
    j = 1
    while(j<n):
        i+=j
        j+=1
    return i

f7(12254)
print f8(17)
