


#		RUN FILE - .05 is adding to amt, but REMAINDER is showing 0.803 



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
	print "your total - including original amount and 11 percent bonus will be %.2f" % total
	print "you will have %i rides" % rides

	if rides_remainder == 0:
		print "this amount will leave you with $0 on your metrocard!"		# END OF SECTION 1
	else:
		print "but you will have $%.2f remaining on your card - go to metroplus()" % remainder
		metroplus()




#									Show all in rounded numbers to 2 decimals
#									This is all correct, i.e., returns what's expected
def metroplus():
	print "Print single_fare:", single_fare								# CORRECT
	print "Print 11% bonus amt:", "{:.2f}".format((round(bonus_only / .05) * .05))							
	print "Print bonus:", "{:.2f}".format((round(bonus / .05) * .05))	# CORRECT (rndd to .05 at 2 decimals)
	print "Print total:", "{:.2f}".format((round(total / .05) * .05))	# CORRECT       "
	print "Remainder is ", "{:.2f}".format((round(remainder / .05) * .05))	# CORRECT	"
	# Above is TESTING::c/b/dele




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
print add_amt


#	> > > > > > 		SECTION 2	BACK to FORMULA; BONUS AND TOTAL NOT WORKING ...
#	 		find the closest 0-remainder total

def finding_nemo():
	print "Finding Nemo"
	print add_amt
	print "Nemo found!"	
	chasing_dory()



def chasing_dory():
	print "Chasing Dory"
	print add_amt
	#	re-calcs for pertinent vars
	new_add = add_amt
	new_remainder = total % 2.75
	
	while new_add < 20 and new_remainder != 0:
		new_add = new_add + .05
		new_bonus_only = new_add * .11
		new_bonus = new_add + new_bonus_only
		new_total = orig_amt + new_bonus
		new_rides = new_total / 2.75
		new_remainder = round((new_total % 2.75) / .05) * .05

		print "Print new_add", new_add
		print "Print new_bonus_only", new_bonus_only
		print "Rounded & divided  -->", round(new_bonus_only / .05) * .05
		print "Print new_bonus - rounded", round(new_bonus / .05) * .05
		print "Print new_total - rounded", round(new_total / .05) * .05
		print "Print new_rides - rounded", round(new_rides / .05) * .05
		print "Print new_remainder - rounded", round(new_remainder / .05) * .05
		print ""
		
	print "Dory caught!"	

"""	while add_amt < 50:
		print "New amount to add is %.2f" % add_amt	# CORRECT
		print "Remainder is ", remainder
		print "Print add_amt:", add_amt
		print "Print single_fare:", single_fare		# CORRECT
		print "Print bonus_only", bonus_only 
		print "Print bonus:", bonus					# CORRECT
		print "Print total:", total					# CORRECT
		print "Remainder is ", remainder
		print ""
		print ""
		add_amt = add_amt + .05
"""


finding_nemo()
# =========== >   MATH WORKING; NEXT UP: WHILE STATEMENT W/"and"
#			(currently ignoring "and new_remainder != 0")




	
