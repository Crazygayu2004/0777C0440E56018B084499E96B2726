import calendar

yr = int(input("Enter year="))
if calendar.isleap(yr):
  print(yr, "is a leap year")
else:
  print(yr, "is not a leap year")
