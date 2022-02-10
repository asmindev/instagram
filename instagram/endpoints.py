from dataclasses import dataclass
from typing import Text
import re


@dataclass
class Instagram:
    USER_AGENT: Text = "Mozilla/5.0 (Linux; Android 9; SM-A102U Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 Instagram 155.0.0.37.107 Android (28/9; 320dpi; 720x1468; samsung; SM-A102U; a10e; exynos7885; en_US; 239490550)"
    BASE_URL: Text = "https://instagram.com"
    LOGIN_URL: Text = BASE_URL + "/accounts/login/ajax/"
    MID: Text = BASE_URL + "/web/__mid/"

    def __init__(self) -> None:
        pass

    def csrftoken(self, response: Text):
        return re.findall('"csrf_token":"(.*?)",', response)[0]
