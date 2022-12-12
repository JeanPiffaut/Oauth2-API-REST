import datetime
from dataclasses import dataclass

from decouple import config


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
        obj_val = value_type(self._value)
        return obj_val

    @value.setter
    def value(self, obj_val):
        if obj_val is not None:
            self._value = str(obj_val)

    def is_valid(self):
        if self._value is None:
            return False

        try:
            value_type = self._value_type
            value_type(self._value)
        except ValueError:
            return False

        if self._length is not None:
            if self._length < len(self._value):
                return False

        return True


@dataclass
class RepoInt(RepositoryValue):
    def __init__(self, obj_val):
        self.value = obj_val
        self._length = 11
        self._value_type = int


@dataclass
class RepoVarchar(RepositoryValue):
    def __init__(self, obj_val):
        self.value = obj_val
        self._length = 255
        self._value_type = str


@dataclass
class RepoText(RepositoryValue):
    def __init__(self, obj_val):
        self.value = obj_val
        self._value_type = str


@dataclass
class RepoDecimal(RepositoryValue):
    def __init__(self, obj_val):
        self.value = obj_val
        self._length = 18
        self._value_type = float


@dataclass
class RepoBool(RepositoryValue):
    def __init__(self, obj_val):
        self.value = obj_val
        self._length = 1
        self._value_type = bool


@dataclass
class RepoDateTime(RepositoryValue):
    def __init__(self, obj_val):
        self.value = obj_val

    @property
    def value(self):
        if self._value is None:
            return None

        obj_val = datetime.datetime.strptime(self._value, config('DATE_TIME_FORMAT'))
        return obj_val

    @value.setter
    def value(self, obj_val):
        if obj_val is not None:
            self._value = str(obj_val)

    def is_valid(self):
        if self._value is None:
            return False

        try:
            datetime.datetime.strptime(self._value, config('DATE_TIME_FORMAT'))
        except ValueError:
            return False

        return True
