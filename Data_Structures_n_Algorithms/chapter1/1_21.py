def read_inputs(filepath):
    fp = open(filepath)
    lines = []
    while True:
        try:
            line = fp.readline()
            if line == '': raise EOFError
            lines.append(line[:-1])  #This will not execute if the EOFError is raised, also need to remove the \n
        except EOFError:
            for line in reversed(lines):
                print (line)
            return 

        
read_inputs("king_never_die.txt")
