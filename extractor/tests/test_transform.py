from extractor.transform import (
    VIDEO_ID_PATTERN,
    extract_actors,
    extract_categories,
    extract_image_sequence,
    extract_tags,
    extract_video_id,
    transform_raw_video_to_video_dto,
)


def test_extract_video_id_returns_video_id_from_iframe():
    input_txt = '<iframe src="https://www.tubesite.com/embed/44bc40f3bc04f65b7a35" frameborder="0" height="481" width="608" scrolling="no"></iframe>'
    assert extract_video_id(input_txt, VIDEO_ID_PATTERN) == "44bc40f3bc04f65b7a35"


def test_extract_image_sequence_returns_list_of_urls():
    source_txt = (
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)1.jpg;"
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)2.jpg;"
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)3.jpg;"
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)4.jpg;"
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)5.jpg;"
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)6.jpg;"
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)7.jpg;"
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)8.jpg;"
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)9.jpg;"
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)10.jpg;"
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)11.jpg;"
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)12.jpg;"
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)13.jpg;"
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)14.jpg;"
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)15.jpg;"
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)16.jpg"
    )

    assert extract_image_sequence(source_txt, ";") == [
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)1.jpg",
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)2.jpg",
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)3.jpg",
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)4.jpg",
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)5.jpg",
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)6.jpg",
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)7.jpg",
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)8.jpg",
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)9.jpg",
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)10.jpg",
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)11.jpg",
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)12.jpg",
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)13.jpg",
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)14.jpg",
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)15.jpg",
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)16.jpg",
    ]


def test_extract_categories_returns_list_of_categories():
    source_txt = "Homemade;DYI;Blue curtains"
    assert extract_categories(source_txt, ";") == ["Homemade", "DYI", "Blue curtains"]


def test_extract_tags_returns_list_of_tags():
    source_txt = "clever;curtains;original recipe"
    assert extract_tags(source_txt, ";") == ["clever", "curtains", "original recipe"]


def test_extract_actors_returns_list_of_actors():
    source_txt = "Anna;Dan;Jeniffer Love-Hewitt"
    assert extract_actors(source_txt, ";") == ["Anna", "Dan", "Jeniffer Love-Hewitt"]


def test_extract_categories_for_empty_string_returns_empty_list():
    source_txt = ""
    assert extract_categories(source_txt, ";") == []


def test_extract_tags_for_empty_string_returns_empty_list():
    source_txt = ""
    assert extract_tags(source_txt, ";") == []


def test_extract_actors_for_empty_string_returns_empty_list():
    source_txt = ""
    assert extract_actors(source_txt, ";") == []


def test_returns_video_dto_for_raw_video_dictionary():
    image_sequence = (
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)1.jpg;"
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)2.jpg;"
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)3.jpg;"
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)4.jpg;"
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)5.jpg;"
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)6.jpg;"
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)7.jpg;"
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)8.jpg;"
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)9.jpg;"
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)10.jpg;"
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)11.jpg;"
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)12.jpg;"
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)13.jpg;"
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)14.jpg;"
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)15.jpg;"
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)16.jpg"
    )

    raw_video_data = {
        "iframe_video": '<iframe src="https://www.domain.com/embed/44bc40f3bc04f65b7a35" frameborder="0" height="481" width="608" scrolling="no"></iframe>',
        "main_image_thumb": "https://ci.domain.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)4.jpg",
        "image_sequence_thumb": image_sequence,
        "title": "A video title",
        "tags": "clever;curtains;original recipe",
        "categories": "Homemade;DYI;Blue curtains",
        "actors": "Anna;Dan;Jeniffer Love-Hewitt",
        "duration": 1234,
        "views": 999999,
        "upvotes": 23,
        "downvotes": 54,
        "main_image": "https://ci.domain.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)4.jpg",
        "image_sequence": image_sequence,
    }
    expected_image_sequence = [
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)1.jpg",
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)2.jpg",
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)3.jpg",
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)4.jpg",
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)5.jpg",
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)6.jpg",
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)7.jpg",
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)8.jpg",
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)9.jpg",
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)10.jpg",
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)11.jpg",
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)12.jpg",
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)13.jpg",
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)14.jpg",
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)15.jpg",
        "https://ci.tubesite.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)16.jpg",
    ]

    dto = transform_raw_video_to_video_dto(raw_video_data)

    assert dto.id == "44bc40f3bc04f65b7a35"
    assert dto.main_image_small == raw_video_data["main_image_thumb"]
    assert dto.image_sequence_small == expected_image_sequence
    assert dto.title == raw_video_data["title"]
    assert dto.tags == ["clever", "curtains", "original recipe"]
    assert dto.categories == ["Homemade", "DYI", "Blue curtains"]
    assert dto.actors == ["Anna", "Dan", "Jeniffer Love-Hewitt"]
    assert dto.duration == raw_video_data["duration"]
    assert dto.views == raw_video_data["views"]
    assert dto.upvotes == raw_video_data["upvotes"]
    assert dto.downvotes == raw_video_data["downvotes"]
    assert dto.main_image_big == raw_video_data["main_image"]
    assert dto.image_sequence_big == expected_image_sequence
