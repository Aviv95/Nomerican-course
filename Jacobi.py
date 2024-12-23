
def jacobi(M,V):
    """
    This function solves a system of linear equations using Jacobi method
    :param M:The matrix of the system of linear equations
    :param V: The vector of the system of linear equations
    :return:The solution
    """
    n = len(V)
    X = [0 for i in range(n)]
    temp = [0 for i in range(n)]
    epsilon = 0.00001
    max_iterations = 100
    print("Solving using Jacobi method")
    print("i  |  x1  |  x2  |  x3  |")
    print("0  | {:.8f} | {:.8f} | {:.8f} |".format(X[0], X[1], X[2]))
    for i in range(max_iterations):
        for j in range(n):
            temp[j] = V[j][0]
            for k in range(n):
                if j != k:
                    temp[j] -= M[j][k] * X[k]
            temp[j] /= M[j][j]
        norm = 0
        for j in range(n):
            norm += abs(X[j] - temp[j])
            X[j] = temp[j]
        print("{:<3d}| {:.8f} | {:.8f} | {:.8f} |".format(i, X[0], X[1], X[2]))
        if norm < epsilon:
            print("Solution found in ", i, " iterations")
            for j in range(n):
                print("X[", j, "] = ", X[j])
            return
    print("\nSolution not found in ", max_iterations, " iterations")
    return



