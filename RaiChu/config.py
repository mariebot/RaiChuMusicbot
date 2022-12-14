## Coder are here

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQAkBmYpH0msRqUkSzN-rZBZfBaaoRxV8BJn5FOVygXlYBEzks8sJa89VtWcODf7jd487C52YPOGGeKWt8IE9QXedn4zx6umW9Ag4Hg7O3bgqmYPngPfMakP6l_5B99ouLxR_9kL5841IdFHgNKL3X1g5mjMAJO8quwPQSNLCNqn344OPAozQCrDO18Dm8Dpkldnmtt3RMU2Y8i3NmDH-44unB69ZOFlWn4gvoOU5h1jfDREw2YgKnqP8XGNfzQLxHDM7txnmCyfK6ElDf7wa8BDByduEDLzNfMU2Jm_lIVhaFv6CUthixMdex6l2p9Z3kl1qE3mCTTZ42-bPi0L3ZPsAAAAATDvfKMA")
BOT_TOKEN = getenv("BOT_TOKEN", "5545963604:AAFyeZDxieUOq1mmz6khwuSzTvvf8JiBJcU")
BOT_NAME = getenv("BOT_NAME", "Elisa")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "denvil")
ALIVE_NAME = getenv("ALIVE_NAME", "Null")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "elisaplay")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "null")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "elisha_support")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "denvil_bots")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5497627952").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/AMANTYA1/RaiChu-MusicV2")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://telegra.ph/file/58da23d726b601dc3b18e.jpg")
