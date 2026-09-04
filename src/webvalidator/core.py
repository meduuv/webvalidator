"""Validation primitives for web-facing values."""

from urllib.parse import urlparse

_ALLOWED_METHODS = {"GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"}


def is_url(value: str) -> bool:
    """Return whether value has an HTTP or HTTPS scheme and a host."""
    parsed = urlparse(value.strip())
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def is_hostname(value: str) -> bool:
    """Return whether value looks like a DNS hostname."""
    value = value.strip().rstrip(".")
    if not value or len(value) > 253 or " " in value:
        return False
    return all(part and len(part) <= 63 and not part.startswith("-") and not part.endswith("-") for part in value.split("."))


def is_http_method(value: str) -> bool:
    """Return whether value is a common HTTP method."""
    return value.upper() in _ALLOWED_METHODS
