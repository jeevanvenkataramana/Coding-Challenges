''' Compute average with 2 decimals precision

sample input

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

sample output

56.00

'''

n=int(input())
dict={}
for i in range(n):
    temp=input().split(" ")
    dict[temp[0]]=temp[1:]
        
a=input()
marks=dict[a]
avg=0
for i in marks:
    avg = avg + float(i)
    
print("{0:0.2f}".format(avg/len(marks)))
