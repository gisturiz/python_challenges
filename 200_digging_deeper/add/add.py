def add(l1, l2):

    result = []
    
    for i in range(0, len(l1)):
        innerRes = []
        result.append(innerRes)
        for j in range(0, len(l1)):
            innerRes.append(l1[i][j] + l2[i][j])

    return result