import numpy as np

def get_matrix(n):
    matrix = []
    print(f"Enter the elements of a {n}x{n} matrix row-wise:")
    for i in range(n):
        row = list(map(float, input().split()))
        if len(row) != n:
            print(f"Error: Enter exactly {n} numbers for row {i+1}")
            return None
        matrix.append(row)
    return np.array(matrix)

def solve_matrix(matrix):
    if matrix is None:
        return
    det = np.linalg.det(matrix)
    print(f"Determinant: {det:.2f}")

def matrix_addition(matrix1, matrix2):
    if matrix1 is None or matrix2 is None:
        return
    print("Matrix Addition:")
    print(matrix1 + matrix2)

def matrix_subtraction(matrix1, matrix2): 
    if matrix1 is None or matrix2 is None:
        return
    print("Matrix Subtraction:")
    print(matrix1 - matrix2)

def matrix_multiplication(matrix1, matrix2): 
    if matrix1 is None or matrix2 is None:
        return 
    print("Matrix Multiplication:")
    print(np.dot(matrix1, matrix2))

def matrix_operations(matrix1, matrix2):
    while True:
        task = int(input("Enter: 1 for addition, 2 for subtraction, 3 for multiplication:, 4 for exit"))
        if task == 1:
            matrix_addition(matrix1, matrix2)
        elif task == 2:
            matrix_subtraction(matrix1, matrix2)
        elif task == 3:
            matrix_multiplication(matrix1, matrix2)
        elif task == 4:
            break
        else:
            print("Invalid Input")
    

def matrix():
    size = int(input("\nEnter matrix size (2 for 2x2, 3 for 3x3): "))

    if size not in [2, 3]:
        print("Invalid size. Only 2x2 or 3x3 matrices are supported.")
    else:
        print("Enter first matrix:")
        matrix1 = get_matrix(size)

        print("Enter second matrix:")
        matrix2 = get_matrix(size)
      
        print("\nSolving first matrix:")
        solve_matrix(matrix1)

        print("Solving second matrix:")
        solve_matrix(matrix2)
        
        matrix_operations(matrix1, matrix2)
