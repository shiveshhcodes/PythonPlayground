import phonenumbers
from phonenumbers import timezone,geocoder,carrier
def ensure_with(no):
    if not no.startswith('+91'):
        no = '+91' + no
    return no

number = input("+91:")
number = ensure_with(number)
print(" phone numbers details are below!! ")
try:
    phone = phonenumbers.parse(number)
    time=timezone.time_zones_for_number(phone)
    car=carrier.name_for_number(phone,"en")
    reg=geocoder.description_for_number(phone,"en")
    print(phone)
    print(time)
    print(car)
    print(reg)
except phonenumbers.phonenumberutil.NumberParseException as e:
    print(f"Error parsing number: {e}")
