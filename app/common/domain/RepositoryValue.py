from dataclasses import dataclass


@dataclass
class RepositoryValue:
    _value = None
    _length: int = None
    _value_type = None

    @property
    def value(self):
        value_type = self._value_type
        value = value_type(self._value)
        return value

    @value.setter
    def value(self, obj_val):
        self._value = str(obj_val)

    def validate(self):
        try:
            value_type = self._value_type
            value_type(self._value)
        except ValueError:
            return False

        if len(self._value) > self._length:
            return False

        return True


@dataclass
class RepoInt(RepositoryValue):
    def __init__(self, value):
        self.value = value
        self._length = 11
        self._value_type = int


@dataclass
class RepoVarchar(RepositoryValue):
    def __init__(self, value):
        self.value = value
        self._length = 255
        self._value_type = str


@dataclass
class RepoText(RepositoryValue):
    def __init__(self, value):
        self.value = value
        self._value_type = str


@dataclass
class RepoDecimal(RepositoryValue):
    def __init__(self, value):
        self.value = value
        self._length = 18
        self._value_type = float


@dataclass
class RepoBool(RepositoryValue):
    def __init__(self, value):
        self.value = value
        self._length = 1
        self._value_type = bool
