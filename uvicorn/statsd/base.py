from __future__ import annotations

import socket

SOCKET_SINGLETON: socket.socket | None = None


def set_socket(statsd_host: str) -> socket.socket:
    global SOCKET_SINGLETON
    if SOCKET_SINGLETON:
        return SOCKET_SINGLETON

    statsd_host = parse_address(statsd_host)

    if isinstance(statsd_host, str):
        address_family = socket.AF_UNIX
    else:
        address_family = socket.AF_INET

    try:
        SOCKET_SINGLETON = socket.socket(address_family, socket.SOCK_DGRAM)
        SOCKET_SINGLETON.connect(statsd_host)
    except Exception:
        SOCKET_SINGLETON = None
    return SOCKET_SINGLETON


def get_socket() -> socket.socket | None:
    return SOCKET_SINGLETON


def parse_address(netloc):
    host, port = netloc.split(":")[:2]
    return host.lower(), int(port)
