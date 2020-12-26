from mathapi.config import base


class Config(base.Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{base.Config.BASE_DIR}/mathapi.db"
