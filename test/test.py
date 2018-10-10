#
# image_url = r'C:\Users\Administrator\PycharmProjects\p_server\test/1.png'
#
# r = open(image_url, 'rb')
# print(r)
from werkzeug.security import generate_password_hash
print(generate_password_hash('root'))

