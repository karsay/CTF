import sys
ans = []
p = [70,152,195,284,475,612,791,896,810,850,737,1332,1469,1120,1470,832,1785,2196,1520,1480,1449]
l = 0

for i in p:
    if l != 0:
        ans.append(chr(i / (l + 1)))
    else:
        ans.append(chr(i))
    l = l + 1

for answer in ans:
    sys.stdout.write(answer)
