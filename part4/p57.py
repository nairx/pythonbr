from datetime import date
d=date(2025,1,10)
# d=date.today()
print(d)
print(d.year)
print(d.day)
print(d.month)
print(d.weekday())
print(d.strftime("%m %d %y"))
print(d.strftime("%B %d %y"))
print(d.strftime("%B %d %Y"))

