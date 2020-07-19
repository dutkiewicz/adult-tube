import re
from re import Pattern
from typing import List

VIDEO_ID_PATTERN = re.compile('embed\/(.*?)"')


def extract_video_id(text: str, pattern: Pattern) -> str:
    return pattern.findall(text)[0]


def extract_image_sequence(text: str, separator: str) -> List[str]:
    return text.split(separator)
