import datetime
from dataclasses import dataclass


@dataclass
class RepositoryValue:
    _value = None
    _length: int = None
    _value_type = None

    @property
    def value(self):
        if self._value is None:
            return None

        value_type = self._value_type
        value = value_type(self._value)
        return value

    @value.setter
    def value(self, obj_val):
        if obj_val is not None:
            self._value = str(obj_val)

    def is_valid(self):
        try:
            value_type = self._value_type
            value_type(self._value)
        except ValueError:
            return False

        if self._length is not None and self._length < len(self._value):
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


@dataclass
class RepoDatetime(RepositoryValue):
    def __int__(self, value):
        self.value = value
        self._value_type = datetime
