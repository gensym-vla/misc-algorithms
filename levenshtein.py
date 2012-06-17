import sys
def levenshtein(str1, str2):
    """
    computes the levenshtein distance between to strings
    space complexity: O(min(|str1|, |str2|))
    """
    length1 = len(str1)
    length2 = len(str2)
    # make sure that first string is the smaller one
    if length2 < length1:
        return levenshtein(str2, str1)
    # maybe i should use nested lists instead of a dictionary
    edit = {}
    # initialize the matrix
    for i in range(length1 + 1):
        edit[0,i] = i
    curr, prev = 0, 1
    for i in range(1,length2 + 1):
        # toggle the two lines
        curr, prev = prev, curr
        edit[curr,0] = i
        for j in range(1,length1 + 1):
            # the cost of the substitution
            diff = 0 if str1[j - 1] == str2[i - 1] else 1
            edit[curr, j] = min(
                                 edit[prev, j]     + 1,   # deletion
                                 edit[curr, j - 1] + 1,   # insertion
                                 edit[prev, j - 1] + diff # substitution
                               )
    return edit[curr, length1]
    
