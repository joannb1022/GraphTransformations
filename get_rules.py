def get_rules_func(N):

    rules = [{} for _ in range(N)]
    rules_file = "rules.txt"
    with open(rules_file) as f:
        for i in range(N):
            line = f.readline()
            while line != "\n" and line != '':
                (key, val) = line.split()
                rules[i][key] = val
                line = f.readline()

    return rules

