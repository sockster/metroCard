#Project: Verifying a User's Age
#	Sometimes a site might not be appropriate for people of a certain age. 
#	For times like these, we'll need a program that verifies the user's age, to ensure that they can view the site.
#GOAL
#	Create a program that makes sure that the user is of an age of your choice (18 being the default).
#SUB GOALS
#	Have the user input their birthday, and use that to determine if they are old enough
#	If the user is not of an appropriate age, suggest a different website/websites that would be appropriate for them



import datetime

now = datetime.datetime.now()
t_month = now.month
t_day = now.day
t_year = now.year

months_d = {
	"jan":"1",
	"feb":"2",
	"mar":"3"
}




print "Today is %d" % t_month



def old_enough():
	bdate = raw_input("In order to verify your age, please enter your birthdate (mm/dd/yyyy)")


	if len(bdate) == 10:
		print (int(now.year)) - (int(bdate[6:]))
	else:
		print "Please use the \"mm/dd/yyyy\" format"
		old_enough()
	
old_enough()

