#Write a program to print the number of days
#remaining for new year
from datetime import datetime
newyear = datetime(2026,1,1)
currdate = datetime.now()
diff = newyear - currdate
print(diff.days)