"""
Thread-safe rate limiter for VacancyFlow.

Designed to respect robots.txt request-rate directives and prevent
overloading remote servers.

Example:
    limiter = RateLimiter(requests=2, period=4)

    limiter.wait()
    response = client.get(url)
"""

from __future__ import annotations

import threading
import time
from collections import deque


class RateLimiter:
    """
    Sliding-window rate limiter.

    Allows at most `requests` requests during every `period`
    seconds.

    Example:
        limiter = RateLimiter(requests=2, period=4)

        limiter.wait()
        client.get(...)
    """

    def __init__(self, requests: int, period: float) -> None:
        if requests <= 0:
            raise ValueError("requests must be greater than zero")

        if period <= 0:
            raise ValueError("period must be greater than zero")

        self.requests = requests
        self.period = float(period)

        self._timestamps: deque[float] = deque()
        self._lock = threading.Lock()

    def wait(self) -> None:
        """
        Block until another request is allowed.

        Safe for concurrent threads.
        """
        while True:
            with self._lock:
                now = time.monotonic()

                # Remove expired timestamps
                while (
                    self._timestamps
                    and now - self._timestamps[0] >= self.period
                ):
                    self._timestamps.popleft()

                # Capacity available
                if len(self._timestamps) < self.requests:
                    self._timestamps.append(now)
                    return

                # Calculate remaining wait time
                sleep_for = (
                    self.period - (now - self._timestamps[0])
                )

            if sleep_for > 0:
                time.sleep(sleep_for)

    def reset(self) -> None:
        """
        Clear limiter history.

        Mostly useful for testing.
        """
        with self._lock:
            self._timestamps.clear()

    @property
    def queued_requests(self) -> int:
        """
        Number of requests currently inside the active window.
        """
        with self._lock:
            now = time.monotonic()

            while (
                self._timestamps
                and now - self._timestamps[0] >= self.period
            ):
                self._timestamps.popleft()

            return len(self._timestamps)

    @property
    def available(self) -> int:
        """
        Remaining requests allowed immediately.
        """
        return self.requests - self.queued_requests