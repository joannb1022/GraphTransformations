from networkx.drawing.nx_agraph import read_dot


def parse(file):
    with open(file) as file_in:
        with open("data/graph.dot", "w") as graph:
            line = file_in.readline()
            while line.strip('\n') not in "--":
                graph.write(line)
                line = file_in.readline()
        line = file_in.readline()

        with open("data/left_sides.txt", "w") as file_L, open("data/rules.txt", "w") as settleFile:
            while line != "":
                prod_num = int(line)
                line = file_in.readline()  # to jest tak naokoło xd
                if line.strip('\n') in "--":
                    line = file_in.readline()
                file_L.write(line)
                file_L.write("\n")

                name_P = "data/P%s.dot" % str(prod_num)
                with open(name_P, "w") as file_P:
                    line = file_in.readline()
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
                line = file_in.readline()
    return prod_num


def get_rules_func(N):
    rules = [{} for _ in range(N)]
    rules_file = "data/rules.txt"
    with open(rules_file) as f:
        for i in range(N):
            line = f.readline()
            while line != "\n" and line != '':
                (key, val) = line.split()
                rules[i][key] = val
                line = f.readline()

    return rules


def get_prod_func(N):

    prod = [[0 for _ in range(2)] for _ in range(N)]
    i = 0
    with open("data/left_sides.txt", "r") as left:
        while i < N:
            for label in left:
                if label not in "\n":
                    prod[i][0] = label.strip('\n')
                    filename = "data/P%s.dot" % str(i + 1)
                    P = read_dot(filename)
                    prod[i][1] = P
                    i += 1

    return prod
