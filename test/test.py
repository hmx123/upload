#-*- coding:utf-8 –*-
# _*_ coding:utf-8 _*_
# image_url = r'C:\Users\Administrator\PycharmProjects\p_server\test/1.png'
#
# r = open(image_url, 'rb')
# print(r)

# from werkzeug.security import generate_password_hash
# print(generate_password_hash('root'))

# 消息推送
from app.views.wyyapi import pushmessage
if __name__ == '__main__':
    pushmessage('this is test', 'root')


