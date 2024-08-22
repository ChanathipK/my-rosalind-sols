with open("./input_files/002_input.txt", "r") as input_file, open("./output_files/002_output.txt", "w") as output_file:
    # if you are using other language, just iterate through each character with conditional statement
    # or control structure
    # but thanks to high level function in Python
    output_file.write(input_file.read().strip("\n").upper().replace("T", "U"))