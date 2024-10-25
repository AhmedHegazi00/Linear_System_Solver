# functions
def subscript(n):
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
    subscript_n = ""
    for c in t:
        subscript_n += subscript_mapping[c]
    return subscript_n
def copy(matrix1):
    matrix2 = [0] * len(matrix1)
    for r in range(len(matrix1)):
        matrix2[r] = [0] * len(matrix1[r])
        for c in range(len(matrix1[r])):
            matrix2[r][c] = matrix1[r][c]
    return matrix2
# classes
class System:
    def __init__(self, equations, variables):
        self.system = [0] * equations
        print("\nThe formula of the system:\na₁₁X₁₁ + a₁₂X₁₂ + ... + a₁ₙX₁ₙ = b₁\na₂₁X₂₁ + a₂₂X₂₂ + ... + a₂ₙX₂ₙ = b₂\n...\naₙ₁Xₙ₁ + aₙ₂Xₙ₂ + ... + aₙₙXₙₙ = bₙ\n")
        for e in range(equations):
            self.system[e] = [0] * (variables + 1)
            for v in range (variables + 1):
                ep = subscript(e+1)
                vp = subscript(v+1)
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
                    rp = subscript(r+1)
                    cp = subscript(c+1)
                    self.matrix[r][c] = int(input(f"Enter a{rp}{cp}: "))
            self.rows = rows
            self.columns = columns
        elif system != 0 and rows == 0 and columns == 0:
            self.matrix = system.system
            self.rows = system.equations
            self.columns = system.variables + 1
    def create_comatrix(self):
        self.comatrix = copy(self.matrix)
        for r in range (self.rows):
            del self.comatrix[r][self.columns - 1]
    @classmethod
    def print(cls, matrix):
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                # print the start line
                if c == 0:
                    print("|", end="")
                # print the number
                print(matrix[r][c], end="")
                # print the spaces
                if c < len(matrix[r]) - 1:
                    print(" ", end="")
                # print the end line
                if c == len(matrix[r]) - 1:
                    print("|", end="")
            print()
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
                pv = subscript(j+1)
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
    print("\nThe agumented matrix after creating the coefficient matrix: ")
    Matrix.print(matrix.matrix)
else:
    print("You entered a wrong value")