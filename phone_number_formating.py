"""Normalize phone number to the format +380XXXXXXXXX.

    The function takes a phone number in various formats and normalizes it to the
    standard format starting with +380 followed by 9 digits.

    Args:
        phone_number (str): The phone number in various
"""
import re

def normalize_phone(phone_number: str) -> str:
#updating phone number to normalized format +380XXXXXXXXX

    #1 removing whitespace from srting phone_number and non digit characters from argument phone_number
    phone_number = phone_number.strip()
    digits = re.sub(r"\D", "", phone_number)  #number updated to digits only


    #2 checking if phone number starts with 380 code 
    if digits.startswith('380'):
        return '+' + digits
    else: 
        return '+38' + digits
    
"""#Example usage
print(normalize_phone("  (050) 123-45-67 "))  # Output: +380501234567
print(normalize_phone("+380501234567"))      # Output: +380501234567
print(normalize_phone("380501234567"))       # Output

"""       
        

""" test for random raw numbers

raw_numbers = {
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
}
for line in raw_numbers:
    print (normalize_phone(line))  

    
"""
