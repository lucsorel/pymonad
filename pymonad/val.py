from typing import Callable, List

class Val:
    def __init__(self, *args):
        raise NotImplementedError('use Val.of to create a value holder')

    def map(self, mapper: Callable):
        raise NotImplementedError()

    def flatMap(self, mapperToVal: Callable):
        raise NotImplementedError()

    def get(self, default=None):
        raise NotImplementedError()

    def orElseCall(self, alternate=Callable):
        raise NotImplementedError()

    def isNothing(self):
        raise NotImplementedError()

    @staticmethod
    def of(value):
        if value is None:
            return Nothing()
        else:
            return Some(value)

    @staticmethod
    def flatMapAllOrElse(vals: List, allMapper: Callable, alternate: Callable=None):
        hasNothings = next((val for val in vals if val.isNothing()), False)

        if hasNothings:
            if alternate is None:
                return None
            else:
                return Val.of(alternate())
        else:
            return allMapper(*[val.get() for val in vals])

    def __repr__(self) -> str:
        return self.__str__()


class Some(Val):
    def __init__(self, value):
        if value is None:
            raise ValueError('cannot create a Some instance wrapping a None value')
        self._value = value

    def map(self, mapper: Callable) -> Val:
        return Val.of(mapper(self._value))

    def flatMap(self, mapperToVal: Callable) -> Val:
        return mapperToVal(self._value)

    def get(self, default=None):
        return self._value

    def orElseCall(self, alternate=Callable) -> Val:
        return self

    def isNothing(self):
        return False

    def __str__(self) -> str:
        return f'Some({self._value})'

class Nothing(Val):
    def __init__(self, *args):
        pass

    def map(self, mapper: Callable) -> Val:
        return self

    def flatMap(self, mapperToVal: Callable) -> Val:
        return self

    def get(self, default=None):
        return default

    def orElseCall(self, alternate=Callable) -> Val:
        return Val.of(alternate())

    def isNothing(self):
        return True

    def __str__(self) -> str:
        return 'Nothing'
