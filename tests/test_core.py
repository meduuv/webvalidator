from webvalidator import is_hostname, is_http_method, is_url


def test_url():
    assert is_url("https://example.com/path")
    assert not is_url("example.com")


def test_hostname():
    assert is_hostname("example.com")
    assert not is_hostname("bad host")


def test_method():
    assert is_http_method("get")
    assert not is_http_method("TRACE")
