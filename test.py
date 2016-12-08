import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth


# params ={"firstname":'Ryan','lastname':'Mitchell'}
# r=requests.post('http://pythonscraping.com/files/processing.php',data=params)
# print(r.text)


# params={'email_addr':'ryan.e.mitchell@gmail.com'}
# r=requests.post('http://post.oreilly.com/client/o/oreilly/forms/quicksignup.cgi',data=params)
# print(r.text)

###简单模拟登陆

##简单处理cookies
# params={'username':"Ryan",'password':'password'}
# r=requests.post('http://pythonscraping.com/pages/cookies/welcome.php',data=params)
# print('cookie is set to ')
# print(r.cookies.get_dict())
# print('---------------')
# print('going to profile page...')
# r=requests.get('http://pythonscraping.com/pages/cookies/profile.php',cookies=r.cookies)
# print(r.text)

### 利用Session处理变化的cookies
# session=requests.Session();
# params={'username':"Ryan",'password':'password'}
# s=session.post('http://pythonscraping.com/pages/cookies/welcome.php',data=params)
# #r=requests.post('http://pythonscraping.com/pages/cookies/welcome.php',data=params)
# print('cookie is set to ')
# print(r.cookies.get_dict())
# print('---------------')
# print('going to profile page...')
# #r=requests.get('http://pythonscraping.com/pages/cookies/profile.php',cookies=r.cookies)
# s=session.get('http://pythonscraping.com/pages/cookies/profile.php')
# print(r.text)

###处理HTTP认证
auth=HTTPBasicAuth('ryan','password')
r=requests.post('http://pythonscraping.com/pages/auth/login.php',auth=auth)
print(r.text)
