from numbers import Number
from typing import Iterable


class HashMixin:
    def __hash__(self):
        hash = 0
        data = {k: v for k, v in self.__dict__.items() if not k.startswith('_')}
        for k, v in data.items():
            if isinstance(v, Iterable) and isinstance(v[0], Iterable) and isinstance(v[0][0], Number):
                for i in v:
                    hash += sum(i)
            elif isinstance(v, str):
                hash += len(v)
            else:
                hash += int(v)
        return int(hash) % 5

    def __eq__(self, other):
        return hash(self) == hash(other)
