"""Stripe connect allows marketplaces and platforms like KickStarters, Shopifys and Postmates of the world to accept money and pay pot to third parties.

Lets say taxico and its drivers demand ride sharing service, wants to pay out to its drivers for each ride they complete. They could simply use stripes connect API to make that happen. Each driver could have their own stripe account and taxico could then send the funds to drivers account.

Stripes standard fees in the US are 2.9% + 0.3 on each transaction. If a ride costs 10, stripe takes 0.59 (0.59 = 10 * 0.029% + .30). Taxico would be left with 9.41 to share between itself and the driver. Taxico can then specify to stripe how much to transfer to the driver. for example, Taxico could tell stripe to send the driver 8.77. Once the driver has been paid stripe transfers the remaining 0.64 in to Taxico's stripe account.

Take an array of lines as input and return an integer array equal in size to the no of line that begin with "BAL".
If an input line begin with 'API'. Update the balance for the platform (in this case it is taxico), If present the destination account. account will have an unique id.
If an input line begins with "Bal". append the current balance in USD cents for the account in question to the output array
Assume that we are using the US Standard stripe fee of 2.9% + 0.30
Test cases:

Input:
    3
    API: amount=1000&merchant=123456789&destination[account]=111111&destination[amount]=877
    BAL: merchant=123456789
    BAL: merchant=111111
Output:
    64
    877


Input:
    2
    API: amount=2000&merchant=10101010
    BAL: merchant=10101010
Output:
    1912


Input:
    API: amount=1000&merchant=123456789&destination[account]=111111&destination[amount]=877
    API: amount=800&merchant=123456789&destination[account]=112211&destination[amount]=622
    BAL: merchant=123456789
    BAL: merchant=112211
Output:
    189
    622
    """

# Solution


def PlatBalance(lines):
    ledger=list()     # contains account no and balance in sucessive indexes
    result=list()
   
    for i in lines:
        if "API" in i:
            temp=i.replace("&","=")         # so that the API splits by each label ['API: amount', '1000', 'merchant', '123456789', 'destination[account]', '111111', 'destination[amount]', '877']
            temp=temp.split("=")
            print(temp)
            print(temp[1].isdigit())
            amount=int(temp[1])
            stripe_charge = int(amount * 0.029 + 30)
            merchant_amt=amount-stripe_charge
            merchant_account=int(temp[3])
            driver_account=0
            driver_amt=0
            #print(amount)
            if(len(temp)>4):
                driver_account=int(temp[5])
                driver_amt=int(temp[7])
                merchant_amt=merchant_amt-driver_amt

            if merchant_account in ledger:
                ledger[ledger.index(merchant_account)+1]=ledger[ledger.index(merchant_account)+1]+merchant_amt
            else:
                ledger.append(merchant_account)
                ledger.append(merchant_amt)
                
            if driver_account in ledger and (driver_account!=0):
                ledger[ledger.index(driver_account)+1]=ledger[ledger.index(driver_account)+1]+driver_amt
            elif driver_account!=0:
                ledger.append(driver_account)
                ledger.append(driver_amt)
        else:
            temp=i.split("=")
            if (int(temp[-1])) in ledger:
                result.append(ledger[ledger.index(int(temp[-1]))+1])
            else:
                result.append(0)
            
                
    return result

    
    
print("\nInput 1\n")
list_x=list()
list_x.append("API: amount=1000&merchant=123456789&destination[account]=111111&destination[amount]=877")
list_x.append("BAL: merchant=123456789")
list_x.append("BAL: merchant=111111")
result=PlatBalance(list_x)
for i in result:
    print(i)
print("\nInput 2\n")
list_x.clear()
list_x.append("API: amount=2000&merchant=10101010")
list_x.append("BAL: merchant=10101010")
result=PlatBalance(list_x)
for i in result:
    print(i)
print("\nInput 3\n")
list_x.clear()
list_x.append("API: amount=1000&merchant=123456789&destination[account]=111111&destination[amount]=877")
list_x.append("API: amount=800&merchant=123456789&destination[account]=112211&destination[amount]=622")
list_x.append("BAL: merchant=123456789")
list_x.append("BAL: merchant=112211")
result=PlatBalance(list_x)
for i in result:
    print(i)
