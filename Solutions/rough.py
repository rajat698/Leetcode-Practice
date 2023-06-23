l = []
for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        l.append("FizzBuzz")
    
    elif i % 5 == 0:
        l.append("Fizz")
    
    elif i % 3 == 0:
        l.append("Buzz")
    
    else:
        l.append(i)

print(l)