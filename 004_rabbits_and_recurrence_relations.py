with open("./input_files/004_input.txt", "r") as input_file, open("./output_files/004_output.txt", "w") as output_file:
    input_data = input_file.read().strip("\n").split(" ")
    n = int(input_data[0])
    k = int(input_data[1])
    start = [1, 1]
    for i in range(n - 2):
        start.append(start[-1] + (k * start[-2]))
    output_file.write(str(start[-1]))
