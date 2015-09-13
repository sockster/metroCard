
#	> > > > > > 		SECTION 1
#							What is on card now: - money
#												 - # of rides
#							


new_card = 0
card_value = 0

new_card = raw_input("Is this a new card?\n")

if (new_card == "Y") or (new_card == "y"):
	orig_amt = 1.00		# $1 charged for new card
elif (new_card == "N") or (new_card == "n"):
	orig_amt = float(raw_input("What is the value on your card now?\n"))
	orig_amt = round(orig_amt, 2)
	rides = int(card_value / 2.75)
	print "Right now your card has %d rides remaining" % rides
else:
	print "Please enter \"Y\" or \"N\" \n"
	orig_card()
print "Print orig_amt: $",orig_amt


#	> > > > > > 		SECTION 2
#							Preferred amt to be added

add_amt = float(raw_input("How much do you want to add to your card?\n"))	# cust_pref now a decimal (tested ok)


#							IF < $5.50, no 11% bonus

if add_amt <= 5.50:
	new_NoBonus = orig_amt + add_amt
	NoBonus_rides = new_NoBonus / 2.75
	new_add = add_amt
	while NoBonus_rides != int(NoBonus_rides) and (new_add < 5.50):
		new_NoBonus = new_add + orig_amt
		print "Print new_NoBonus"
		print new_NoBonus
		new_add = new_add + .05
		print "Print new_add"
		print new_add
		
	print "If you add $%0.2f instead," % new_add
	print "you'll have %i rides and zero remaining on your card" % NoBonus_rides
else:
	print "Adding more than $5.50 will give you an 11% bonus!"
	chasing_dory_up()
		


#	> > > > > > 		SECTION 3
#							

def chasing_dory_up():

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
		
	print "Dory caught - upstream!"
	print "For a zero remainder, you should add $%s" % new_add
	print "Which will give you a bonus of $%s" % new_bonus_only
	print "And a MetroCard balance of $%s" % new_total
	print "Which means you'll have %i rides with no remaining money on your card!" % new_rides
	chasing_dory_down()

#	> > > > > > 		SECTION 2 - END
#	> > > > > > 		SECTION 2a

def chasing_dory_down():
	print "Chasing Dory\n$", add_amt
	#	re-calcs for pertinent vars
	new_sub = add_amt
	new_sub = new_sub + .05
	new_bonus_only = round(new_sub * .11 / .05) * .05
	# new_bonus_only = (new_sub * .11)
	new_bonus_only = round(new_bonus_only,2)
	new_bonus = new_sub + new_bonus_only
	new_total = orig_amt + new_bonus
	new_rides = new_total / 2.75
	new_remainder = new_total % 2.75
	intNew_rides = int(new_rides)
	

	while new_rides != intNew_rides and (new_sub > 0.00):
		# (new_remainder != 0 or new_remainder != 2.75)
		new_sub = new_sub - .05
		new_bonus_only = round(new_sub * .11 / .05) * .05
		new_bonus_only = round(new_bonus_only,2)
		new_bonus = new_sub + new_bonus_only
		new_total = orig_amt + new_bonus
		new_rides = round(new_total,2) / 2.75
		new_remainder = new_total % 2.75
		intNew_rides = int(new_rides)

		
		
				
		# = = = = = = = =>  PRINT SECTION
		print "Print new_sub", new_sub
		print "Print new_bonus_only", new_bonus_only

		print "Print new_bonus", new_bonus
		print "Print new_total", new_total
		print "Print formatted new_rides: %.2f" % new_rides
		print "Print new_rides", new_rides
		print ""
		# = = = = = = = =>  PRINT SECTION END
		
	print "Dory caught - downstream!"
	print "For a zero remainder, you should add $%s" % new_sub
	print "Which will give you a bonus of $%s" % new_bonus_only
	print "And a MetroCard balance of $%s" % new_total
	print "Which means you'll have %i rides with no remaining money on your card!" % new_rides

#	> > > > > > 		SECTION 2a - END









if __name__ == "__main__":




#  END OF COMMENTING FOR TESTING		

	print "End of File"
