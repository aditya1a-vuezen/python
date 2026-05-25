print("Welcome to Tip Calculator")
bill = float(input("What was the total bill?"))
print(bill)
tip = int(input("How much tip would you like to give? 10,15, or 20"))
print(tip)
people = int(input("How many  people to split the bill ?"))
Each_person_should_pay = tip / 100 * bill + bill
Each_person_should_pay = round(Each_person_should_pay, 2 )
print(f"Each person should pay = {Each_person_should_pay}$ ")

