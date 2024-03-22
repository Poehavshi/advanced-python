from typing import Generic, TypeVar

T = TypeVar('T')


class Matrix(Generic[T]):
    """
    A class to represent a matrix.
    Does not support broadcasting.
    And don't use numpy at all.
    """
    def __init__(self, data: list[list[T]]):
        self.data = data

    def __repr__(self):
        return f"Matrix({self.data})"

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def __add__(self, other: 'Matrix') -> 'Matrix':
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Matrices must have the same dimensions")
        new_data = [[self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))] for i in range(len(self.data))]
        return Matrix(new_data)

    def __sub__(self, other: 'Matrix') -> 'Matrix':
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Matrices must have the same dimensions")
        new_data = [[self.data[i][j] - other.data[i][j] for j in range(len(self.data[0]))] for i in range(len(self.data))]
        return Matrix(new_data)

    def __mul__(self, other: 'Matrix') -> 'Matrix':
        """Matrix multiplication of two matrices"""
        if len(self.data[0]) != len(other.data):
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix")
        new_data = [[sum(self.data[i][k] * other.data[k][j] for k in range(len(other.data))) for j in range(len(other.data[0]))] for i in range(len(self.data))]
        return Matrix(new_data)

    def __matmul__(self, other):
        """Element-wise multiplication of two matrices"""
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Matrices must have the same dimensions")
        new_data = [[self.data[i][j] * other.data[i][j] for j in range(len(self.data[0]))] for i in range(len(self.data))]
        return Matrix(new_data)

