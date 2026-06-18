"""
Template Method

What:
    Define the skeleton of an algorithm in a base class, then let subclasses fill
    in specific steps.

When / why:
    Use it when jobs share the same lifecycle but differ in a few details, such
    as importers, exporters, test fixtures, or deployment tasks.
"""

from abc import ABC, abstractmethod


class ImportJob(ABC):
    def run(self) -> None:
        raw = self.fetch()
        rows = self.parse(raw)
        self.save(rows)

    @abstractmethod
    def fetch(self) -> str:
        pass

    @abstractmethod
    def parse(self, raw: str) -> list[dict]:
        pass

    def save(self, rows: list[dict]) -> None:
        print(f"saved {len(rows)} rows")


class CsvUserImport(ImportJob):
    def fetch(self) -> str:
        return "id,name\n1,Ada\n2,Grace"

    def parse(self, raw: str) -> list[dict]:
        lines = raw.splitlines()[1:]
        return [{"id": line.split(",")[0], "name": line.split(",")[1]} for line in lines]


def main() -> None:
    CsvUserImport().run()


if __name__ == "__main__":
    main()
