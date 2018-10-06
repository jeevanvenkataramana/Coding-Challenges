''' for sample input 5

output

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

'''



def print_rangoli(size):
    # your code goes here
    lines = size*2 -1
    width = lines + size*2 -2
   
    ch='a'
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    ch="-"
    temp=alpha[0]
        
        
    result=list()

    for i in range(1,size+1):
        temp1=alpha[size-i:size]
        temp2 = temp1[:]
        temp1.reverse()
        temp1=temp1+temp2[1:]
        ans=("-".join(temp1)).center(width,"-")
        print(ans)
        result.append(ans)
   
    
    for j in range(len(result)-2,-1,-1):
        print(result[j])
        
