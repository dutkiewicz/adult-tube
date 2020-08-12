import re
from re import Pattern
from typing import List

from extractor.dto import VideoDTO

VIDEO_ID_PATTERN = re.compile('embed/(.*?)"')


def extract_video_id(text: str, pattern: Pattern) -> str:
    return pattern.findall(text)[0]


def extract_image_sequence(text: str, separator: str) -> List[str]:
    return text.split(separator) if text else []


def extract_tags(text: str, separator: str) -> List[str]:
    return text.split(separator) if text else []


def extract_categories(text: str, separator: str) -> List[str]:
    return text.split(separator) if text else []


def extract_actors(text: str, separator: str) -> List[str]:
    return text.split(separator) if text else []


def transform_raw_video_to_video_dto(input: dict) -> VideoDTO:
    return VideoDTO(
        id=extract_video_id(input["iframe_video"], VIDEO_ID_PATTERN),
        main_image_small=input["main_image_thumb"],
        image_sequence_small=extract_image_sequence(input["image_sequence_thumb"], ";"),
        title=input["title"],
        tags=extract_tags(input["tags"], ";"),
        categories=extract_categories(input["categories"], ";"),
        actors=extract_actors(input["actors"], ";"),
        duration=input["duration"],
        views=input["views"],
        upvotes=input["upvotes"],
        downvotes=input["downvotes"],
        main_image_big=input["main_image"],
        image_sequence_big=extract_image_sequence(input["image_sequence"], ";"),
    )
