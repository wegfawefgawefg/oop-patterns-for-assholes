"""
Decorator

What:
    Wrap an object to add behavior while keeping the same interface.

When / why:
    Use it for cross-cutting backend behavior like caching, logging, retries, or
    authorization without changing the core service.
"""

from typing import Protocol


class UserRepository(Protocol):
    def get_name(self, user_id: int) -> str:
        pass


class DatabaseUserRepository:
    def get_name(self, user_id: int) -> str:
        print(f"database lookup for user {user_id}")
        return "Ada"


class CachedUserRepository:
    def __init__(self, wrapped: UserRepository) -> None:
        self.wrapped = wrapped
        self.cache: dict[int, str] = {}

    def get_name(self, user_id: int) -> str:
        if user_id not in self.cache:
            name = self.wrapped.get_name(user_id)
            self.cache[user_id] = name
            return name
        
        return self.cache[user_id]


def main() -> None:
    repo = CachedUserRepository(DatabaseUserRepository())
    print(repo.get_name(1))
    print(repo.get_name(1))


if __name__ == "__main__":
    main()
