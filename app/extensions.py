# 导入类库
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_uploads import UploadSet, IMAGES
from flask_uploads import configure_uploads, patch_request_class
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

# 创建对象
db = SQLAlchemy()
migrate = Migrate(db=db)
photos = UploadSet('photos', IMAGES)
bootstrap = Bootstrap()
login_manager = LoginManager()

# 初始化
def config_extensions(app):
    db.init_app(app)
    migrate.init_app(app)
    # 上传文件
    configure_uploads(app, photos)
    patch_request_class(app, size=None)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    # 设置登录端点
    login_manager.login_view = 'user.login'
