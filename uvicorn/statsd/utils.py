from __future__ import annotations

import typing

from uvicorn.statsd.metrics import Counter

T = typing.TypeVar("T")


class SetCounter(set[T]):
    def __init__(self, event_name: str) -> None:
        super().__init__()
        self.event_name = event_name
        self._counter = Counter()

    def add(self, _element: T) -> None:
        super().add(_element)
        self._counter.increment(self.event_name, 1)

    def remove(self, __element) -> None:
        super().remove(__element)
        self._counter.decrement(self.event_name, 1)

    def discard(self, __element) -> None:
        super().discard(__element)
        self._counter.decrement(self.event_name, 1)
