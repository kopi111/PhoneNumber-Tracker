import phonenumbers
from phonenumbers import carrier, geocoder,timezone
mobileNo = input("Please Enter Mobile Number ")
mobileNo = phonenumbers.parse("+"+mobileNo)


#8764644762
#get timezone  PHONE NUMBER
print(timezone.time_zones_for_number(mobileNo))

#Getting carrier of a phone number
print(carrier.name_for_number(mobileNo,"en"))

#Getting the region information 
print(geocoder.description_for_number(mobileNo,"en"))

#validating a phone number 
print("Valid Mobile Number:", phonenumbers.is_valid_number(mobileNo))

#Checking possibility of a number 
print("Checking possibility of number:" , phonenumbers.is_possible_number(mobileNo))