"""
Builder

What:
    Build a complex object step by step instead of passing a giant constructor
    full of optional arguments.

When / why:
    Use it for backend queries, game entities, or API requests where readable
    setup matters and some fields are optional.
"""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class SearchQuery:
    index: str
    filters: list[str] = field(default_factory=list)
    sort: str | None = None
    limit: int = 20


class SearchQueryBuilder:
    def __init__(self, index: str) -> None:
        self._index = index
        self._filters: list[str] = []
        self._sort: str | None = None
        self._limit = 20

    def where(self, field_name: str, value: str) -> "SearchQueryBuilder":
        self._filters.append(f"{field_name}:{value}")
        return self

    def sort_by(self, field_name: str) -> "SearchQueryBuilder":
        self._sort = field_name
        return self

    def limit(self, count: int) -> "SearchQueryBuilder":
        self._limit = count
        return self

    def build(self) -> SearchQuery:
        return SearchQuery(self._index, self._filters, self._sort, self._limit)


def main() -> None:
    query = (
        SearchQueryBuilder("players")
        .where("region", "na")
        .where("rank", "diamond")
        .sort_by("-last_login")
        .limit(5)
        .build()
    )
    print(query)


if __name__ == "__main__":
    main()
