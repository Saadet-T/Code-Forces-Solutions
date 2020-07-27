list = [ ] #making a list for inputs
n = 0
a = int(input())
for n in range(0,a):
    list.append(str(input()))#add inputs in list

for i in range(0,a):
    b = list[i]
    if len(list[i])>10:
            print(b[0]+str(len(b)-2)+b[len(b)-1])#if word lenght is longer than 10 get first and last letters and put the numbers in between
    else:
         print(b)
