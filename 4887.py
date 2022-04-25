x = 18**105 + 25*16**100 - 3**51
s = ''
while x>0:
    s=str(x %16)+s
    x //= 16
ms=0
for i in range(len(s)):
    if int(s[i])> int (ms):
        ms = s[i]

print(s.count(ms))