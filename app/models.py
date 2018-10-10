from flask_login import UserMixin

from app.extensions import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash


# 用户头像模型
class Icon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id =  db.Column(db.String(15))
    icon = db.Column(db.String(64))
    token = db.Column(db.String(128))
    # 头像类型
    icon_type = db.Column(db.Integer, default=1)
    # 审核状态 1审核中   2审核失败  3审核成功
    confirmed = db.Column(db.Integer, default=1)

# 管理员
class Admin(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('error')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # 密码校验
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

# 设置回调
@login_manager.user_loader
def load_user(uid):
    return Admin.query.get(uid)
