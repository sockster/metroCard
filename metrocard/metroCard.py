"""

A Pay-Per-Ride MetroCard costs



= = = = = = = = = = = = = = = = = = PARAMETERS
- The fare for a subway or local bus ride is $2.75.
- Initial MetroCard purchase can be from $5.50 to $80 
	+ $1 for new card
- Put $5.50 or more on your card and receive an 11 percent bonus. 
	For example, a $20 purchase gives you $22.20 on your card. 
	Refill your card to use the balance.
- Given current MC value, how much s/b added to have value come out divisible by 2.75?
	

= = = = = = = = = = = = = = = = = = VALUES/VARIABLES NEEDED
fare = 2.75							Return:
card_value = float(raw_input)		current card value (will be 0 or current amount on card)
									number of rides left on card now (if not a new card)
cust_pref = int(raw_input)			how much do you want to add (approx) to reach even # of ride
card_value_final = int(value)		amount to add - for 1 under and 1 over preferred amt - for even # of ride
									include $1 for new card if applicable

= = = = = = = = = = = = = = = = = = OUTLINE OF STEPS

- VALUE OF CURRENT CARD
	new card?
	if yes:
		card_value  = 0+= 1
		call addl_value  MOD
	else:
		call addl_value  MOD


- ADDL_VALUE MOD
	^ how much value is cust adding? 	(cust_pref = raw_input)
	if amt not divisible by .05:
		print "Values must be 5-cent increments"
	elif > $80:
		print "Sorry, cannot add more than $80 to your card."
	elif <= $5.50:
		call value_small()
	else:
		call value_big()


- VALUE_SMALL MOD
	^ add card_value
	^ what is lowest amt to add to have total divisible by 2.75?
	^ print that amount

		
- VALUE_BIG MOD
	^ add card_value
	^ add 11% of cust_pref
	^ what are next 3 amounts that are divisible by 2.75?
	^ throw each of the 3 amounts into list, print list
	
	
		
= = = = = = = = = = = = = = = = = = END OF OUTLINE
"""





def orig_card():
	if (new_card == "Y") or (new_card == "y"):
		card_value = 0
		addl_value()
	elif (new_card == "N") or (new_card == "n"):
		card_value = float(raw_input("What is the value on your card now?\n"))
		print "Right now your card has",
		print int(card_value / 2.75),
		print "rides remaining"
		addl_value()
	else:
		print "Please enter \"Y\" or \"N\" \n"


def addl_value():
	cust_pref = float(raw_input("How much do you want to add to your card?\n"))	# cust_pref now a decimal (tested ok)
	if (cust_pref * 100) % 5 != 0:
		print "Values must be in 5-cent increments"
		addl_value()
	elif cust_pref < 5.50 or cust_pref > 80.00:
		print "The value you add to your MetroCard must be between $5.50 and $80.00."
		addl_value
	else:
		print """Ok, the amount we'll be adding will be approximately $%0.2f in order 
to reach an even number of rides""" % cust_pref
	



if __name__ == "__main__":
	new_card = raw_input("Is this a new card?\n")

	orig_card()
	
