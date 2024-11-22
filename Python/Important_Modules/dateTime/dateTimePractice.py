



import datetime
# 1
'''
EXdate = datetime.date(2021, 6, 25)

todayDate = datetime.datetime.now().date()


print(f"Days From {EXdate} To {todayDate} Is => {(todayDate - EXdate).days}")


print(todayDate)
'''


# 2

dateNow = datetime.datetime.now()

print(dateNow.strftime("%Y-%m-%d"))
print(dateNow.strftime("%b %d, %Y"))

print(dateNow.strftime("%d - %b - %Y"))
print(dateNow.strftime("%d / %b / %y"))
print(dateNow.strftime("%d / %B / %Y"))

print(dateNow.strftime("%a, %d %B %Y"))




