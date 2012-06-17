def cyk(word, grammar, verbose=False):
    """
    A not neccesarily efficient implementation of the Cocke-Younger-Kasami
    algorithm.
    Grammar should be represented as a dictionary, whose keys are the
    nonterminals.
    The hashvalues should be lists containing the productions.
    i.e 
    S -> AA | AB, A -> a, B -> b <=> 
         {"S" : ["AA", "AB"], "A" : ["a"], "B" : ["b]}
    """
    size = len(word)
    pyramide = {}
    # initialize the first row of the pyramide
    for i,ch in enumerate(word):
        pyramide[i,i] = []
        for rule in grammar:
            # iterate over all "or" clauses
            for subclause in grammar[rule]:
                if subclause == ch:
                    pyramide[i,i].append(rule)
                    break # go to the next rule
    for i in range(1, size):
        for j in range(size - i):
            # populate the box j,j+i
            pyramide[j,j+i] = []
            for k in range(j, j + i):
                for rule in grammar:
                    for subclause in grammar[rule]:
                        print rule, subclause
                        if any(B+C == subclause 
                                for B in pyramide[j,k]
                                for C in pyramide[k + 1, j + i]):
                            pyramide[j,j+i].append(rule)
                            break 
    if verbose:
        print pyramide
    return "S" in pyramide[0, size - 1]

