from dataclasses import dataclass
from typing import Text
import re


@dataclass
class endpoints:
    MEDIA: Text = "17880160963012870"
    USER_AGENT: Text = "Mozilla/5.0 (Linux; Android 9; SM-A102U Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 Instagram 155.0.0.37.107 Android (28/9; 320dpi; 720x1468; samsung; SM-A102U; a10e; exynos7885; en_US; 239490550)"
    BASE_URL: Text = "https://instagram.com"
    LOGIN_URL: Text = BASE_URL + "/accounts/login/ajax/"
    ACCOUNT_JSON_INFO = BASE_URL + "/%s/channel/?__a=1"
    MEDIA_JSON_INFO = BASE_URL + "/p/%s/?__a=1"
    MID: Text = BASE_URL + "/web/__mid/"
    FOLLOW: Text = BASE_URL + "/web/friendships/%s/follow/"
    UNFOLLOW: Text = BASE_URL + "/web/friendships/%s/unfollow/"
    LIKE: Text = BASE_URL + "/web/likes/%s/like/"
    UNLIKE: Text = BASE_URL + "/web/likes/%s/unlike/"
    GRAPHQL: Text = BASE_URL + "/graphql/query/"
    REELS: Text = BASE_URL + "/reel/%s/?__a=1"
    STORY: Text = GRAPHQL + "?query_hash=de8017ee0a7c9c45ec4260733d81ea31&variables=%s"
    FOLLOWERS_FIRST: Text = (
        GRAPHQL + "?query_hash=c76146de99bb02f6415203be841dd25a&variables=%s"
    )
    AFTER_FIRST_FOLLOWERS: Text = (
        GRAPHQL + "?query_id=17851374694183129&id=%s&first=%s&after=%s"
    )
    FOLLOWING_FIRST: Text = (
        GRAPHQL + "?query_hash=d04b0a864b4b54837c0d870b0e77e076&variables=%s"
    )
    AFTER_FIRST_FOLLOWING: Text = (
        GRAPHQL + "?query_id=17851374694183129&id=%s&first=%s&after=%s"
    )

    def __init__(self) -> None:
        pass

    def csrftoken(self, response: Text):
        return re.findall('"csrf_token":"(.*?)",', response)[0]
