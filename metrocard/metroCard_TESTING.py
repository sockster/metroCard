orig = raw_input("how much on your current card?\n")
addl = raw_input("how much do you want to add to card?\n")
addl = float(addl)
bonus = addl + (addl * .11)
total = float(orig) + bonus
rides = total / 2.75

def metrocard():
	print orig
	print addl
	print "your total will be %.2f" % total
	print "you will have %.2f rides" % rides
	if  == 0:
		print "this amount will not leave you with money on your metrocard!"
	else:
		print "go to metroplus()"
#		metroplus()
	
	
def metroplus():
	suggest_rides = rides
	suggest_addl = addl

	while suggest_rides != 0:
		suggest_addl + .05
	
	







	
metrocard()