print("Welcome to Bill Calculator Project!")

# converting input to appropriate numerical values
bill_total = float(input("How much is the total bill?\n"))
tip = float(input("How much tip do you want to give?\n"))
split = int(input("How many people will this bill be splitted?\n"))

# computations
tip_total = bill_total * tip/100
bill_total_shared = (bill_total + tip_total)/split
bill_split = bill_total / split
final_amount = "{:.2f}".format(bill_total_shared)

print(f"Total amount per person is:${final_amount}")

