def ismorphic(s, t):
        
    hashMap = {}

    for i in range(len(s)):
        if s[i] not in hashMap:
            hashMap[s[i]] = t[i]
        
        else:
            if hashMap[s[i]] == t[i]:
                continue
            
            else:
                return False

    return True

print(ismorphic('paper', 'title'))