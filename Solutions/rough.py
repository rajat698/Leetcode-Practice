def rotate(s):
    s[:] = s[4:] + s[:4]

n = [1,2,3,4,5,6,7]

rotate(n)

print(n)