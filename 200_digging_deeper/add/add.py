def add(*arrays):

    result = []
    
    for i in range (0, len(arrays)):
        innerArray = []
        result.append(innerArray)
        for j in range (0, len(arrays[i])):
            arrays[i][j] + arrays[i + 1][j]

    return result