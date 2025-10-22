# a program to convert kg to lbs 

kg_value_1 = 20 
kg_value_2 = 30 
kg_value_3 = 40 
kg_value_4 = 50 

# Converting lbs to kg 
# lb = kg * 2.20462


conversion_value = 2.20462

#calculating each value while also using the conversion value variable 

lb_value_1 = kg_value_1 * conversion_value
lb_value_2 = kg_value_2 * conversion_value
lb_value_3 = kg_value_3 * conversion_value
lb_value_4 = kg_value_4 * conversion_value

#implementing f string to keep the decimals down to 2. final printing of conversion 
print(f"{kg_value_1} kg is equal to {lb_value_1:.2f} lbs")
print(f"{kg_value_2} kg is equal to {lb_value_2:.2f} lbs")
print(f"{kg_value_3} kg is equal to {lb_value_3:.2f} lbs")
print(f"{kg_value_4} kg is equal to {lb_value_4:.2f} lbs")
