# Given a string of digits, return the longest substring with alternating odd/even or even odd digits. If two or more substring have the same lenght, return the substrings that occur first.

def longest_substring(digits):
    #Keep track of all the substrings that occur in the string that follow the pattern.
    substirings=[]
    substirings.append(2)
    print (substirings)

# longest_substring(3)
digits="1234567891"
combined=[]
sequence=True
substring=''
# while sequence:

for number in digits:
    if int(number)%2==0:
        substring+=number
        combined.append((number,'Even'))
    else:
        combined.append((number,'Odd'))

print(combined[0])
print(substring)