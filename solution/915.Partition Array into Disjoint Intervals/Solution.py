def partitionDisjoint(A):
    """
    :type A: List[int]
    :rtype: int
    """
    max_left = [None] * len(A)
    min_right = [None] * len(A)

    temp = A[0]
    for i in range(len(A)):
        temp = max(temp, A[i])
        max_left[i] = temp
    
    temp = A[len(A)-1]
    for i in range(len(A)-1, -1, -1):
        temp = min(temp, A[i])
        min_right[i] = temp

    for i in range(1,len(A)):
        if max_left[i-1] <= min_right[i]:
            return i