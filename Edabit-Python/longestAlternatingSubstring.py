# Given a string of digits, return the longest substring with alternating odd/even or even odd digits. If two or more substring have the same lenght, return the substrings that occur first.

def longest_substring(digits):
    #Keep track of all the substrings that occur in the string that follow the pattern.
    substirings=[]
    substirings.append(2)
    print (substirings)

# longest_substring(3)
digits="225424272163254474441338664823"
combined=[]
sequence=True
substring=''
substrings=[]
# while sequence:

for number in digits:
    #if the substring is empty then it can start off as either even or odd.
    if not substring:
        if int(number)%2==0:
            substring+=number
            combined.append((number,'Even'))
        else:
            substring+=number
            combined.append((number,'Odd'))
    else:
        if int(substring[-1])%2==0 and int(number)%2!=0 :
            substring+=number
            combined.append((number,'Odd'))
        elif int(substring[-1])%2!=0 and int(number)%2==0 :
            substring+=number
            combined.append((number,'Even'))
        else:
            if len(substring)>=2:
                substrings.append(substring)
                substring=''
            else:
                substring=''
            
print(substrings)