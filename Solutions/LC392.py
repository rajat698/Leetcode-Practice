s = "aaaaaa"
t = "bbaaaa"

count = 0
j = 0
i = 0

while i < len(s):
    while j < len(t):
        if s[i] == t[j]:
            count += 1
            i += 1
            j += 1
            break
        
        j += 1

    if j == len(t):
        break
    
    print(i, j)

if count == len(s):
    print("Y")

else:
    print("F")