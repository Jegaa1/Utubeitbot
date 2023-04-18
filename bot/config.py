import os


class Config:

    BOT_TOKEN = "6240552623:AAG8Jj0rOytCH5B0BUeSWArALHECas_HGdU"

    SESSION_NAME = ":memory:"

    API_ID = 1923471

    API_HASH = "fcdc178451cd234e63faefd38895c991"

    CLIENT_ID = "120733850121-1p8qhnr7rd6fa5q0ogi4gp3ob0o25o7k.apps.googleusercontent.com"

    CLIENT_SECRET = "XXCO5muxHs_vvo7cRpwoyEf9"

    BOT_OWNER = 880087645

    AUTH_USERS_TEXT = os.environ.get("AUTH_USERS", "")

    AUTH_USERS = [BOT_OWNER, 754495556] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE", "public") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
