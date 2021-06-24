## 1. Introduction ##

from csv import reader
potus_visitors_2015 = open('potus_visitors_2015.csv')
read_potus_visitors_2015 = reader(potus_visitors_2015)
list_potus_visitors_2015 = list(read_potus_visitors_2015)
potus = list_potus_visitors_2015[1:]
print(potus)

## 3. The Datetime Module ##

import datetime as dt

## 4. The Datetime Class ##

import datetime as dt

ibm_founded = dt.datetime(1911,6,16)

man_on_moon = dt.datetime(1969,7,20,20,17)
#ano, mes e dia, hora minuto, segundo

print(ibm_founded)
print(man_on_moon)

## 5. Using Strptime to Parse Strings as Dates ##

# The `potus` list of lists is available from
# the earlier screen where we created it
import datetime as dt

date_format = "%m/%d/%y %H:%M"
for column in potus:
    appt_start_date = column[2]
    convert = dt.datetime.strptime(appt_start_date, date_format)
    column[2] = convert
    print(column[2])

## 6. Using Strftime to format dates ##

import datetime as dt

visitors_per_month = {}
format_date = "%B, %Y"
for row in potus:
    appt_start_date = row[2]
    appt_start_date = appt_start_date.strftime(format_date)
    if appt_start_date not in visitors_per_month:
        visitors_per_month[appt_start_date] = 1
    else:
        visitors_per_month[appt_start_date] +=1

## 7. The Time Class ##

import datetime

appt_times = []
for row in potus:
    appt_dt = row[2]
    dt_time = appt_dt.time()
    appt_times.append(dt_time)

## 8. Comparing time objects ##

min_time = min(appt_times)
max_time = max(appt_times)
print(min_time, max_time)

## 9. Calculations with Dates and Times ##

dt_1 = dt.datetime(1981, 1, 31)
dt_2 = dt.datetime(1984, 6, 28)
dt_3 = dt.datetime(2016, 5, 24)
dt_4 = dt.datetime(2001, 1, 1, 8, 24, 13)

answer_1 = dt_2 - dt_1
answer_2 = dt_3 + dt.timedelta(days=56)
answer_3 = dt_4 - dt.timedelta(seconds=3600)
print(answer_1, answer_2, answer_3)

## 10. Summarizing Appointment Lengths ##

appt_lengths = {}

for row in potus:
    end_date = row[3]
    end_date = dt.datetime.strptime(end_date, "%m/%d/%y %H:%M")
    row[3] = end_date
    start_date = row[2]
    length = end_date - start_date
    if length not in appt_lengths:
        appt_lengths[length] = 1
    else:
        appt_lengths[length] +=1
        
        
min_length = min(appt_lengths)
max_length = max(appt_lengths)
print(max_length)
print(min_length)

print(appt_lengths)