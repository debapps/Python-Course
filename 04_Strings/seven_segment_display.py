def simulate_seven_segment(input_data):
    # Define the segments for each digit 0-9
    digit_design_data = {
        '0': [" ### ", "#   #", "#   #", "#   #", " ### "],
        '1': ["  #  ", "  #  ", "  #  ", "  #  ", "  #  "],
        '2': [" ### ", "    #", " ### ", "#    ", " ### "],
        '3': [" ### ", "    #", " ### ", "    #", " ### "],
        '4': ["#   #", "#   #", " ### ", "    #", "    #"],
        '5': [" ### ", "#    ", " ### ", "    #", " ### "],
        '6': [" ### ", "#    ", " ### ", "#   #", " ### "],
        '7': [" ### ", "    #", "    #", "    #", "    #"],
        '8': [" ### ", "#   #", " ### ", "#   #", " ### "],
        '9': [" ### ", "#   #", " ### ", "    #", " ### "]
    }
    
    if input_data.isdigit():
        input_str = str(input_data)
    else:
        print('ERROR: The input data should be only integer.')
        return 

    output_design = ['' for idx in range(5)]
    
    for digit in input_str:
        design = digit_design_data[digit]
        for idx in range(5):
            output_design[idx] += design[idx] + ' '

    output = '\n' + '\n'.join(output_design) + '\n'
    return output

input_data = input('Enter the input number (int): ')
print(simulate_seven_segment(input_data))