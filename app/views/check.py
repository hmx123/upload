#-*- coding:utf-8 –*-
from flask import Blueprint, request, render_template, url_for
from app.models import Icon
from app.extensions import db, photos
from math import ceil
from app.views.wyyapi import wyy_updata_user
from flask_login import login_required

check = Blueprint('check', __name__)

@check.route('/')
@check.route('/<int:page>')
@login_required
def check_photo(page=1):
    per_page = 20
    start = (page - 1) * per_page
    end = start + per_page
    icons = Icon.query.filter_by(confirmed=1).all()[start:end]
    total = Icon.query.count()
    pages = ceil(total / per_page)
    img_url = url_for('static', filename='upload/')
    return render_template('common/icon.html', icons=icons, img_url=img_url, pages=range(1, pages))

@check.route('/updata/', methods=['POST'])
def updata_photo():
    formData = request.form
    formData = str(formData)
    formData = reques_data(formData)
    icons = Icon.query.filter(Icon.user_id.in_(tuple([x['user'] for x in formData]))).all()
    for x in range(len(icons)):
        icons[x].confirmed = formData[x]['test']
    db.session.add_all(icons)
    db.session.commit()
    users = Icon.query.filter_by(confirmed=2).all()
    # �����ͷ���ϴ��������� def wyy_updata_user(accid, icon, token):
    for user in users:
        img_url = photos.url(user.icon)
        img_url = img_url.replace('_uploads', 'static')
        img_url = img_url.replace('photos', 'upload')
        print(img_url)
        print(wyy_updata_user(user.user_id, img_url))
    return 'ok'

# ���ݴ���
def reques_data(string):
    string = string.strip('ImmutableMultiDict(')
    string = eval(string.strip(')'))
    length = len(string)
    cont = int(length / 2)
    list_users = string[0:cont]
    list_checks = string[cont: length]
    lis = []
    for list_user in list_users:
        checks = {}
        checks[list_user[0]] = list_user[1]
        lis.append(checks)
    for x in range(len(lis)):
        lis[x][list_checks[x][0]] = list_checks[x][1]
    return lis
