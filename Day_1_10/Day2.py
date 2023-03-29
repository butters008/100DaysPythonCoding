print("This is tip calculator")
bill = float(input("What was the bill? "))
people = int(input("How many people"))
tip = int(input("How much of a tip do you want to give? 10% 12% 15% "))

tipResult = bill * (tip / 100)
total = (bill + tipResult) / people

print("Your bill is ")
print(round(total, 2))
