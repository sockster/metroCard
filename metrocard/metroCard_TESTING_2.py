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
		print "print orig_amt", orig_amt				# TESTING ONLY - T/B DELE
		rides = (orig_amt / 2.75)
		print "print rides", rides						# TESTING ONLY - T/B DELE
		print "Right now your card has %0.2f rides remaining" % rides

	else:
		print "Please enter \"Y\" or \"N\" \n"
		card_status()









card_status()





#   commented for testing
# orig_amt = float(raw_input("What is the value on your card now?\n"))
#orig_amt = round(orig_amt, 2)
#rides = int(card_value / 2.75)