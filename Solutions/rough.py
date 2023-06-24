s = "abacaba"

count = 1
letters = set()

for i in s:
    
    if i not in letters:
        letters.add(i)
    
    else:
        count += 1
        letters = set()
        letters.add(i)
        print(count)
    print(letters)

print(count)
