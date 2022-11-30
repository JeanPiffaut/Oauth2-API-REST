from typing import List


class ModelBase:
    _errors: List = []

    @property
    def errors(self):
        return self._errors

    @errors.setter
    def errors(self, error: List):
        self._errors = error

    @property
    def error(self):
        return self.errors

    @error.setter
    def error(self, val):
        self._errors.append(val)
