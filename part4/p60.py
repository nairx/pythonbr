from datetime import datetime,date,timedelta
d=date.today()
print(d)
tomorrow = d + timedelta(days=1)
print(tomorrow)
yesterday = d - timedelta(days=1)
print(yesterday)
t1 = datetime(2025,12,12,10,10,10)
t2 = datetime(2025,12,10,10,10,11)
diff = t1-t2
print(diff.days)
print(diff.seconds)
