# importing the module
import pywhatkit

# using Exception Handling to avoid unprecedented errors

# write inside this empty list the phone numbers you plan to send them the message
phone_li =[
'+20.....'
]

# assigne m to the current minute +1
m= 30
try:

#Parameters:
#Receiver mobile number: The Receiver’s mobile number must be in string format and the country code must be mentioned before the mobile number.
#Message: Message to be sent(Must be in string format).
#Hours: This module follows the 24 hrs time format.
#Minutes: Mention minutes of the scheduled time for the message(00-59).

    for con in phone_li:
        pywhatkit.sendwhatmsg(con,"Hello World!",12,m)
        m+=1
			
            
    print("Successfully Sent!")
        

# handling exception
# and printing error message
except Exception as e:
	print(e)