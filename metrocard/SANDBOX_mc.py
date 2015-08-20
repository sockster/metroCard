# Plea to the Python gods - and goddesses - to make math magic for me		
#	> > > > > > 		THE MATH

# FORMULA - where:
# x = amt on card
# y = amt to add - t/b raw_input
# 	(y + (y * .11) + x) / 2.75 = 0

#	> > > > > > 		END OF THE MATH



"""		IT. COULD. WORK!!!
# import decimal
def testing():
	x = 4
	y = 24
	z = y / x
	print ("{:.2f}".format(z))
#	print("{:.2f}".format(3.1415926))		#from string formatting ckbk
	
"""

def testing():
	x = raw_input("on card now\n")			# to be fixed amt
	y = raw_input("to add to card\n")		# to be var, added to by .05 until div by 2.75

	x = float(x)
	y = float(y)
	z = 0
#	while z <= 10:
	if "{:.2f}".format((y + (y * .11) + x) / 2.75) != 0:
		y += .05
#		z += 1
	else:
		print "outta' heah!"
	print "{:.2f}".format(x), "This is x"
	print "{:.2f}".format(y), "This is y"
	print "{:.2f}".format(z), "This is z"

#	THIS IS WHERE I STOPPED (ABOVE)
#	THIS RETURNS:
#	 .80 as x
#	7.80 as y
#	0.00 as z

testing()

