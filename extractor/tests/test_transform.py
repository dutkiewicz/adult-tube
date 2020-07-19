from extractor.transform import VIDEO_ID_PATTERN, extract_image_sequence, extract_video_id


def test_extract_video_id_returns_video_id_from_iframe():
    input_txt = '<iframe src="https://www.tubesite.com/embed/44bc40f3bc04f65b7a35" frameborder="0" height="481" width="608" scrolling="no"></iframe>'
    assert extract_video_id(input_txt, VIDEO_ID_PATTERN) == "44bc40f3bc04f65b7a35"


def test_extract_image_sequence_returns_list_of_urls():
    source_txt = "https://ci.phncdn.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)1.jpg;https://ci.phncdn.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)2.jpg;https://ci.phncdn.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)3.jpg;https://ci.phncdn.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)4.jpg;https://ci.phncdn.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)5.jpg;https://ci.phncdn.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)6.jpg;https://ci.phncdn.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)7.jpg;https://ci.phncdn.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)8.jpg;https://ci.phncdn.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)9.jpg;https://ci.phncdn.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)10.jpg;https://ci.phncdn.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)11.jpg;https://ci.phncdn.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)12.jpg;https://ci.phncdn.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)13.jpg;https://ci.phncdn.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)14.jpg;https://ci.phncdn.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)15.jpg;https://ci.phncdn.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)16.jpg"
    assert extract_image_sequence(source_txt, ";") == [
        "https://ci.phncdn.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)1.jpg",
        "https://ci.phncdn.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)2.jpg",
        "https://ci.phncdn.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)3.jpg",
        "https://ci.phncdn.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)4.jpg",
        "https://ci.phncdn.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)5.jpg",
        "https://ci.phncdn.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)6.jpg",
        "https://ci.phncdn.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)7.jpg",
        "https://ci.phncdn.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)8.jpg",
        "https://ci.phncdn.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)9.jpg",
        "https://ci.phncdn.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)10.jpg",
        "https://ci.phncdn.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)11.jpg",
        "https://ci.phncdn.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)12.jpg",
        "https://ci.phncdn.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)13.jpg",
        "https://ci.phncdn.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)14.jpg",
        "https://ci.phncdn.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)15.jpg",
        "https://ci.phncdn.com/videos/201010/27/267/original/(m=eaf8Ggaaaa)(mh=MfCPJy4vlF9ZUl1_)16.jpg",
    ]
