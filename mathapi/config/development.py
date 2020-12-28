import os

from mathapi.config import base


class Config(base.Config):
    DEBUG = False

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return os.getenv("DATABASE_URI", "postgresql://postgres@localhost/mathapi")
