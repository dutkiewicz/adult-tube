from dataclasses import dataclass
from typing import List


@dataclass
class VideoDTO:
    id: str
    main_image_small: str
    image_sequence_small: List[str]
    title: str
    tags: List[str]
    categories: List[str]
    actors: List[str]
    duration: int
    views: int
    upvotes: int
    downvotes: int
    main_image_big: str
    image_sequence_big: List[str]
