x = 8**888+16*16**1616-2**444
s = ''
while x>0:
    s=str(x %16)+s
    x //= 16
ms=0
for i in range(len(s)):
    if int(s[i])> int (ms):
        ms = s[i]

print(s.count(ms))