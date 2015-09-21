new_card = 0
card_value = 0






#	> > > > > > 		SECTION 1
#							What is on card now: - money
#												 - # of rides
#							

def card_status():
	new_card = raw_input("Is this a new card?\n")

	if (new_card == "Y") or (new_card == "y"):
		orig_amt = 1.00
		print "The cost of a new card is $%0.2f" % orig_amt

	elif (new_card == "N") or (new_card == "n"):
		orig_amt = float(raw_input("What is the value on your card now?\n"))
		print "print orig_amt", round(orig_amt,2)		# TESTING ONLY - T/B DELE
		rides = (orig_amt / 2.75)
		rides = round(rides,2)
		print "print rides", rides						# TESTING ONLY - T/B DELE
		print "Print type", type(rides)					# TESTING ONLY - T/B DELE
		print "Right now your card has %s rides remaining" % int(rides)

	else:
		print "Please enter \"Y\" or \"N\" \n"
		card_status()

# # # # # # # # # # # GOOD TO HERE # # # # # # # # # # # 





#	> > > > > > 		SECTION 2
#							What to add: 	- money
#											- # of rides

# > > > > NEXT STEPS:
#		How much do you want to add?
#		  - check if div by $0.05
#		  - if < $5.50, no bonus, i.e., straight addition
#		  - else addl 11% bonus to amt adding
#		Return total of card after amt added, and # of rides







if __name__ == "__main__":
	card_status()

	addl_amt = raw_input("How much do you want to add?\n")




#   commented for testing
# orig_amt = float(raw_input("What is the value on your card now?\n"))
#orig_amt = round(orig_amt, 2)
#rides = int(card_value / 2.75)