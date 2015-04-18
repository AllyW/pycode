import time

def time_exc(s):
    start = time.clock()
    result = eval(s)
    run_time = time.clock() - start
    return result, run_time

def spin_loop(n):
    i = 0
    while i < n:
        i +=1

print time_exc('1+1')
print time_exc('spin_loop(10000)')

print time_exc('spin_loop(10 ** 7)')[1]


