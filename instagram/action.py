from .endpoints import Instagram
from typing import Text, Any
import urllib.parse as parse


def follow(username: Text):
    url_to_follow = Instagram.FOLLOW % username
    return url_to_follow


def unfollow(username: Text):
    url_to_unfollow = Instagram.UNFOLLOW % username
    return url_to_unfollow


def like(media_id: Any):
    return Instagram.LIKE % parse.quote_plus(str(media_id))


def unlike(media_id: Any):
    return Instagram.UNLIKE % parse.quote_plus(str(media_id))
