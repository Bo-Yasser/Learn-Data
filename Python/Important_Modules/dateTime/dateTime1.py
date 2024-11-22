


import datetime

# print(dir(datetime))
# print(dir(datetime.datetime))
# print(dir(datetime.datetime.now()))
#################################################################

print(datetime.datetime.now())


print("#"* 50)
#################################################################

print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)
print(datetime.datetime.now().hour)
print(datetime.datetime.now().minute)
print(datetime.datetime.now().second)
print(datetime.datetime.now().microsecond)


print("#"* 50)
#################################################################

print(datetime.datetime.min)
print(datetime.datetime.max)


print("#"* 50)
#################################################################

print(datetime.datetime.now().time().min)
print(datetime.time.min)

print(datetime.datetime.now().time().max)
print(datetime.time.max)

print("#"* 50)
#################################################################

print(datetime.datetime.now().date().min)
print(datetime.date.min)

print(datetime.datetime.now().date().max)
print(datetime.date.max)

print("#"* 50)
#################################################################

print(datetime.datetime.now().date())
print(datetime.datetime.now().date().year)
print(datetime.datetime.now().date().month)
print(datetime.datetime.now().date().day)

print(datetime.datetime.now().time())
print(datetime.datetime.now().time().hour)
print(datetime.datetime.now().time().minute)
print(datetime.datetime.now().time().second)
print(datetime.datetime.now().time().microsecond)

print("#"* 50)
#################################################################

print(datetime.datetime(1982, 10, 25))
print(datetime.datetime(1982, 10, 25, 10, 45, 55, 150364))


birthDay = datetime.datetime(1982, 10, 25).date()

dateNow = datetime.datetime.now().date()

print(f"My Birthday Is {birthDay} And", end=" ")
print(f"Date Now Is {dateNow}")

print(f"I Lived For {(dateNow - birthDay).days} Days.")

print("#"* 50)
#################################################################

