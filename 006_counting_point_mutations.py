with open("./input_files/006_input.txt", "r") as input_file, open("./output_files/006_output.txt", "w") as output_file:
    dnas = input_file.read().strip("\n").split("\n")
    count = 0
    for i in range(len(dnas[0])):
        if dnas[0][i] != dnas[1][i]:
            count += 1
    output_file.write(str(count))