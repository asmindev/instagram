from typing import Any, List, Text, Dict
from .request import Session
from .endpoints import endpoints
from . import action
from . import parse
from .models import Models
import re
import json


class Instagram(Session):
    HTTP_OK = 200

    def __init__(self, user_agent: Text | Any = None):
        super().__init__(user_agent=user_agent)
        Instagram.FOLLOWERS = 10
        self.__models = Models()

    def __override(self, result: Dict):
        Instagram.FOLLOWERS = result["edge_followed_by"]
        Instagram.FOLLOWING = result["edge_follow"]
        Instagram.USER_ID = result["id"]
        Instagram.USERNAME = result["username"]
        Instagram.PROFILE_PIC_URL = result["profile_pic_url_hd"]
        Instagram.IS_PRIVATE = result["is_private"]
        Instagram.IS_VERIFIED = result["is_verified"]
        Instagram.FULLNAME = result["fullname"]

    def follow(self, user_id: Text) -> Dict:
        """
        Follow instagram user
        --------------------

        user_id: Text = Instagram user id
        rtype: json data type
        """
        response = self.requests.post(action.follow_url(user_id), data={})
        if response.status_code == Instagram.HTTP_OK:
            try:
                return response.json()
            except json.decoder.JSONDecodeError:
                return dict(status="ok", result="requested")

        else:
            return parse.uknown(response.status_code)

    def unfollow(self, user_id: Text) -> Dict:
        """
        Unfollow instagram user
        --------------------

        user_id: Text = Instagram user id
        rtype: json data type
        """
        response = self.requests.post(action.unfollow_url(user_id), data={})
        if response.status_code == Instagram.HTTP_OK:
            return response.json()
        else:
            return parse.uknown(response.status_code)

    def like(self, post_id: Text) -> Dict:
        """
        Like post simplecity
        --------------------

        post_id: Text = Instagram post id
        rtype: json data type
        """
        response = self.requests.post(
            action.like_url(media_id=post_id), data={})
        if response.status_code == Instagram.HTTP_OK:
            return response.json()
        else:
            return parse.uknown(response.status_code)

    def unlike(self, post_id: Text):
        """
        Unlike post simplecity
        --------------------

        post_id: Text = Instagram post id
        rtype: json data type
        """
        response = self.requests.post(
            action.unlike_url(media_id=post_id), data={})
        if response.status_code == Instagram.HTTP_OK:
            return response.json()
        else:
            return parse.uknown(response.status_code)

    def get_user_followings(
        self, user_id: Text, count_per_page: int = 12, end_cursor=None
    ) -> Dict:
        """
        Get user followings instagram
        -----------------------------

        user_id: Text = Instagram user id
        count_per_page: int = How many user in per page. default 12
        end_cursor: None = If have more page
        return json type
        """
        response = self.requests.get(
            self.__models.generate_url_get_followings(
                user_id=user_id, count=str(count_per_page), end_cursor=end_cursor
            )
        )
        if response.status_code == Instagram.HTTP_OK:
            return response.json()
        else:
            return parse.uknown(response.status_code)

    def get_user_followers(
        self, user_id: Text, count_per_page: int = 12, end_cursor=None
    ) -> Dict:
        """
        Get user followers instagram
        -----------------------------

        user_id: Text = Instagram user id
        count_per_page: int = How many user in per page. default 12
        end_cursor: None = If have more page
        return json type
        """
        response = self.requests.get(
            self.__models.generate_url_get_followers(
                user_id=user_id, count=str(count_per_page), end_cursor=end_cursor
            )
        )
        if response.status_code == Instagram.HTTP_OK:
            return response.json()
        else:
            return parse.uknown(response.status_code)

    def get_post_user(
        self, user_id: Text, count_post_per_page: int = 12, end_cursor=None
    ) -> Dict:
        """
        Get user post instagram
        -----------------------

        user_id: Text = Instagram user id
        count_post: int = How many post in per page. default 12
        end_cursor: None = If have more page
        return json type
        """
        response = self.requests.get(
            self.__models.generate_url_get_post(
                user_id=user_id,
                count_post=str(count_post_per_page),
                end_cursor=end_cursor,
            )
        )
        if response.status_code == Instagram.HTTP_OK:
            return response.json()
        else:
            return parse.uknown(response.status_code)

    def get_details_user_login(self):
        """
        Get details information instagram user logged.
        ---------------------------------------

        rtype: Dict
        """
        response = self.requests.get(endpoints.BASE_URL)
        if response.status_code == Instagram.HTTP_OK:
            graphql = re.findall(
                r"window._sharedData = (.+);</script>", response.text)
            if graphql:
                username = json.loads(graphql[0])[
                    "config"]["viewer"]["username"]
                result = self.get_user_info(username)
                if result.get("id"):
                    self.__override(result)
                return result
        else:
            return parse.uknown(response.status_code, message="uknown error")

    def get_user_info(self, username: Text, less=True) -> Dict:
        """
        Get details information instagram user.
        ---------------------------------------

        username: Text = "Instagram username"
        less: bool = More information. default `less`
        rtype: Dict
        """
        response = self.requests.get(endpoints.ACCOUNT_JSON_INFO % username)
        if response.status_code == Instagram.HTTP_OK:
            info = response.json()
            return parse.details_user(info, less=less)
        else:
            return parse.uknown(response.status_code)

    def get_post_info(self, post_id: Text) -> Dict:
        """
        Get details information media post.
        -----------------------------------

        media_id: Text = "Instagram media post id"
        rtype: Dict
        """
        response = self.requests.get(endpoints.MEDIA_JSON_INFO % post_id)
        if response.status_code == Instagram.HTTP_OK:
            return response.json()
        else:
            return parse.uknown(response.status_code)

    def get_stories(self, username: Text = None, link: Text = None):
        """
        Get details information about story.
        ---------------------------------------

        username: Text = "instagram username". default `None`
        link: Text = "instagram stories url". default `None`
        rtype: Dict
        """
        story_id: Text = ""
        status_code = Instagram.HTTP_OK
        if not username and not link:
            raise TypeError(
                "get_stories() missing one arguments: username or link")
        if link:
            username, story_id = re.findall(r"stories/(.*?)/(\d+)", link)[0]
        if username:
            user_id = self.get_user_info(username)["id"]
            url = self.__models.generate_url_get_story(user_id)
            response = self.requests.get(url)
            if response.status_code == Instagram.HTTP_OK:
                result = parse.stories_details(
                    response.json(), story_id=story_id)
                return result
            else:
                status_code = response.status_code
        else:
            return parse.uknown(status_code, message="invalid username")

    def get_reel(self, link: Text, less=True):
        """
        Get details information about reel.
        ---------------------------------------

        link: Text = "instagram reel url"
        less: bool = More information. default `less: True`
        rtype: Dict
        """
        response = self.requests.get(link)
        if response.status_code == Instagram.HTTP_OK:
            graphql: List = re.findall(r'({"graphql":.*?)\);', response.text)
            if graphql:
                result = json.loads(graphql[0])
                return parse.reels_details(result, less=less)
        return parse.uknown(response.status_code)
