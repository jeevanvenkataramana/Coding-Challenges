''' count consecutive 1's of a integer no in binary'''

n = int(input())
binary = bin(n)[2:]
list = binary.split("0")
count = 0
for i in list:
    if(len(i)>count):
        count=len(i)
print(count)
