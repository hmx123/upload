#-*- coding:utf-8 –*-
import hashlib,requests,json,time

AppKey = '0151eb211fb26ebf020684cfd8125624'
AppSecret = '269163c64b9e'

apiurl = {
	'create_user':'https://api.netease.im/nimserver/user/create.action',
	'create_room':'https://api.netease.im/nimserver/chatroom/create.action',
	'create_group': '',
	'updata_user': 'https://api.netease.im/nimserver/user/updateUinfo.action'
}

# 更新用户头像 accid, icon,token
def wyy_updata_user(accid, icon):
	body = ('accid=%s&icon=%s' % (accid, icon)).encode("utf-8")
	nonce = '575728120'  # 随机数（最大长度128个字符）
	curTime = str(int(time.time()))
	checkSum = AppSecret + nonce + curTime
	checkSum = hashlib.sha1(checkSum.encode("utf-8")).hexdigest()
	headers = {'content-type': 'application/x-www-form-urlencoded;charset=utf-8', 'AppKey': AppKey, 'Nonce': nonce,
			   'CurTime': curTime, 'CheckSum': checkSum}
	response = requests.post(apiurl['updata_user'], data=body, headers=headers)
	if response.status_code == 200:
		print(response.text)
		try:
			jsonData = json.loads(response.text)
			if jsonData['code'] == 200:
				return jsonData['code']
		except ValueError:
			jsonData = None
	return None