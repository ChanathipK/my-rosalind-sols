with open("./input_files/003_input.txt", "r") as input_file, open("./output_files/003_output.txt", "w") as output_file:
    reversed_string = input_file.read().strip("\n")[::-1]
    # when you don't provide the first two number when slicing, and the last number is negative
    # the first number will be the last index, and this syntax will reverse the string
    complemented_string = ""
    for ch in reversed_string:
        if ch.upper() == "A":
            complemented_string += "T"
        elif ch.upper() == "T":
            complemented_string += "A"
        elif ch.upper() == "C":
            complemented_string += "G"
        elif ch.upper() == "G":
            complemented_string += "C"
    output_file.write(complemented_string)
    # is there a better way to do this, yes, but for the sake of readability, this is my opinionated choice