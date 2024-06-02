phone_number = input(" Enter your number and let's check if it's valid or not. ")
while True:
    d,k = 0,0
    if len(phone_number)>=10:
     if (phone_number.startswith("0")) or (phone_number.startswith("+91")):
      if phone_number.replace("+91" , "").isdigit() or phone_number.replace("9" , "").isdigit():
          print("Yess , this looks like a perfect number here :)")
          break
      else:
             print(" please use only numbers , nothing else digits. ")        
     else:
         print("Please Start with 0 or +91")
    else:
        print("Phone Number Must be atleast 10 Digits!! Let's Try Again.")
        
    phone_number = input(" Enter your number and let's check if it's valid or not. ")