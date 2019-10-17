from typing import Callable, List, TypeVar, Generic

I = TypeVar('I')
O = TypeVar('O')

class Val(Generic[I]):
    def __init__(self, *args):
        raise NotImplementedError('use Val.of to create a value holder')

    def map(self, mapper: Callable[[I], O]) -> 'Val[O]':
        raise NotImplementedError()

    def flatMap(self, mapperToVal: Callable[[I], 'Val[O]']) -> 'Val[O]':
        raise NotImplementedError()

    def get(self, default=None) -> I:
        raise NotImplementedError()

    def orElseCall(self, alternate=Callable[[], I]) -> 'Val[I]':
        raise NotImplementedError()

    def orElseFlatCall(self, alternate=Callable[[], 'Val[I]']) -> 'Val[I]':
        raise NotImplementedError()

    def isNothing(self) -> bool:
        raise NotImplementedError()

    @staticmethod
    def of(value: I) -> 'Val[I]':
        if value is None:
            return Nothing()
        else:
            return Some(value)

    @staticmethod
    def flatMapAllOrElse(vals: List, allMapper: Callable[[], O], alternate: Callable[[], O]=None) -> 'Val[O]':
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


class Some(Val[I]):
    def __init__(self, value):
        if value is None:
            raise ValueError('cannot create a Some instance wrapping a None value')
        self._value = value

    def map(self, mapper: Callable[[I], O]) -> Val[O]:
        return Val.of(mapper(self._value))

    def flatMap(self, mapperToVal: Callable[[I], Val[O]]) -> Val[O]:
        return mapperToVal(self._value)

    def get(self, default: I=None) -> I:
        return self._value

    def orElseCall(self, alternate=Callable[[], I]) -> Val[I]:
        return self

    def orElseFlatCall(self, alternate=Callable[[], Val[I]]) -> Val[I]:
        return self

    def isNothing(self) -> bool:
        return False

    def __str__(self) -> str:
        return f'Some({self._value})'

class Nothing(Val[I]):
    def __init__(self, *args):
        pass

    def map(self, mapper: Callable[[I], O]) -> Val[O]:
        return self

    def flatMap(self, mapperToVal: Callable[[I], Val[O]]) -> Val[O]:
        return self

    def get(self, default: I=None) -> I:
        return default

    def orElseCall(self, alternate=Callable[[], I]) -> Val[I]:
        return Val.of(alternate())

    def orElseFlatCall(self, alternate=Callable[[], Val[I]]) -> Val[I]:
        return alternate()

    def isNothing(self) -> bool:
        return True

    def __str__(self) -> str:
        return 'Nothing'
