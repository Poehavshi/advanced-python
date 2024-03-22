

class ToJsonFileMixin:
    def tofile(self, path: str):
        data = {k: v for k, v in self.__dict__.items() if not k.startswith('_')}
        for k, v in data.items():
            if isinstance(v, list):
                data[k] = ' '.join(map(str, v))
            else:
                data[k] = str(v)
        with open(path, 'w') as f:
            f.write(str(data))


class StringifyMixin:
    def __str__(self):
        return str(self.__dict__)
