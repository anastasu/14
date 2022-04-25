x = 9 ** 81 + 27 ** 729 - 4
s = ''
while x > 0:
    s = str (x % 9) + s
    x = x // 9
print (s)
k = s.count('0') + s.count('8')
print (k)
