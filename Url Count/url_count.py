''' Read the content from input.txt where details about a user accesstime of url present
create a output.txt file which contains a list of urls accessed and a count in decreasing order

input.txt
[www.google.com;starttime:22:00:53;endtime:01:23:22]
[www.youtube.com;starttime:22:00:53;endtime:01:23:22]
[www.google.com;starttime:22:00:53;endtime:01:23:22]
[www.linkedin.com;starttime:22:00:53;endtime:01:23:22]
[www.google.com;starttime:22:00:53;endtime:01:23:22]
[www.linkedin.com;starttime:22:00:53;endtime:01:23:22]
[www.linkedin.com;starttime:22:00:53;endtime:01:23:22]
[www.google.com;starttime:22:00:53;endtime:01:23:22]
[www.linkedin.com;starttime:22:00:53;endtime:01:23:22]
[www.linkedin.com;starttime:22:00:53;endtime:01:23:22]
[www.youtube.com;starttime:22:00:53;endtime:01:23:22]

output.txt

www.linkedin.com 5
www.google.com 4
www.youtube.com 2

'''


def solution(in_file):
    file_in=open(in_file,"r+")
    file_out=open("output.txt","w+")
    results=dict()
    
    for line in file_in:
        line = line.strip("[")
        line=line.split(";")
        if line[0] in results:
            results[line[0]]=results[line[0]]+1
        else:
            results[line[0]]=1

    sorted_keys = sorted(results, key=results.get, reverse = True)

    for i in sorted_keys:
        file_out.write(i+" "+str(results[i])+"\n")
        
    file_in.close()
    file_out.close()
    return("output.txt")






out_file=solution("input.txt")
for line in open(out_file,"r+"):
    print(line)
