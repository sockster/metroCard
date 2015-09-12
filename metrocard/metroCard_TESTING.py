

#	NOTE: comment on WHY something is, not what it is
#		ex: x = 5   doesn't need # var x = 5   (duh)
#					but ok to comment x = velocity








#	> > > > > > 		SECTION a	assigning vars
single_fare = 2.75
orig = raw_input("how much on your current card?\n")
addl = raw_input("how much do you want to add to card?\n")
orig_amt = float(orig)				# $ on card now - amt only
add_amt = float(addl)				# preferred $ to add - amt only
bonus_only = add_amt * .11
bonus = add_amt + (add_amt * .11)	# add'l amt including bonus
total = orig_amt + bonus			# orig amt + (add'l amt) + bonus
rides = total / single_fare			# also use for start number in figuring best amt t/b added
remainder = total % single_fare
rides_remainder = int(100 * remainder)
new_rides_remainder = int(100 * (add_amt % single_fare))




#	> > > > > > 		SECTION 1	Sum of: current amt, addl to add, and bonus (show # rides)
#									if remainder, go to metroplus(),
#									(for suggested amts to add for no remainder)

#		
def metrocard():
	print orig
	print addl
	print "your total - including original amount and 11 percent bonus - will be $%.2f" % total
	print "you will have %i rides" % rides

	if rides_remainder == 0:
		print "this amount will leave you with $0 on your metrocard!"		# END OF SECTION 1
	else:
		print "but you will have $%.2f remaining on your card - go to multis\n\n" % remainder


"""
#	> > > > > > 		SECTION 1a		BREAK from FORMULA; create list containing multiples of 2.75
metrocard()


#	show 50 multiples of 2.75	
multis = []
x = 1.00
while x < 50:	# 50 for testing purposes only
	y = x * single_fare
	multis.append(y)
	x += 1
print multis
print ""
print ""

"""



#	> > > > > > 		SECTION 2	BACK to FORMULA; BONUS AND TOTAL NOT WORKING ...
#	 		find the closest 0-remainder total

def finding_nemo():
	print "Finding Nemo\n$", add_amt
	print "Nemo found!\n"	
	chasing_dory()



def chasing_dory():
	print "Chasing Dory\n$", add_amt
	#	re-calcs for pertinent vars
	new_add = add_amt
	new_add = new_add + .05
	new_bonus_only = round(new_add * .11 / .05) * .05
	# new_bonus_only = (new_add * .11)
	new_bonus_only = round(new_bonus_only,2)
	new_bonus = new_add + new_bonus_only
	new_total = orig_amt + new_bonus
	new_rides = new_total / 2.75
	new_remainder = new_total % 2.75
	intNew_rides = int(new_rides)
	

	while new_rides != intNew_rides and (new_add < 27.00):	# "27.00" for testing only
		# (new_remainder != 0 or new_remainder != 2.75)
		new_add = new_add + .05
		new_bonus_only = round(new_add * .11 / .05) * .05
		new_bonus_only = round(new_bonus_only,2)
		new_bonus = new_add + new_bonus_only
		new_total = orig_amt + new_bonus
		new_rides = round(new_total,2) / 2.75
		new_remainder = new_total % 2.75
		intNew_rides = int(new_rides)

		
		
				
		# = = = = = = = =>  PRINT SECTION
		print "Print new_add", new_add
		print "Print new_bonus_only", new_bonus_only

		print "Print new_bonus", new_bonus
		print "Print new_total", new_total
		print "Print formatted new_rides: %.2f" % new_rides
		print "Print new_rides", new_rides
		print ""
		# = = = = = = = =>  PRINT SECTION END
		
	print "Dory caught!"
	print "For a zero remainder, you should add $%s" % new_add
	print "Which will give you a bonus of $%s" % new_bonus_only
	print "And a MetroCard balance of $%s" % new_total
	print "Which means you'll have %i rides with no remaining money on your card!" % new_rides



finding_nemo()



#	NEXT STEPS:

#		format print section to return to 2 decimals
#		put all the pertinent parts into the original file, which has
#		the opening frills, and 
#		the if statement to determine whether original amounts would result in zero remainder
#		THEN, hook it into a front-end interface




	
