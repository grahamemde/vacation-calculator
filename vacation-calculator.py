# Vacation Calculator; Author - Graham Emde; Created - 2017

from __future__ import division
from datetime import *

print "\n"
print "====================================================="
print "VACATION CALCULATOR"
print "Graham Emde, 26 March 2017"
print "-----------------------------------------------------"

def parseDate(retry):
	if retry:
		print("Date didn't parse. Please try again, using the format mm/dd")
	else:
		print("\nWhat month and day would you like calculate your available vacation days for? Enter month as an integer.")
		month = int(raw_input())
		print("\nEnter day as an integer.")
		day = int(raw_input())
	try:
		dateOfInterest = date(currentYear, month, day)
		return dateOfInterest
	except ValueError:
		parseDate(true)

#Get year
now = datetime.now()
currentYear = now.year

#Get responses
print("\nHow many vacation days do you get in " + str(currentYear) + "?")
leaveDays_Total = int(raw_input())
print("\nHow many vacation days have you spent already?")
leaveDays_Spent = int(raw_input())
print("\nDo you want to calculate your available vacation days as of today? y/n")
response = raw_input()

#Date of interest
dateOfInterest = None
if(response.lower() == "y" or response.lower() == "yes"):
	now = datetime.now()
	dateOfInterest = date(currentYear,now.month,now.day)
else:
	dateOfInterest = parseDate(False)

#Get the total number of days in the year (since it's 366 in leap years)
startOfYear = date(currentYear,1,1)
endOfYear = date(currentYear,12,31)
daysInYear = (endOfYear - startOfYear).days + 1

#Get the accrual rate per day
rate = leaveDays_Total/daysInYear

#Get the number of passed days from date of interest (or from today)
if dateOfInterest is None:
	dateOfInterest = today
passedDays = (dateOfInterest - startOfYear).days

#Get accrued to date
accruedToDate = round(passedDays * rate, 2)

#Results
print "RESULTS:"
print "-----------------------------------------------------"
print "DAYS AVAILABLE ON " + str(dateOfInterest)
print "-----------------------------------------------------"
print "\tTotal days accrued:          " + str(accruedToDate)
print "\tDays spent so far:           " + str(leaveDays_Spent)
print "\tDays remaining:              " + str(accruedToDate - leaveDays_Spent)
print "====================================================="
print "TOTAL"
print "-----------------------------------------------------"
print "\tTotal vacation days in " + str(currentYear) + ": " + str(leaveDays_Total)
print "\tDays spent so far:           " + str(leaveDays_Spent)
print "\tTotal remaining in " + str(currentYear) + ":     " + str(leaveDays_Total - leaveDays_Spent)
print "====================================================="