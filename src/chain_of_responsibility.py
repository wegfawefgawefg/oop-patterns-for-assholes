"""
Chain of Responsibility

What:
    Pass a request through handlers until one handles it.

When / why:
    Use it for middleware-style backend flows: auth, rate limits, validation,
    routing, and policy checks.
"""

from dataclasses import dataclass


@dataclass
class Request:
    user_id: str | None
    path: str
    requests_this_minute: int


class Handler:
    def __init__(self, next_handler: "Handler | None" = None) -> None:
        self.next_handler = next_handler

    def handle(self, request: Request) -> str:
        if self.next_handler is None:
            return "200 OK"
        return self.next_handler.handle(request)


class AuthHandler(Handler):
    def handle(self, request: Request) -> str:
        if request.user_id is None:
            return "401 Unauthorized"
        return super().handle(request)


class RateLimitHandler(Handler):
    def handle(self, request: Request) -> str:
        if request.requests_this_minute > 100:
            return "429 Too Many Requests"
        return super().handle(request)


def main() -> None:
    pipeline = AuthHandler(RateLimitHandler())
    print(pipeline.handle(Request(None, "/api/profile", 1)))
    print(pipeline.handle(Request("user_42", "/api/profile", 150)))
    print(pipeline.handle(Request("user_42", "/api/profile", 2)))


if __name__ == "__main__":
    main()
