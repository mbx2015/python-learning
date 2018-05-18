import datetime, calendar

print('Now: ', datetime.datetime.now())
print('Today: ', datetime.datetime.today())
print('UTC now: ', datetime.datetime.utcnow())

FIELDS = [
    'year', 'month', 'day',
    'hour', 'minute', 'second',
    'microsecond'
]

for attr in FIELDS:
    print('{:15}: {}'.format(attr, getattr(datetime.datetime.now(), attr)))

t = datetime.time(1, 2, 3)
print('t:', t)

d = datetime.date.today()
print('d:', d)

dt = datetime.datetime.combine(d, t)
print('dt: ', dt)

print('\n=== Calendar ===\n')
c = calendar.TextCalendar(calendar.SUNDAY)
c.prmonth(2018, 6)

