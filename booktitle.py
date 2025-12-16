def main():
    #max count and counte variable. keeping an open titles 
    counter = 0
    max_count = 10
    titles = []

#while true so so that it stops on the break 
    while True:
        user_input = input(" enter a book title: ")
        title = user_input.title()

        # Check if the input is empty or only spaces
        if not title.strip():
            print("error - enter a valid book")
            continue
#converting it to the right casing
        titles.append(title)
        #counter variable increment 
        counter += 1

        # thss should stop the count at some point 
        if counter == max_count:
            break

    #using the sort to make it alphabetically 
    titles.sort()

    # Print the sorted titles
    print("Sorted book titles:")
    for t in titles:
        print(t)


main()