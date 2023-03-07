bill=float(input("What was the bill?"))
tip=int(input("What is the tip you want to give?10,12, or 15?"))
people= int(input("How many people to split the bill?"))
tip_percent= tip /100
final_amount=float(bill + bill*tip_percent/people)
print(final_amount)