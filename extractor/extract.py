from tempfile import TemporaryFile
from typing import IO, Generator

import requests


class SourceContent:
    def __init__(self, url: str) -> None:
        self.url = url

    def _get_url(self) -> Generator:
        with requests.get(self.url, stream=True) as response:
            response.raise_for_status()
            for chunk in response.iter_lines():
                yield chunk

    def as_temp_file(self) -> IO[bytes]:
        file = TemporaryFile()
        for chunk in self._get_url():
            file.write(chunk)
        file.seek(0)
        return file

    def as_stream(self) -> Generator:
        return self._get_url()
