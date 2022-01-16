import phonenumbers
from phonenumbers import geocoder, carrier

number=input("Enter Phone Number: ")
success=1
try:
     phone_number=phonenumbers.parse(number)
     valid=phonenumbers.is_valid_number(phone_number)
     if(valid):
          country_code=phonenumbers.parse(number, "CH")
          country=(geocoder.description_for_number(country_code,"en"))
          service=phonenumbers.parse(number,"RO")
          service_provider=(carrier.name_for_number(service,"en"))
     else:
          possible=phonenumbers.is_possible_number(phone_number)
          success=-1

except:
     success=0

if(success==1):
     print("Number is valid!")
     print("Country: "+country+"\nService Provider: "+service_provider)
     file=open('Records.txt','a')
     file.write("Phone Number: "+number+"\nCountry: "+country+"\nService provider: "+service_provider+"\n\n")
     file.close()
elif(success==-1):
     print("Not valid but possible")
else:
     print("Please provide a valid phone number.")