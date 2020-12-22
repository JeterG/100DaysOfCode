# Write a function that accepts a positive integer between 0 and 999 inclusive and returns a string representation of that interger written in English

def num_to_eng(num):  
    ones={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
    teens={11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eightteen',19:'nineteen'}
    tens=['ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    str_num=str(num)
    if len(str_num)==1:
        return(ones[num])
    elif len(str_num)==2:
        if num<20:
            return(teens[num])
        elif num%10==0:
            return(tens[int(str_num[0])-1])
        else:
            return(tens[int(str_num[0])-1] + " " + ones[int(str_num[1])])
    else:
        if str_num[1:]=='00':
            return (ones[int(str_num[0])] + " hundred")
        else:
            return(ones[int(str_num[0])] + " hundred "+num_to_eng(int(str_num[1:])))

print(num_to_eng(900))