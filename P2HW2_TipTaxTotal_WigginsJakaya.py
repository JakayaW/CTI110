#CTI-110
#P2HW2 - Tip Tax Total
#Jakaya Wiggins
#2/20/2018

foodCharge = float( input( "Please enter the charge of the food: " ) )

tip = 0.18 * foodCharge

salesTax = 0.07 * foodCharge

total = foodCharge + tip + salesTax

print("Food Charge: $" + format( foodCharge, ",.2f"), "Tip: $" + \
      format( tip, ",.2f" ), "Sales Tax: $" + format( salesTax, ",.2f"), \
      "Total: $" + format( total, ",.2f"))

Please enter the charge of the food: 200
Food Charge: $200.00 Tip: $36.00 Sales Tax: $14.00 Total: $250.00
