"""
Singleton

What:
    Ensure one shared instance exists for a class.

When / why:
    Use carefully. It can be acceptable for process-wide infrastructure like a
    metrics registry, but it is easy to overuse and makes tests harder.
"""


class MetricsRegistry:
    _instance: "MetricsRegistry | None" = None

    def __new__(cls) -> "MetricsRegistry":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.counters = {}
        return cls._instance

    def increment(self, name: str) -> None:
        self.counters[name] = self.counters.get(name, 0) + 1


def main() -> None:
    web_handler_metrics = MetricsRegistry()
    job_worker_metrics = MetricsRegistry()

    web_handler_metrics.increment("http.requests")
    job_worker_metrics.increment("http.requests")
    job_worker_metrics.increment("jobs.completed")

    print(web_handler_metrics.counters)
    print(web_handler_metrics is job_worker_metrics)


if __name__ == "__main__":
    main()
