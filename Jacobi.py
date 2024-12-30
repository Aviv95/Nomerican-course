
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
    max_width = 10

    header = "i  | " + " | ".join([f"{'x' + str(j + 1):^{max_width}}" for j in range(n)]) + " |"
    print(header)
    print("-" * len(header))

    # Initial values (iteration 0)
    print(f"0  | " + " | ".join([f"{X[j]:.8f}" for j in range(n)]) + " |")
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
        print(f"{i + 1:<3d}| " + " | ".join([f"{X[j]:.8f}" for j in range(n)]) + " |")
        if norm < epsilon:
            print("Solution found in ", i, " iterations")
            for j in range(n):
                print(f"X[{j}] = {X[j]:.8f}")
            return
    print("\nSolution not found in ", max_iterations, " iterations")
    return



