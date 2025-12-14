'''Requirements:

    Define time_slots as a list with times of day (e.g., "Morning", "Midday", "Afternoon", "Evening").
    Use a loop to prompt the user for heart rate (in BPM) at each time slot.
    Create a multi-level list heart_rates to store the time slots and their corresponding heart rates.
    Calculate the average heart rate and display it.
'''



#definin the time slot list. Similar to the blood sugar program
time_slots = ["Morning", "Midday", "Afternoon", "Evening", "Night"]

#counter variable 
total = 0

#implementing the multi list to get the time and beats 
heart_rates = []

# Get heart rate info from user
for time in time_slots:
    bpm = int(input(f"Please enter your heart rate for {time} (beats per min): "))
    #multi level list and append lke the blood sugar program as well
    heart_rates.append([time, bpm])

# Print heart rates and calculate total
for item in heart_rates:
    print(f"At {item[0]}, your heart rate was {item[1]} BPM")
    total += item[1]

# Calculate and get the average
avg = total / len(heart_rates)
print(f"Your average heart rate today was: {avg:.1f} BPM")