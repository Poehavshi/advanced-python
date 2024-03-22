import numpy as np

from numpyclone import MatrixNpLike


def test_addition():
    data1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    data2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    mat1 = MatrixNpLike(data1)
    mat2 = MatrixNpLike(data2)
    mat3 = mat1 + mat2
    assert mat3.value == np.add(data1, data2).tolist()


def test_subtraction():
    data1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    data2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    mat1 = MatrixNpLike(data1)
    mat2 = MatrixNpLike(data2)
    mat3 = mat1 - mat2
    assert mat3.value == np.subtract(data1, data2).tolist()


def test_multiplication():
    data1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    data2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    mat1 = MatrixNpLike(data1)
    mat2 = MatrixNpLike(data2)
    mat3 = mat1 * mat2
    assert mat3.value == np.matmul(data1, data2).tolist()


def test_elementwise_multiplication():
    data1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    data2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    mat1 = MatrixNpLike(data1)
    mat2 = MatrixNpLike(data2)
    mat3 = mat1 @ mat2
    assert mat3.value == np.multiply(data1, data2).tolist()
