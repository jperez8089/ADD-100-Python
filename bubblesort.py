'''Task:

    Prompt the user to enter five names.
    Store the names in a list.
    Sort the list using the Bubble Sort algorithm.
    Reverse the sorted list using a Python list method.
    Print both the sorted and reversed lists.
'''

# getting the user input by havngt the user to enter five names and storing in list
enter_name = []

#for loop fo the iterations
for i in range(5):
    name = input("Enter a name: ")
    enter_name.append(name)

# using bubble structure from provided reference 
swapped = True
while swapped:
    swapped = False
    for i in range(len(enter_name) - 1):
        if enter_name[i] > enter_name[i + 1]:
            enter_name[i], enter_name[i + 1] = enter_name[i + 1], enter_name[i]
            swapped = True

#sorting the list print 
print("list:", enter_name)

#reverse the sorted list
enter_name.reverse()

#reversed list
print("reversed:", enter_name)