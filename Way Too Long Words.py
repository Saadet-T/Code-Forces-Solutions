list = [ ]
n = 0
a = int(input())
for n in range(0,a):
    list.append(str(input()))

for i in range(0,a):
    b = list[i]
    if len(list[i])>10:
            print(b[0]+str(len(b)-2)+b[len(b)-1])
    else:
         print(b)