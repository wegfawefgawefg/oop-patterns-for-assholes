"""
Abstract Factory

What:
    Create families of related objects without the app knowing their exact classes.

When / why:
    Use it when an environment switch changes several collaborating services at
    once, such as local fake services versus production cloud services.
"""

from abc import ABC, abstractmethod


class BlobStore(ABC):
    @abstractmethod
    def save(self, path: str, body: bytes) -> str:
        pass


class EmailSender(ABC):
    @abstractmethod
    def send(self, to: str, subject: str) -> None:
        pass


class LocalBlobStore(BlobStore):
    def save(self, path: str, body: bytes) -> str:
        return f"file://tmp/{path} ({len(body)} bytes)"


class LocalEmailSender(EmailSender):
    def send(self, to: str, subject: str) -> None:
        print(f"[local email] to={to} subject={subject}")


class S3BlobStore(BlobStore):
    def save(self, path: str, body: bytes) -> str:
        return f"s3://app-bucket/{path} ({len(body)} bytes)"


class SesEmailSender(EmailSender):
    def send(self, to: str, subject: str) -> None:
        print(f"[ses email] to={to} subject={subject}")


class ServiceFactory(ABC):
    @abstractmethod
    def blob_store(self) -> BlobStore:
        pass

    @abstractmethod
    def email_sender(self) -> EmailSender:
        pass


class LocalServiceFactory(ServiceFactory):
    def blob_store(self) -> BlobStore:
        return LocalBlobStore()

    def email_sender(self) -> EmailSender:
        return LocalEmailSender()


class AwsServiceFactory(ServiceFactory):
    def blob_store(self) -> BlobStore:
        return S3BlobStore()

    def email_sender(self) -> EmailSender:
        return SesEmailSender()


def process_report(factory: ServiceFactory) -> None:
    url = factory.blob_store().save("reports/june.csv", b"user_id,total\n1,42\n")
    factory.email_sender().send("admin@example.com", f"Report ready: {url}")


def main() -> None:
    print("Local stack:")
    process_report(LocalServiceFactory())
    print("\nProduction stack:")
    process_report(AwsServiceFactory())


if __name__ == "__main__":
    main()
