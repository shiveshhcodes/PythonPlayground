email = input(" Enter Your Email : ") #g@g.in , wscube@gmail.com
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
                        d =1 
                if k ==1 or j ==1 or d==1:
                    print(" Wrong Email 5 ")
                else:
                    print("Wrong E-Mail")
            else: 
                print(" wrong email 4 ")
        else:
            print(" wrong email 3 ")
    else:
        print(" Wrong Email 2 ")
else:
    print(" Wrong Email 1 ")