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


if __name__ == '__main__':
    task3_1()
