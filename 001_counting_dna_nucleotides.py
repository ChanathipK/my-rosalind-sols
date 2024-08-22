# input's length might be long, getting input from a file is recommended
with open("./input_files/001_input.txt", "r") as input_file, open("./output_files/001_output-txt", "w") as output_file:
    data = input_file.read().strip("\n")
    a_count = 0
    c_count = 0
    g_count = 0
    t_count = 0
    # sadly, Python doesn't have switch-case
    for ch in data:
        if ch.upper() == "A":
            a_count += 1
        elif ch.upper() == "C":
            c_count += 1
        elif ch.upper() == "G":
            g_count += 1
        elif ch.upper() == "T":
            t_count += 1
    output_file.write(f"{a_count} {c_count} {g_count} {t_count}")