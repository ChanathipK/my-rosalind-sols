with open("./input_files/005_input.txt", "r") as input_file, open("./output_files/005_output.txt", "w") as output_file:
    gc_content = [[0, e[0:13], e[13:].upper()] for e in input_file.read().replace("\n", "").replace(" ", "").strip(">").split(">")]
    for read in gc_content:
        read[0] = round((read[2].count("G") + read[2].count("C")) / len(read[2]) * 100, 6)
    gc_content.sort()
    answer = f"{gc_content[-1][1]}\n{gc_content[-1][0]}"
    output_file.write(answer)