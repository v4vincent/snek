import math

x = int(input())

def hurts(frequency):

    n = 0

    while n <= 3:
        if n <= 3:
            r = math.pow(2, 1/12)
            next_freq = frequency * math.pow(r,n)
            print(f'{next_freq:.2f} Hz')
            n = n + 1
    

hurts(x)
