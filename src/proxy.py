"""
Proxy

What:
    Put a stand-in object in front of a real object to control access to it.

When / why:
    Use it for lazy loading, permissions, remote calls, or rate limiting around
    an expensive service.
"""

from typing import Protocol


class ImageStore(Protocol):
    def load(self, image_id: str) -> bytes:
        pass


class S3ImageStore:
    def load(self, image_id: str) -> bytes:
        print(f"expensive s3 download for {image_id}")
        return b"image-bytes"


class CachingImageStoreProxy:
    def __init__(self, wrapped: ImageStore) -> None:
        self.wrapped = wrapped
        self.cache: dict[str, bytes] = {}

    def load(self, image_id: str) -> bytes:
        if image_id not in self.cache:
            self.cache[image_id] = self.wrapped.load(image_id)
        return self.cache[image_id]


def main() -> None:
    store = CachingImageStoreProxy(S3ImageStore())
    print(len(store.load("avatar-1")))
    print(len(store.load("avatar-1")))


if __name__ == "__main__":
    main()
