# libraries
import copy
# functions
def sub(n):
    subscript_mapping = {
        '0': '₀',
        '1': '₁',
        '2': '₂',
        '3': '₃',
        '4': '₄',
        '5': '₅',
        '6': '₆',
        '7': '₇',
        '8': '₈',
        '9': '₉'
    }
    t = str(n)
    sub_n = ""
    for c in t:
        sub_n += subscript_mapping[c]
    return sub_n
# classes
class System:
    def __init__(self, equations, variables):
        self.system = [0] * equations
        print("\nThe formula of the system:\na₁₁X₁₁ + a₁₂X₁₂ + ... + a₁ₙX₁ₙ = b₁\na₂₁X₂₁ + a₂₂X₂₂ + ... + a₂ₙX₂ₙ = b₂\n...\naₙ₁Xₙ₁ + aₙ₂Xₙ₂ + ... + aₙₙXₙₙ = bₙ\n")
        for e in range(equations):
            self.system[e] = [0] * (variables + 1)
            for v in range (variables + 1):
                ep = sub(e+1)
                vp = sub(v+1)
                if v < variables:
                    self.system[e][v] = int(input(f"Enter a{ep}{vp}: "))
                elif v == variables:
                    self.system[e][v] = int(input(f"Enter b{ep}: "))
        self.equations = equations
        self.variables = variables
class Matrix:
    def __init__(self, system, rows, columns):
        if system == 0:
            self.matrix = [0] * rows
            print("\nThe formula of the matrix:\n|a₁₁ a₁₂ ... a₁ₙ|\n|a₂₁ a₂₂ ... a₂ₙ|\n|        ...    |\n|aₙ₁ aₙ₂ ... aₙₙ|\n")
            for r in range(rows):
                self.matrix[r] = [0] * columns
                for c in range (columns):
                    rp = sub(r+1)
                    cp = sub(c+1)
                    self.matrix[r][c] = int(input(f"Enter a{rp}{cp}: "))
            self.rows = rows
            self.columns = columns
        elif system != 0 and rows == 0 and columns == 0:
            self.matrix = system.system
            self.rows = system.equations
            self.columns = system.variables + 1
    def create_comatrix(self):
        self.comatrix = copy.deepcopy(self.matrix)
        for r in range (self.rows):
            del self.comatrix[r][self.columns - 1]
    @classmethod
    def print(cls, matrix):
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if c == 0:
                    print("|", end="")
                print(matrix[r][c], end="")
                if c < len(matrix[r]) - 1:
                    print(" ", end="")
                if c == len(matrix[r]) - 1:
                    print("|", end="")
            print()
    @classmethod
    def switch_row(cls, matrix, r1, r2):
        matrix[r1-1] , matrix[r2-1] = matrix[r2-1] , matrix[r1-1]
    @classmethod
    def multiply_row(cls, matrix, r, constant):
        if constant != 0:
            for c in range(len(matrix[r-1])):
                matrix[r-1][c] *= constant
    @classmethod
    def multiply_add_row(cls, matrix, r1, r2, constant):
        r = list(matrix[r1-1])
        for c in range(len(r)):
            r[c] *= constant
        for c in range(len(r)):
            matrix[r2-1][c] += r[c]
# program 
print("""What are you going to enter?
- Choose 1 to enter a system
- Choose 2 to enter a matrix""")
m = int(input("Choose by entering a number: "))
if m == 1 or m == 2:
    # system entered
    if m == 1:
        print("\nYou are going to enter a system!\n")
        equations = int(input("Enter the system's number of equations: "))
        variables = int(input("Enter the system's number of variables: "))
        system = System(equations, variables)
        matrix = Matrix(system, 0, 0)
        print("\nThe equation: ")
        for i in range(system.equations):
            for j in range(system.variables + 1):
                pv = sub(j+1)
                if j < system.variables:
                    print(f"{system.system[i][j]}X{pv}", end="")
                if j < system.variables - 1:
                    print(" + ", end="")
                if j == system.variables:
                    print(" = ", end="")
                    print(system.system[i][j])
    # matrix entered
    elif m == 2:
        print("\nYou are going to enter a matrix!\n")
        rows = int(input("Enter the matrix's number of rows: "))
        columns = int(input("Enter the matrix's number of columns: "))
        matrix = Matrix(0,rows, columns)
    # general
    # agumented matrix
    print("\nThe agumented matrix: ")
    Matrix.print(matrix.matrix)
    # coefficient matrix
    matrix.create_comatrix()
    print("\nThe coefficient matrix: ")
    Matrix.print(matrix.comatrix)
    #test
    print("Test")
    Matrix.multiply_add_row(matrix.matrix, 1, 2, 2)
    Matrix.print(matrix.matrix)
else:
    print("You entered a wrong value")