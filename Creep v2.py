import datetime
now = datetime.datetime.now()

year = int("%d" % now.year)

name = input("What is your name? ")
dob = int(input("What year were you born? "))
print(name, "you will turn", year-dob, "this year.")