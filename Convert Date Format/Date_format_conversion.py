''' Convert a date in the format 9-sep-2015 to yyyy/mm/dd --> 2015/09/09'''

def convert(dates):
    month = {'jan':'01','feb':'02','mar':'03' ,'apr':'04' ,'may':'05' ,'jun':'06' ,'jul':'07' ,'aug':'08' ,'sep':'09' ,'oct':'10' ,'nov':'11' ,'dec':'12'}
    results=list()
    temp_str="/"
    for i in dates:
        date = i.split("-")
        date[1]=month[date[1]]
        if (len(date[0])==1):
            date[0]="0"+date[0]
        results.append(temp_str.join(reversed(date)))
    return(results)


dates=list()
dates.append("6-aug-2018")
dates.append("9-jan-2018")
print("\nInputs given")
for i in dates:
    print(i)
print("\nConverted dates")
for i in convert(dates):
    print(i)

