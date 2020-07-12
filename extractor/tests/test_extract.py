import pytest
import responses
from requests.exceptions import ConnectionError

from extractor.extract import SourceContent


@pytest.fixture
def response_content():
    return b"file content from url"


class TestSourceContent:
    @responses.activate
    def test_raises_error_for_non_existing_url(self):
        with pytest.raises(ConnectionError):
            content = SourceContent("http://example.com")
            next(content.as_stream())

    @responses.activate
    def test_returns_stream_content(self, response_content):
        responses.add(responses.GET, "http://url.com", body=response_content)

        content = SourceContent("http://url.com")
        assert b"".join([bytes(x) for x in content.as_stream()]) == response_content

    @responses.activate
    def test_returns_temp_file(self, response_content):
        responses.add(responses.GET, "http://url.com", body=response_content)

        content = SourceContent("http://url.com")
        with content.as_temp_file() as f:
            assert f.read() == response_content
