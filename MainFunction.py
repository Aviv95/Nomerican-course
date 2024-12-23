from Jacobi import  jacobi
from GaiusSeidel import  gaius_seidel
from itertools import permutations

def diagonally_dominant(M):
    """
    This function checks if the matrix is diagonally dominant
    :param M:The matrix to check
    :return:The true or false
    """
    n = len(M)
    for i in range(n):
        sum = 0
        for j in range(n):
            if i != j:
                sum += abs(M[i][j])
        if abs(M[i][i]) <= sum:
            return False
    return True

def make_diagonally_dominant(M):
    """
    This function makes the matrix diagonally dominant
    :param M:The matrix to make it diagonally dominant
    :return: The matrix after making it diagonally dominant and if it can be made diagonally dominant
    """
    n = len(M)
    for perm in permutations(range(n)):
        permuted_matrix = [M[i] for i in perm]
        if all(abs(permuted_matrix[i][i]) > sum(abs(permuted_matrix[i][j]) for j in range(n) if j != i) for i in
               range(n)):
            return permuted_matrix, True
    return M, False

def main():
    matrixA = [[4, 2, 0], [2, 10, 4], [0, 4, 5]]
    vectorB = [[2], [6], [5]]

    while True:
        print("This program will solve a system of linear equations using Jacobi or Gaius Seidel method.")

        if (diagonally_dominant(matrixA)):
            print("Matrix is diagonally dominant")
            matrixB = matrixA
        else:
            print("Matrix is not diagonally dominant")
            matrixB,result=make_diagonally_dominant(matrixA)
            if result:
                print("The matrix changed to diagonally dominant matrix ")
                print(matrixB)
            else:
                print("The matrix can't be changed to diagonally dominant matrix")


        print("For Jacobi choose 1, for Gaius Seidel choose 2, for stop the program choose 3")

        choice = input("1. Jacobi\n2. Gaius Seidel\n3. Stop program\n")

        if choice == "1":
            jacobi(matrixB, vectorB)
        elif choice == "2":
            gaius_seidel(matrixB, vectorB)
        elif choice == "3":
            print("Program stopped")
            break
        else:
             print("Invalid choice!")



if __name__ == "__main__":
        main()