import phonenumbers

number = phonenumbers.parse("9425813786" , "IN")
# print(number)

from phonenumbers import format_number , PhoneNumberFormat
formatted_number = format_number(number , PhoneNumberFormat.INTERNATIONAL)
print(formatted_number)