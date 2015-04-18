import math
def MuyuanC(T):
    if T > 0:
        print 'Hello Muyuan Chen'
    else:
        print 'Good bye Muyuan Chen'


F = [1, 2]
def fibNEven(N):
    if( N <= 0):
        print 'please input a valid number'
        return
    print F[0]
    while( N - 1 > 0 ):
        a = F[0]+F[1]
        if(a % 2 == 1):
            F[0] = F[1]
            F[1] = a
        else:
            F[0] = F[1]
            F[1] = a
            print a
            N -= 1

def tandf(N):
    if (N <= 0 ):
        print 'please input a valid number'
        return
    for a in range (1, N):
        if(a % 3 == 0 and a % 5 == 0):
            print 'FizzBuzz'
        elif (a % 3 == 0):
            print 'Fizz'
        elif (a % 5 == 0):
            print 'Buzz'
        else:
            print a

print math.sqrt(4)
print 'Calm down, Li Wang'
fibNEven(7)

tandf(15)
MuyuanC(20)

