class GetterMixin:
    def __getitem__(self, key):
        print("Accessing key:", key)
        return self.__dict__[key]


class SetterMixin:
    def __setitem__(self, key, value):
        print("Setting key:", key, "to value:", value)
        self.__dict__[key] = value
