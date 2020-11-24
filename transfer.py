def parse(file):
    with open(file) as file_in:
        with open("graph.dot", "w") as graph:
            line = file_in.readline()
            while line.strip('\n') not in "--":
                graph.write(line)
                line = file_in.readline()
        line = file_in.readline()

        with open("left_sides.txt", "w") as file_L, open ("rules.txt", "w") as settleFile:
            while line != "":
                prod_num = int(line)
                line=file_in.readline()  #to jest tak naokoło xd
                if line.strip('\n') in "--":
                    line=file_in.readline()
                file_L.write(line)
                file_L.write("\n")

                name_P = "P%s.dot" % str(prod_num)
                with open(name_P, "w") as file_P:
                    line=file_in.readline()
                    if line.strip('\n') in "--":
                        line = file_in.readline()
                    while line.strip('\n') not in "--":
                        file_P.write(line)
                        line = file_in.readline()
                    line = file_in.readline()
                    while line.strip('\n') not in "--":
                        settleFile.write(line)
                        line = file_in.readline()
                    settleFile.write("\n")
                line=file_in.readline()
    return prod_num
