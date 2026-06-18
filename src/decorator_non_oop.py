"""
Decorator idea, but without @decorator syntax

What:
    Add behavior around a plain function without changing the caller.

When / why:
    Use this when a literal @decorator feels too magical. The get_name function
    stays free-standing, and a small cache object handles the repeated lookup.
"""


class NameCache:
    def __init__(self) -> None:
        self.names: dict[int, str] = {}

    def has(self, user_id: int) -> bool:
        return user_id in self.names

    def get(self, user_id: int) -> str:
        return self.names[user_id]

    def set(self, user_id: int, name: str) -> None:
        self.names[user_id] = name


name_cache = NameCache()


def get_name(user_id: int) -> str:
    if name_cache.has(user_id):
        return name_cache.get(user_id)

    print(f"database lookup for user {user_id}")
    name = "Ada"
    name_cache.set(user_id, name)
    return name


def main() -> None:
    print(get_name(1))
    print(get_name(1))
    print(get_name(2))


if __name__ == "__main__":
    main()
