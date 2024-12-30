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
    max_width = 10

    header = "i  | " + " | ".join([f"{'x' + str(j + 1):^{max_width}}" for j in range(n)]) + " |"
    print(header)
    print("-" * len(header))

    # Initial values (iteration 0)
    print(f"0  | " + " | ".join([f"{X[j]:.8f}" for j in range(n)]) + " |")

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

        # Print the solution at this iteration
        print(f"{i + 1:<3d}| " + " | ".join([f"{X[j]:.8f}" for j in range(n)]) + " |")

        if norm < epsilon:
            print("Solution found in ", i + 1, " iterations")
            for j in range(n):
                print(f"X[{j}] = {X[j]:.8f}")
            return
    print("Solution not found in ", max_iterations, " iterations")
    return



