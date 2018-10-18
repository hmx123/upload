from .check import check
from .jgpush import jg
from .user import user



# 蓝本配置
DEFAULT_BLUEPRINT = (
    (user, '/user'),
    (check, '/check'),
    (jg, '/jg')
)


# 封装函数，注册蓝本
def register_blueprint(app):
    for blueprint, url_prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=url_prefix)
