'''Print odd and even position characters of a string

sample input

2
Hacker
Rank

sample output

Hce akr
Rn ak

'''



n=int(input())
list=list()
for i in range(n):
    list.append(input())

for i in list:
    print(i[::2]+" "+i[1::2])
