


#		RUN FILE - .05 is adding to amt, but REMAINDER is showing 0.803 




single_fare = 2.75
orig = raw_input("how much on your current card?\n")
addl = raw_input("how much do you want to add to card?\n")
orig_amt = float(orig)	# $ on card now - amt only
add_amt = float(addl)	# preferred $ to add - amt only
bonus = add_amt + (add_amt * .11)	# add'l amt including bonus
total = orig_amt + bonus	# orig amt + (add'l amt) + bonus
rides = total / single_fare	#also use for start number in figuring best amt t/b added
remainder = total % single_fare
rides_remainder = int(100 * remainder)
new_rides_remainder = int(100 * (add_amt % single_fare))



#	> > > > > > 		SECTION 1	to "if" - Queries: current amt, addl to add, # rides, will there be remainder of $$$?
#	> > > > > > 		SECTION 2	"else" - if remainder $$$, go to metroplus to figure out even amts to add for 0 remainder


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

import math
def metroplus():
	add_amt = float(addl)
	while (remainder != 0) and (add_amt < 100):
		print "New amount to add is %.2f" % add_amt
		print "Remainder is ", remainder
		print "Print add_amt:", add_amt
		add_amt = add_amt + .05

		bonus = add_amt + (add_amt * .11)	# add'l amt including bonus
		total = orig_amt + bonus	# orig amt + (add'l amt) + bonus
#		remainder = total % single_fare
		print "Print bonus:", bonus
		print "Print total:", total
#		print "Remainder is ", remainder
	print "We're done here!"	


#	START ABOVE
#		Q: Why does remainder remain the same throughout?
#			w/o commented lines 49 & 52, Py insists remainder called before assigned







"""


#	START HERE !!!
# if ORIG_AMT <= 2.75:
#	RIDES_ADDING			--> # rides being added: BONUS (add amt + 11%) / 2.75, round to nearest .05
#	+ 1 (to round up for amt originally on card)
# else:
#	RIDES_CURRENT + RIDES_ADDING			

		
		



#			FROM ORIGINAL FILE (seems to work for getting floor & ceiling)
#			COMMENTED FOR TESTING FOR MATH

# math - floor & ceil:
# CLOSEST number BELOW num or expression divided by divisor
# math.floor(a-number-or-expression)  -  in this case, looking for amt to add divided by 2.75

import math
def addl_value_choices():
	print cust_pref
	pref_plus_bonus = cust_pref + (cust_pref * .11)
	total_actual = pref_plus_bonus + card_value
	y = pref_plus_bonus
	t = y + z
	if total_actual % 2.75 == 0:
		print "Go ahead - the final total will give you exactly %d" % (total_actual / 2.75),
		print "rides"
	else:
#				
		lower = total_actual - math.floor(total_actual / 2.75)
		upper = total_actual + math.ceil(total_actual / 2.75)
		
		print "You can either add %0.2f" % lower
		print "for %d rides" % math.floor(total_actual / 2.75)
		print "or you can add %0.2f" % upper
		print "for %d rides" % math.ceil(total_actual / 2.75)
	
#			END FROM ORIGINAL FILE

"""


# var_statmts - THE NEW SHIT ... kickin' it old school (sep raw_input stmt from ans)

#	var_statements: define the vars and do the initial %age math
def var_statemts():
	print "on card now"
	x = float(raw_input())			# on card now amt
	print "to add to card"
	y = float(raw_input())			# adding amt
	y2 = y + round((y * .11),2)		# adding amt + 11% bonus
	print "Print y2:", y2
	print ("{:.2f}".format(y2))
	z = x + y2
	print "Print z:", z
	print ("{:.2f}".format(y2))

""" 08.23.15	Done; Next; Waiting:
	D - Ask how much on card - save as var
	D - Ask how much to add - save as var
	D - Add 11% bonus to add amt - save as var
	D - Add to orig amt on card - save as var
	D - Divide by fare ($2.75)
	D - Return number of rides
	D - Return amt left on card
	D - If amt != 0, go to metroplus() for...
	N - If amt < 2.75
"""	
	
#var_statemts()



	
metrocard()




