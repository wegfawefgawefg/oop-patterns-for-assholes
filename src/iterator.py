"""
Iterator

What:
    Traverse a collection without exposing how it stores data internally.

When / why:
    Use it for paginated APIs, streaming database rows, inventories, or any
    collection where callers should just loop.
"""

from collections.abc import Iterator


class PaginatedUsers:
    def __init__(self, pages: list[list[str]]) -> None:
        self.pages = pages

    def __iter__(self) -> Iterator[str]:
        for page_number, page in enumerate(self.pages, start=1):
            print(f"fetch page {page_number}")
            yield from page


def main() -> None:
    users = PaginatedUsers([["ada", "grace"], ["linus"], ["guido"]])
    for username in users:
        print(f"process {username}")


if __name__ == "__main__":
    main()
