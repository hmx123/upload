from flask import Flask
from app.config import config
from app.extensions import config_extensions
from app.views import register_blueprint


# 工厂函数创建应用实例
def create_app(config_name):
    # 创建应用实例
    app = Flask(__name__)
    # 初始化配置
    if config_name not in config:
        config_name = 'default'
    app.config.from_object(config[config_name])
    # 配置扩展
    config_extensions(app)
    # 注册蓝本
    register_blueprint(app)
    # 返回应用实例
    return app
