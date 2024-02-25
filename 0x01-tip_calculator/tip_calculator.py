#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

#total_bill = input("What was the total bill? $")
#tip_percentage = input("How much tip would you like to give? 10, 12, 0r 15? ")
#people_split = input("How many people to split the bill? ")
#total_bill_float = float(total_bill)
#tip_percentage_float = float(tip_percentage)
#people_split_int = int(people_split)
#tip_percentage_float = tip_percentage_float / 100
#tip_percentage_float = tip_percentage_float + 1
#total_bill_float = total_bill_float * tip_percentage_float
#total_bill_float = total_bill_float / people_split_int
#total_bill_float = round(total_bill_float, 2)
#print(f"Each person should pay: ${total_bill_float}")
#print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))
tip_percentage = float(input("How muchh would you like to give? 10, 12, 0r 15? "))
people_split = int(input("How many people are splitting the bill? "))
new_tip_percentage = tip_percentage / 100 + 1
new_total_bill = total_bill * new_tip_percentage
new_total_bill = round(new_total_bill / people_split, 2)
print(f"Each person should pay: ${new_total_bill}" )
