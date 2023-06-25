def mySqrt(x: int) -> int:
    

    for i in range(x):
        tot = i * i
        if tot == x:
            return i
        
        elif tot > x:
            return i - 1
        

print(mySqrt(1))