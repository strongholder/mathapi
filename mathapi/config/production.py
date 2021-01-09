import os

from mathapi.config import base


class Config(base.Config):
    broker_url = "redis://mathapi-redis-master:6379/0"
    result_backend = "redis://mathapi-redis-master:6379/0"

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return os.getenv("DATABASE_URI", "postgresql://postgres@mathapi-postgresql/mathapi-production")
