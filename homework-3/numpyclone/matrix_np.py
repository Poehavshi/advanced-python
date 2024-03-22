import numbers

import numpy as np

from numpyclone.mixins.getset import GetterMixin, SetterMixin
from numpyclone.mixins.io import ToJsonFileMixin, StringifyMixin


class MatrixNpLike(np.lib.mixins.NDArrayOperatorsMixin, ToJsonFileMixin, StringifyMixin, GetterMixin, SetterMixin):
    """
    Matrix realization with numpy mixins and our mixins
    """
    def __init__(self, value: list[list]):
        self.value = value

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())
        for x in inputs + out:
            if not isinstance(x, (np.ndarray, MatrixNpLike, numbers.Number)):
                return NotImplemented

        inputs = tuple(x.value if isinstance(x, MatrixNpLike) else x for x in inputs)
        if out:
            kwargs['out'] = tuple(x.value if isinstance(x, MatrixNpLike) else x for x in out)
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            return tuple(MatrixNpLike(x) for x in result)
        elif method == 'at':
            return None
        else:
            return MatrixNpLike(result.tolist())


if __name__ == '__main__':
    matrix = MatrixNpLike([[1, 2], [3, 4]])
    matrix.tofile("matrix.txt")
