#Question One: simplified
import sys
import datetime
data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("current date and time:")
print(data)
print("")

#Question Two
from datetime import timedelta
from datetime import datetime
print("date and time if you add two years from now and subtract 60 seconds:")
print(datetime.now()+timedelta(days = 730)-timedelta(seconds=60))
print("")

#Question Three
from datetime import timedelta
answer = timedelta(days=100, hours=10, minutes=13)
(answer.days, answer.seconds, answer.microseconds)
print("Object representing 100 days, 10 hours, and 13 minutes: ")
print(answer)
print("")

#Question Four
from datetime import datetime
print("Input height:")
ft = int(input("Feet: "))
inch = int(input("Inches: "))
inch += ft*12
shadow = inch*2.5
shadow_f = round(shadow/12,0)
shadow_i = shadow%12
print("Your shadow at 3pm for your height would be "+str(shadow_f)+" feet, and "+str(shadow_i)+" inches")