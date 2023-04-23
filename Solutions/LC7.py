#7. Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        
            l = list(str(x))

            for i in range(len(l) - 1, 0, -1):

                if len(l) != 1 and l[i] == '0':
                    l.pop()
                else:
                    break

            if l[0] == '-':

                l = l[1:len(l)]
                a = '-' + ''.join(l[::-1])

            else:

                a = ''.join(l[::-1])
            
            b = int(a)
            if -2**31 <= b <= 2**31 - 1:
                return b
            else:
                return '0'