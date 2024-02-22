import datetime
x=datetime.datetime.now()
b=datetime.datetime.now()-datetime.timedelta(days=4)
print(x-b)