def gaius_seidel(M,V) :
    """
    This function solves a system of linear equations using Gaius Seidel method
    :param M:The matrix of the system of linear equations
    :param V:The vector of the system of linear equations
    :return:The solution
    """
    n = len(V)
    X = [0 for i in range(n)]
    epsilon = 0.00001
    max_iterations = 100
    print("Solving using Gaius Seidel method")
    print("i  |  x1  |  x2  |  x3  |")
    print("0 | {:.8f} | {:.8f} | {:.8f} |".format(X[0], X[1], X[2]))
    for i in range(max_iterations):
        norm = 0
        for j in range(n):
            temp = V[j][0]
            for k in range(n):
                if j != k:
                    temp -= M[j][k] * X[k]
            temp /= M[j][j]
            norm += abs(X[j] - temp)
            X[j] = temp
        print("{:<3d}| {:.8f} | {:.8f} | {:.8f} |".format(i, X[0], X[1], X[2]))
        if norm < epsilon:
            print("Solution found in ", i, " iterations")
            for j in range(n):
                print("X[", j, "] = ", X[j])
            return
    print("Solution not found in ", max_iterations, " iterations")
    return


