# Chalakorn Manopirom
# Let's find out how many second since you was born.

import datetime
y = input("What is the year that you war born:")
y = int(y)
m = input("What is the month that you was born:")
m = int(m)
d = input("What is the day that you war born:")
d = int(d)
h = input("What is the hour that you war born:")
h = int(h)
mi = input("What is the minute that you war born:")
mi = int(d)


birthdate = datetime.date(y,m,d)
birthtime = datetime.time(h,mi)
birthday = datetime.datetime.combine(birthdate, birthtime)
now = datetime.datetime.now()

time_passed = now - my_birthday
how_many_seconds = time_passed.total_seconds()
print ("That is ",how_many_seconds,"seconds since you was born")
