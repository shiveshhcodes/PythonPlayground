email = input(" Enter Your Email : ")
while True:
    k,j,d = 0,0,0
    if len(email)>=6:
        if email[0].isalpha():
            if ("@"in email) and (email.count("@")==1):
                if (email[-4]==".") or (email[-3]=="."):
                    for i in email:
                        if i.isspace():
                            k = 1
                        elif i.isalpha():
                            if i.isupper():
                                j=1
                        elif i.isdigit():
                            continue
                        elif i=="_" or i=="." or i=="@":
                            continue
                        else:
                            d=1 
                    if k ==1 or j ==1 or d==1:
                        print('Please do not use anu symbols other then "." , "," , "_" ')
                    else:
                        print("Yes!! This email format is Perfect for you , you can use it now!!")
                        break
                else: 
                    print(" Please use .com/.in at last. Let's Try Again. ")
            else:
                print(" Please use '@' only once. Let's Try Again. ")
        else:
            print(" Please start with Alphabets Only!! Let's Try Again. ")
    else:
        print(" Email Must be size of more then 6 characters!! Let's Try Again. ")
    
    email = input(" Enter Your Email : ")
    
    
    

    
