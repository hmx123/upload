import requests
url = 'http://192.168.2.5:5000/user/upload/'
for x in range(1000, 2000):
    data = {
        'user_id': x,
        'icon_type': 1
    }
    files = {'photo': open(r'C:\Users\Administrator\PycharmProjects\p_server\test/jj.jpg', 'rb')}
    print(x)
    response = requests.post(url, data=data, files=files)


