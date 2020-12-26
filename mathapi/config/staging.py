import os

from mathapi.config import base


class Config(base.Config):
    @property
    def DATABASE_URI(self):
        return os.getenv("DATABASE_URI", f"sqlite:///{base.Config.BASE_DIR}/mathapi.db")
