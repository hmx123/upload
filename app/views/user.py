import os
from flask import Blueprint, current_app, request, render_template, redirect, url_for
from app.models import Icon, Admin
from app.extensions import db, photos
import json
from app.forms import LoginForm
from flask_login import login_user, login_required

user = Blueprint('user', __name__)


# 生成指定长度的随机字符串
def random_string(length=32):
    import random
    base_str = 'abcdefghijklmnopqrstuvwxyz1234567890'
    return ''.join(random.choice(base_str) for i in range(length))


@user.route('/')
def index():
    return 'full upload'
    # return random_string()


@user.route('/upload/', methods=['POST'])
def upload():
    photo = request.files.get('photo')
    user_id = request.form.get('user_id')
    icon_type = int(request.form.get('icon_type'))
    token = request.form.get('token')
    # 提取文件后缀
    suffix = os.path.splitext(photo.filename)[1]
    # 生成随机文件名
    filename = random_string() + suffix
    photos.save(photo, name=filename)
    img_url = photos.url(filename)
    img_url = img_url.replace('_uploads', 'static')
    img_url = img_url.replace('photos', 'upload')
    # 判断数据库是否有该用户
    user = Icon.query.filter_by(user_id=user_id).first()
    if user:
        # 删除原来的头像
        os.remove(os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'], user.icon))
        user.icon = filename
        user.confirmed = 1
    else:
        u = Icon(user_id=user_id, icon_type=icon_type, icon=filename, token=token)
        db.session.add(u)
    data = {"url": img_url}
    data = json.dumps(data)
    return data


# 管理员登录
@user.route('/login/', methods=['GET', 'POST'])
def login():
    try:
        form = LoginForm()
        if form.validate_on_submit():
            u = Admin.query.filter(Admin.name == form.username.data).first()
            if u and u.verify_password(form.password.data):
                login_user(u, remember=False)
                return redirect(request.args.get('next') or url_for('check.check_photo'))
        return render_template('user/login.html', form=form)
    except Exception as e:
        print(e)
        return ''
