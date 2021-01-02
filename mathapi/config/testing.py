from mathapi.config import base


class Config(base.Config):
    DEBUG = True
    API_USER = "test"
    API_PASSWORD = (
        "pbkdf2:sha256:150000$0wnP6KqA$a4d58ab33adbfd2cd596f4b5584ea0f7f5250a2d1718dbd34c44b2006aee3813"  # password
    )
