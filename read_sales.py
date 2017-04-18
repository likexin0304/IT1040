def main():
    # Open the sales.txt file for reading.
    sales_file = open( 'sales.txt', 'r')
    # From program 6-12
    # Initialize an accumulator to 0.0
    total = 0.0
    # From program 6-12
    # Initialize a variable to keep count of the sales.
    count = 0
    #From program 6-12
    print('Here are the sales for each day entered')
    # Read all the lines from the file.
    # Get the values from the file and total them.
    for line in sales_file:
        #Convert a line to a float.
        amount = float(line)
        # Add 1 to the count variable.
        count += 1

        # Display the sales.
        #print("{0:.2f}".format(a))
        print('Day #', count, ': ', format(amount, '.2f'), sep='')

        # Add the time to total.
        total += amount
    # Close the file
    sales_file.close()

    #From program 6-12
    # Display the total of the running times.
    print('The total amount in sales is', format(total, '.2f'))

    # Call the main function

main()
