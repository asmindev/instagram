from .endpoints import endpoints
from typing import Text, Any
import urllib.parse as parse


def follow_url(user_id: Text):
    url_to_follow = endpoints.FOLLOW % user_id
    return url_to_follow


def unfollow_url(user_id: Text):
    url_to_unfollow = endpoints.UNFOLLOW % user_id
    return url_to_unfollow


def like_url(media_id: Any):
    return endpoints.LIKE % parse.quote_plus(str(media_id))


def unlike_url(media_id: Any):
    return endpoints.UNLIKE % parse.quote_plus(str(media_id))
