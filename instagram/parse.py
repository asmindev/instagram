from typing import Dict, List, Text


def uknown(status_code, **kwargs):
    return dict(
        kwargs,
        success=False,
        status="ok",
        message="uknown error",
        status_code=status_code,
    )


def details_user(content: Dict, less: bool = True) -> Dict:
    user = content["graphql"]["user"]
    if less:
        id = user["id"]
        username: Text = user["username"]
        fullname: Text = user["full_name"]
        is_private = user["is_private"]
        is_verified = user["is_verified"]
        profile_pic_url_hd = user["profile_pic_url_hd"]
        biography: Text = user["biography"]
        edge_follow: Dict = user["edge_follow"]
        edge_followed_by: Dict = user["edge_followed_by"]
        return dict(
            id=id,
            username=username,
            fullname=fullname,
            is_private=is_private,
            is_verified=is_verified,
            profile_pic_url_hd=profile_pic_url_hd,
            biography=biography,
            edge_follow=edge_follow,
            edge_followed_by=edge_followed_by,
        )
    else:
        return user


def stories_details(content: Dict, story_id: Text = None):
    response: Dict = content["data"]
    if response["reels_media"]:
        data = response["reels_media"][0]["items"]
        if story_id:
            data = list(filter(lambda x: x["id"] == story_id, data))
            response["reels_media"] = data
        return response
    else:
        return response
