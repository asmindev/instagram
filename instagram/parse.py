from typing import Dict, Text, Any


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


def stories_details(content: Dict, story_id: Text | Any = None):
    response: Dict = content["data"]
    if response["reels_media"]:
        data = response["reels_media"][0]["items"]
        if story_id:
            data = list(filter(lambda x: x["id"] == story_id, data))
            response["reels_media"] = data
        return response
    else:
        return response


def reels_details(content: Dict, less=True):
    items = content.get("items")
    if items:
        media = items[0]
        if less:
            user: Text = media["user"]
            caption = media["caption"]
            video_duration: Text = media["video_duration"]
            video_url: Text = media["video_versions"]
            audio: Dict = media["clips_metadata"]
            if audio["music_info"]:
                audio["music_info"]["music_asset_info"].pop("dash_manifest")
            if audio["original_sound_info"]:
                audio["original_sound_info"].pop("dash_manifest")
            return dict(
                video_duration=video_duration,
                user=user,
                caption=caption,
                video_url=video_url,
                audio=audio,
            )
        else:
            return media
    else:
        return content
