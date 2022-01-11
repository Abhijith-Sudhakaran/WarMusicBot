import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQB9wlzQPgQ6OFXeEJG9eNm08catd5bjcfBu0ep-Goe8y4L6WXwwO5U1rT2BBsAn1nRfaCzB0hMf0G9uhTLoHnfEqqYWk5wgrN6nj0CdPQ0BQcG7dXzN3ojRUZbM6xXj-xF-5EOrKCks0h_4_0Fs4rv13awBk-fRkjKqe-ISFESbQT4WkvWEPnnwVCkbo24lbT8PrW6_4drB1vATrFZBYYk0caPEJ3J9uXdoHfG5ViE7RulV23HR9gkqb0MzcNcqj4dYUdsCGfVuOrD7QI5aueao4zJw1KECgjv4nIfKo3_6Fzl7qsz9TliRoy2a4ITEaMCtW0KhEHWtBr2D8GJDgjErX51r6AA")
BOT_TOKEN = getenv("BOT_TOKEN", "1959668222:AAGFuP9yC4oejEm-osDq_YkAYVhs4bzbin4")
BOT_NAME = getenv("BOT_NAME", "🦋🎶 Aαмι 🎶🦋")
API_ID = int(getenv("API_ID","2599004"))
API_HASH = getenv("API_HASH","d556b9298469c3b68a2330ebe47f9587")
OWNER_NAME = getenv("OWNER_NAME", "Telecat_X")
ALIVE_NAME = getenv("ALIVE_NAME", "🦋♪⋆ Äαʍί ⋆♪ 🦋")
BOT_USERNAME = getenv("BOT_USERNAME", "Aami_song_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "CatKing_ext")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "GEETHUBOTCHATZ")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "GEETHUBOTUPDATES")
SUDO_USERS = list(map(int, getenv("SUDO_USERS","1981831553").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/8bad7843782ee1a1cc4f0.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "540000"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/xAbhish3k/video-stream")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/cd573e828a010ef46534c.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/a91c17a11f1e3a9cf4a3e.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/e2250edc9ec36f489db02.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/554b047bd413dcd518cdf.png")
