import phonenumbers
from phonenumbers import format_number , PhoneNumberFormat , is_valid_number ,  region_code_for_number , geocoder , carrier

print("entered number is - 9425813786\nand details of the numbers are ⬇️\n")

number = phonenumbers.parse("9425813786" , "IN" ,)
print(number)

description = geocoder.description_for_number(number , "en")
print("This number belongs to Country", description)

is_valid = is_valid_number(number)
print(f"This number valids according to {description}" , is_valid)

formatted_number = format_number(number , PhoneNumberFormat.INTERNATIONAL)
print("The International format of this number is",formatted_number)

region_code = region_code_for_number(number)
print("The region code for the entered numeber is" , region_code)

carrier_name = carrier.name_for_number(number , "en")
print("The Carrier Name of The Number is - " , carrier_name)
