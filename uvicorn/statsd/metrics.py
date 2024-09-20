from uvicorn.statsd.base import get_socket


class Counter:
    def increment(self, key: str, value: int, rate: float = 1.0) -> None:
        msg = f"{key}:{value}|c|@{rate}"
        self._send(msg)

    def decrement(self, key: str, value: int, rate: float = 1.0) -> None:
        msg = f"{key}:-{value}|c|@{rate}"
        self._send(msg)

    def _send(self, msg: str) -> None:
        socket_ = get_socket()
        if socket_ is None:
            return
        socket_.send(msg.encode("ascii"))
