hp=1000000
credit= True

if credit:
    downpayment = int(hp)*.10
    print ("Your downpayment is",downpayment)
else:
    downpayment= int(hp)*.2
    print ("Your downpayment is $"+downpayment)