import os

from mathapi.config import base


class Config(base.Config):
    @property
    def DATABASE_URI(self):
        return os.getenv("DATABASE_URI", "postgresql://postgres@mathapi-postgresql/mathapi-staging")
