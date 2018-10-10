import os

base_dir = os.path.dirname(__file__)


# 配置基类
class Config:
    # 秘钥
    SECRET_KEY = '123456'
    # 数据库
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 文件上传
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024
    UPLOADED_PHOTOS_DEST = os.path.join(base_dir, 'static/upload')


# 开发环境配置
class DevelopConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/uploaddev?charset=utf8'


# 测试环境配置
class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/uploadtest?charset=utf8'


# 生产环境配置
class ProductConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/upload?charset=utf8'


# 配置字典
config = {
    'develop': DevelopConfig,
    'testing': TestingConfig,
    'product': ProductConfig,
    # 默认环境
    'default': DevelopConfig
}
