num = 1994
class Solution:
    def intToRoman(self, num: int) -> str:

        dict = {1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D', 1000: 'M'}

        nums = []
        x = 10
        while num != 0:

            a = num % x
            x *= 10
            nums.append(a)

            num -= a
        nums.sort(reverse=True)

        exp = [4, 9, 40, 90, 400, 900]
        result = ""

        def exceptions(num):
            if num == 4:
                return 'IV'
            elif num == 9:
                return 'IX'
            elif num == 40:
                return 'XL'
            elif num == 90:
                return 'XC'
            elif num == 400:
                return 'CD'
            elif num == 900:
                return 'CM'


        keys = list(dict.keys())
        i = 0
        curr = 0
        req = 0
        for j in nums:
            if j in exp:
                result += exceptions(j)

            else:
                curr = j
                while curr != 0:
                    for i in keys:
                        if i > curr:
                            break
                        req = i

                    result += dict[req]
                    curr -= req
                    i = 0
    
        return result
