from typing import Text
from .endpoints import Instagram
import urllib.parse as parse
import json


class Models:
    def __init__(self):
        pass

    def generate_url_get_followers(self, user_id: Text, count: Text, next_page=None):
        if not next_page:
            query = parse.quote_plus(
                json.dumps(
                    {
                        "id": user_id,
                        "include_reel": "true",
                        "fetch_mutual": "true",
                        "first": count,
                    },
                    separators=(",", ";"),
                )
            ).replace("3B", "3A")
            url = Instagram.FOLLOWERS_FIRST % query
        else:
            url = Instagram.AFTER_FIRST_FOLLOWERS % (user_id, count, next_page)
        return url

    def generate_url_get_followings(self, user_id: Text, count: Text, next_page=None):
        if not next_page:
            query = parse.quote_plus(
                json.dumps(
                    {
                        "id": user_id,
                        "include_reel": "true",
                        "fetch_mutual": "true",
                        "first": count,
                    },
                    separators=(",", ";"),
                )
            ).replace("3B", "3A")
            url = Instagram.FOLLOWING_FIRST % query
        else:
            url = Instagram.AFTER_FIRST_FOLLOWING % (user_id, count, next_page)
        return url

    def generate_url_get_post(
        self, media_id: Text, count_post: Text = "20", next_page=None
    ):
        if not next_page:
            url = (
                Instagram.GRAPHQL
                + "?query_hash=d04b0a864b4b54837c0d870b0e77e076&variables="
                + parse.quote_plus(
                    json.dumps(
                        {"id": str(media_id), "first": count_post},
                        separators=(",", ";"),
                    )
                ).replace("3B", "3A")
            )
        else:
            params = dict(
                query_id=Instagram.MEDIA, id=media_id, after=next_page, first=count_post
            )
            url = Instagram.GRAPHQL + "?" + parse.urlencode(params)
        return url
