import json
import urllib.parse as parse
from .endpoints import endpoints
from typing import Text


class Models:
    def __init__(self):
        pass

    def generate_url_get_followers(self, user_id: Text, count: Text, end_cursor=None):
        if not end_cursor:
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
            url = endpoints.FOLLOWERS_FIRST % query
        else:
            url = endpoints.AFTER_FIRST_FOLLOWERS % (
                user_id, count, end_cursor)
        return url

    def generate_url_get_followings(self, user_id: Text, count: Text, end_cursor=None):
        if not end_cursor:
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
            url = endpoints.FOLLOWING_FIRST % query
        else:
            url = endpoints.AFTER_FIRST_FOLLOWING % (
                user_id, count, end_cursor)
        return url

    def generate_url_get_post(
        self, user_id: Text, count_post: Text = "20", end_cursor=None
    ):
        if not end_cursor:
            url = (
                endpoints.GRAPHQL
                + "?query_hash=d04b0a864b4b54837c0d870b0e77e076&variables="
                + parse.quote_plus(
                    json.dumps(
                        {"id": str(user_id), "first": count_post},
                        separators=(",", ";"),
                    )
                ).replace("3B", "3A")
            )
        else:
            params = dict(
                query_id=endpoints.MEDIA, id=user_id, after=end_cursor, first=count_post
            )
            url = endpoints.GRAPHQL + "?" + parse.urlencode(params)
        return url

    def generate_url_get_story(self, user_id: Text):
        variables = {
            "reel_ids": [user_id],
            "tag_names": [],
            "location_ids": [],
            "highlight_reel_ids": [],
            "precomposed_overlay": False,
            "show_story_viewer_list": True,
            "story_viewer_fetch_count": 50,
            "story_viewer_cursor": "",
        }
        result = parse.quote_plus(json.dumps(variables, separators=(",", ":")))
        return endpoints.STORY % result
