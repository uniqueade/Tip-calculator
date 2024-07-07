# A Tip calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill"))
tip = int(input("How much tip will you like to give"))
people = int(input('How many people to split the bill'))    
tip_as_percent = tip/100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = f"{round(bill_per_person,2):.3f}"
print(f"Each person should pay:${final_amount}")
