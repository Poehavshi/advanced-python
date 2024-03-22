"""
Test matrix class to ensure that the matrix class is working as expected (like the numpy matrix class)
"""

import numpy as np
from numpyclone.matrix import Matrix
import pytest


def test_matrix_creation():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mat = Matrix(data)
    assert mat.data == data


def test_matrix_addition():
    data1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    data2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    mat1 = Matrix(data1)
    mat2 = Matrix(data2)
    mat3 = mat1 + mat2
    assert mat3.data == np.add(data1, data2).tolist()


def test_matrix_subtraction():
    data1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    data2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    mat1 = Matrix(data1)
    mat2 = Matrix(data2)
    mat3 = mat1 - mat2
    assert mat3.data == np.subtract(data1, data2).tolist()


def test_matrix_multiplication():
    data1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    data2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    mat1 = Matrix(data1)
    mat2 = Matrix(data2)
    mat3 = mat1 * mat2
    assert mat3.data == np.matmul(data1, data2).tolist()


def test_matrix_elementwise_multiplication():
    data1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    data2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    mat1 = Matrix(data1)
    mat2 = Matrix(data2)
    mat3 = mat1 @ mat2
    assert mat3.data == np.multiply(data1, data2).tolist()


def test_matrix_addition_exception():
    data1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    data2 = [[9, 8, 7], [6, 5, 4]]
    mat1 = Matrix(data1)
    mat2 = Matrix(data2)
    with pytest.raises(ValueError):
        mat3 = mat1 + mat2


def test_matrix_subtraction_exception():
    data1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    data2 = [[9, 8, 7], [6, 5, 4]]
    mat1 = Matrix(data1)
    mat2 = Matrix(data2)
    with pytest.raises(ValueError):
        mat3 = mat1 - mat2


def test_matrix_multiplication_exception():
    data1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    data2 = [[9, 8, 7], [6, 5, 4]]
    mat1 = Matrix(data1)
    mat2 = Matrix(data2)
    with pytest.raises(ValueError):
        mat3 = mat1 * mat2


def test_matrix_elementwise_multiplication_exception():
    data1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    data2 = [[9, 8, 7], [6, 5, 4]]
    mat1 = Matrix(data1)
    mat2 = Matrix(data2)
    with pytest.raises(ValueError):
        mat3 = mat1 @ mat2


def test_matrix_repr():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mat = Matrix(data)
    assert mat.__repr__() == f"Matrix({data})"


def test_matrix_str():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mat = Matrix(data)
    assert mat.__str__() == "1 2 3\n4 5 6\n7 8 9"
