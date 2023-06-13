class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        result = strs[0]

        for i in range(1, len(strs)):
            if result == "":
                break  
            count = 0
            t = list(zip(result, strs[i]))
            for i in range(len(t)):
                if t[i][0] == t[i][1]:
                    count += 1
                else:
                    break

            result = result[:count] 

        return result