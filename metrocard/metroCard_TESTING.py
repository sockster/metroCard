


#		RUN FILE - .05 is adding to amt, but REMAINDER is showing 0.803 




single_fare = 2.75
orig = raw_input("how much on your current card?\n")
addl = raw_input("how much do you want to add to card?\n")
orig_amt = float(orig)	# $ on card now - amt only
add_amt = float(addl)	# preferred $ to add - amt only
bonus = add_amt + (add_amt * .11)	# add'l amt including bonus
total = orig_amt + bonus	# orig amt + (add'l amt) + bonus
rides = total / single_fare
remainder = total % single_fare
rides_remainder = int(100 * remainder)
new_rides_remainder = int(100 * (add_amt % single_fare))



#	> > > > > > 		SECTION 1	to "if" - Queries: current amt, addl to add, # rides, will there be remainder of $$$?
#	> > > > > > 		SECTION 2	"else" - if remainder $$$, go to metroplus to figure out even amts to add for 0 remainder
	

def metrocard():
	print orig
	print addl
	print "your total will be %.2f" % total
	print "you will have %i rides" % rides
	if rides_remainder == 0:
		print "this amount will leave you with $0 on your metrocard!"		# END OF SECTION 1
	else:
		print "but you will have %.2f remaining on your card - go to metroplus()" % remainder
		metroplus()
	

def metroplus():
	add_amt = float(addl)
	while (remainder != 0) and (add_amt < 100.00) :
		print "New amount to add is %.2f" % add_amt
		print "Remainder is ", remainder
		add_amt = add_amt + .05

	print "We're done here!"	







	
metrocard()




