from math import comb
def matrix_multiply(A, B):
    """
    Multiply two square matrices A and B.
    
    Parameters:
        A (list of lists): First square matrix.
        B (list of lists): Second square matrix.
    
    Returns:
        list of lists: Resulting matrix.
    """
    mod = 10**9 + 7
    # Get dimensions of matrices
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])

    # Initialize result matrix
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Perform multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += (A[i][k] * B[k][j])%mod

    return result

def matrix_power(M, P):
    """
    Compute the power of a square matrix M to the exponent P.
    
    Parameters:
        M (list of lists): Square matrix.
        P (int): Exponent.
    
    Returns:
        list of lists: Resulting matrix.
    """
    n = len(M)
    result = [[int(i == j) for j in range(n)] for i in range(n)]  # Identity matrix
    while P > 0:
        if P % 2 == 1:
            result = matrix_multiply(result, M)
        M = matrix_multiply(M, M)
        P //= 2
    return result

P = 5
HR = [[1], [0], [1]]
MR = [[1, 1, 1],
      [1, 0, 0],
      [0, 0, 1]]

HG = [[1], [0], [0], [1]]
MG = [[1, 0, 1, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1]]

HB = [[1], [0], [0], [0], [1]]
MB = [[1, 0, 0, 1, 1],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1]]



T = int(input())
for _ in range(T):
    P = int(input())
    if P > 5:
        result = matrix_multiply(matrix_power(MR,P-2), HR)[0][0] + matrix_multiply(matrix_power(MG,P-3), HG)[0][0] + matrix_multiply(matrix_power(MB,P-4), HB)[0][0]
        print(result % (10**9+7))
    else:
        n = P
        tiles = [2, 3, 4]
        count = 0
        for tile in tiles:
            c = 1
            while True:
                t = n-(tile-1)*c
                if t > 0:
                    combination = comb(t, c)
                    if combination == 0:
                        break
                else:
                    break
                count += combination
                c += 1
        print(count % (10**9+7))
