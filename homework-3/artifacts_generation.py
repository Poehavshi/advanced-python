import numpy as np
import numpyclone as npclone
from pathlib import Path


def task3_1():
    np.random.seed(0)
    a = np.random.randint(0, 10, (10, 10)).tolist()
    b = np.random.randint(0, 10, (10, 10)).tolist()
    np.random.randint(0, 10, (10, 10))
    mat1 = npclone.Matrix(a)
    mat2 = npclone.Matrix(b)
    artifacts_path = Path("artifacts") / "3.1"
    with open(artifacts_path / "matrix1.txt", "w") as f:
        f.write(str(mat1))
    with open(artifacts_path / "matrix2.txt", "w") as f:
        f.write(str(mat2))
    with open(artifacts_path / "matrix+.txt", "w") as f:
        f.write(str(mat1 + mat2))
    with open(artifacts_path / "matrix_multiplication.txt", "w") as f:
        f.write(str(mat1 * mat2))
    with open(artifacts_path / "matrix@.txt", "w") as f:
        f.write(str(mat1 @ mat2))


def task3_2():
    np.random.seed(0)
    a = np.random.randint(0, 10, (10, 10)).tolist()
    b = np.random.randint(0, 10, (10, 10)).tolist()
    np.random.randint(0, 10, (10, 10))
    mat1 = npclone.MatrixNpLike(a)
    mat2 = npclone.MatrixNpLike(b)
    artifacts_path = Path("artifacts") / "3.2"
    with open(artifacts_path / "matrix1.txt", "w") as f:
        f.write(str(mat1))
    with open(artifacts_path / "matrix2.txt", "w") as f:
        f.write(str(mat2))
    with open(artifacts_path / "matrix+.txt", "w") as f:
        f.write(str(mat1 + mat2))
    with open(artifacts_path / "matrix_multiplication.txt", "w") as f:
        f.write(str(mat1 * mat2))
    with open(artifacts_path / "matrix@.txt", "w") as f:
        f.write(str(mat1 @ mat2))
    mat1.tofile(artifacts_path / "matrix.txt")
    print(mat1.value)
    mat1.value = a


def task3_3():
    # test cache
    np.random.seed(0)
    A = npclone.Matrix(((1, 2, 3), (4, 5, 6)))
    B = npclone.Matrix(((4, 5, 6), (1, 2, 3)))
    C = npclone.Matrix(((4, 6, 5), (1, 2, 3)))
    D = npclone.Matrix(((4, 5, 6), (1, 2, 3)))

    artifacts_path = Path("artifacts") / "3.3"
    with open(artifacts_path / "A.txt", "w") as f:
        f.write(str(A))
    with open(artifacts_path / "B.txt", "w") as f:
        f.write(str(B))
    with open(artifacts_path / "C.txt", "w") as f:
        f.write(str(C))
    with open(artifacts_path / "D.txt", "w") as f:
        f.write(str(D))

    ab = A @ B
    cd = C @ D
    with open(artifacts_path / "ab.txt", "w") as f:
        f.write(str(ab))
    with open(artifacts_path / "cd.txt", "w") as f:
        f.write(str(cd))
    with open(artifacts_path / "hash.txt", "w") as f:
        f.write(f"ab: {hash(ab)}\n")
        f.write(f"cd: {hash(cd)}\n")


if __name__ == '__main__':
    task3_1()
    task3_2()
    task3_3()
