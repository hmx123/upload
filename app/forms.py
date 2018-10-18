#-*- coding:utf-8 –*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired

# 管理员登录表单
class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(message='用户名不能为空')])
    password = PasswordField('密码', validators=[DataRequired(message='密码不能为空')])
    submit = SubmitField('立即登录')

# 推送内容表单
class JgPush(FlaskForm):
    content = TextAreaField('通知内容', validators=[DataRequired(message='用户名不能为空')])
    platform = SelectField('推送平台', choices=[('all', 'all'), ('ios开发', 'ios开发'), ('ios生产', 'ios生产'), ('android', 'android')], validators=[DataRequired(message='用户名不能为空')])
    submit = SubmitField('立即发送')

