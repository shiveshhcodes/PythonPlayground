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
                        print("Yes!! This email format is Perfect for you can use!!")
                        break
                else: 
                    print(" Please use .com/.in at last. Let's Try Again. ")
            else:
                print(" Please do use @ once only. Let's Try Again. ")
        else:
            print(" Please start with Alphabets Only!! Let's Try Again. ")
    else:
        print(" Email Must be size more then 6 characters!! Let's Try Again. ")
    
    email = input(" Enter Your Email : ")
    
    
    
# phone_number = input(" Enter your number and let's check if it's valid or not. ")
# while True:
#     d,k = 0,0
#     if len(phone_number)>=10:
#      if (phone_number.startswith("0")) or (phone_number.startswith("+91")):
#       if phone_number.replace("+91" , "").isdigit() or phone_number.replace("9" , "").isdigit():
#           print("Yess , this looks like a perfect number here :)")
#           break
#       else:
#              print(" please use only numbers , nothing else digits. ")        
#      else:
#          print("Please Start with 0 or +91")
#     else:
#         print("Phone Number Must be atleast 10 Digits!! Let's Try Again.")
        
#     phone_number = input(" Enter your number and let's check if it's valid or not. ")
        
        