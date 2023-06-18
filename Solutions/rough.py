def isHappy(n):

        summ = 0
        for i in str(n):

            summ += (int(i) * int(i))
            # print(summ)
        
        result = 0

        for i in str(summ):

            result += (int(i) * int(i))
            print(result)

        n = summ
        if result == 1:
            return True
        
        else:
            isHappy(result)
        

print(isHappy(19))      