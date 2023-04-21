#67. Add Binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        a, b = a[::-1], b[::-1]
        carry = 0

        result = ""

        for i in range(max(len(a), len(b))):

            pa = int(a[i]) if i < len(a) else 0
            pb = int(b[i]) if i < len(b) else 0

            summ = pa + pb + carry
            char = str(summ % 2)

            result = char + result

            carry = summ // 2
        
        if carry == 1:
            result = "1" + result

        return result