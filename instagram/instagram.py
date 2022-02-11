from typing import Text, Dict

import requests
from .request import Session
from .endpoints import endpoints
from . import action
from .models import Models


class Instagram(Session):
    HTTP_OK = 200

    def __init__(self):
        super().__init__()
        self.__models = Models()

    def follow(self, user_id: Text) -> Dict:
        """
        Follow instagram user
        --------------------

        user_id: Text = Instagram user id
        rtype: json data type
        """
        response = self.session.post(action.follow_url(user_id), data={})
        if response.status_code == Instagram.HTTP_OK:
            return response.json()
        else:
            return dict(
                success=False,
                status="ok",
                message="uknown error",
                status_code=response.status_code,
            )

    def unfollow(self, user_id: Text) -> Dict:
        """
        Unfollow instagram user
        --------------------

        user_id: Text = Instagram user id
        rtype: json data type
        """
        response = self.session.post(action.unfollow_url(user_id), data={})
        if response.status_code == Instagram.HTTP_OK:
            return response.json()
        else:
            return dict(
                success=False,
                status="ok",
                message="uknown error",
                status_code=response.status_code,
            )

    def like(self, post_id: Text) -> Dict:
        """
        Like post simplecity
        --------------------

        post_id: Text = Instagram post id
        rtype: json data type
        """
        response = self.session.post(
            action.like_url(media_id=post_id), data={})
        if response.status_code == Instagram.HTTP_OK:
            return response.json()
        else:
            return dict(
                success=False,
                status="ok",
                message="uknown error",
                status_code=response.status_code,
            )

    def unlike(self, post_id: Text):
        """
        Unlike post simplecity
        --------------------

        post_id: Text = Instagram post id
        rtype: json data type
        """
        response = self.session.post(
            action.unlike_url(media_id=post_id), data={})
        if response.status_code == Instagram.HTTP_OK:
            return response.json()
        else:
            return dict(
                success=False,
                status="ok",
                message="uknown error",
                status_code=response.status_code,
            )

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
        response = self.session.get(
            self.__models.generate_url_get_followings(
                user_id=user_id, count=str(count_per_page), end_cursor=end_cursor
            )
        )
        if response.status_code == Instagram.HTTP_OK:
            return response.json()
        else:
            return dict(
                success=False,
                status="ok",
                message="uknown error",
                status_code=response.status_code,
            )

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
        response = self.session.get(
            self.__models.generate_url_get_followers(
                user_id=user_id, count=str(count_per_page), end_cursor=end_cursor
            )
        )
        if response.status_code == Instagram.HTTP_OK:
            return response.json()
        else:
            return dict(
                success=False,
                status="ok",
                message="uknown error",
                status_code=response.status_code,
            )

    def get_post_user(
        self, user_id: Text, count_post: int = 12, end_cursor=None
    ) -> Dict:
        """
        Get user post instagram
        -----------------------

        user_id: Text = Instagram user id
        count_post: int = How many post in per page. default 12
        end_cursor: None = If have more page
        return json type
        """
        response = self.session.get(
            self.__models.generate_url_get_post(
                user_id=user_id, count_post=str(count_post), end_cursor=end_cursor
            )
        )
        if response.status_code == Instagram.HTTP_OK:
            return response.json()
        else:
            return dict(
                success=False,
                status="ok",
                message="uknown error",
                status_code=response.status_code,
            )

    def get_user_info(self, username: Text) -> Dict:
        """
        Get details information instagram user.
        ---------------------------------------

        username: Text = "Instagram username"
        rtype: Dict
        """
        response = self.session.get(endpoints.ACCOUNT_JSON_INFO % username)
        if response.status_code == Instagram.HTTP_OK:
            return response.json()
        else:
            return dict(
                success=False,
                status="ok",
                message="uknown error",
                status_code=response.status_code,
            )

    def get_post_info(self, media_id: Text) -> Dict:
        """
        Get details information media post.
        -----------------------------------

        media_id: Text = "Instagram media post id"
        rtype: Dict
        """
        response = self.session.get(endpoints.MEDIA_JSON_INFO % media_id)
        if response.status_code == Instagram.HTTP_OK:
            return response.json()
        else:
            return dict(
                success=False,
                status="ok",
                message="uknown error",
                status_code=response.status_code,
            )
