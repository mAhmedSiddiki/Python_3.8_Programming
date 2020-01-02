#import now time
import datetime

time = datetime.datetime.now()
print("Hour: ", time.hour)
print("Minute: ", time.minute)
print("Second: ", time.second)
print("Microsecond: ", time.microsecond)



#import now date
from datetime import date

date = date.today()
print("\nToday's Date: ",date)