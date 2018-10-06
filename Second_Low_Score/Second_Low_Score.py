'''
Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.


Sample input

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Output

Berry
Harry

'''


data = list()
for _ in range(int(input())):
    name = input()
    score = float(input())
    temp=[name,score]
    data.append(temp)

        
scores=list()
for i in data:
    scores.append(i[1])

scores.sort()
second_low=0
    
for i in range(1,len(scores)):
    if scores[i]>scores[0]:
        second_low=scores[i]
        break
    
names=list()
for i in data:
    if i[1]==second_low:
        names.append(i[0])
            
names.sort()
for i in names:
        print(i)
