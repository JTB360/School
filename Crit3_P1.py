import math
while True: 
    try: 
        meal_cost = float(input("Please enter cost of the meal: ")) 
        break 
# ValueError is used if user enters a non number
    except ValueError: 
        print("Invalid input.") 
meal_tip = meal_cost * .18
meal_tax = meal_cost * .07
cost_total = meal_tip + meal_tax + meal_cost


print ('\nThe cost 18% tip is :',"$", round(meal_tip, 2))
print ('The cost 7% sales tax is :',"$", round(meal_tax, 2))
print ('The total cost plus tip and tax is :',"$", round(cost_total,2))
