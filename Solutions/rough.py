n = 58

#4, 90, 900, 0
#1990, 1900, 1000

l = []
x = 10
while n != 0:
    
    a = n % x
    x *= 10
    l.append(a)

    n -= a

l.sort(reverse=True)

print(l)