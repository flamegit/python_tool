#!/usr/local/bin/python3
# encoding: utf-8
'''
模拟Github登陆步骤：
    1、请求头:self.headers,请求url
    2、设置session,保存登陆信息cookies,生成github_cookie文件
    3、POST表单提交,请求数据格式post_data
    4、authenticity_token获取
    5、在个人中心验证判断是否登陆成功,输出个人中心信息即登陆成功

'''

import requests
from lxml import etree
try:
    import cookielib
except:
    import http.cookiejar as cookielib

class GithubLogin():

    def __init__(self):
        # url
        self.loginUrl = 'https://fabric.io/login'
        self.postUrl = 'https://fabric.io/api/v2/session'
        self.profileUrl = 'https://github.com/settings/profile'

        # 设置请求头
        self.headers = {
            'origin':'https://fabric.io',
            'Referer': 'https://fabric.io/login',
            #'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
            'Host':'fabric.io',
            'X-Requested-With':'XMLHttpRequest',
            'X-CRASHLYTICS-DEVELOPER-TOKEN':'0bb5ea45eb53fa71fa5758290be5a7d5bb867e77',
            'X-CSRF-Token':'HAuKxa8WtLIH1QTc+4MCvt4dZFS3E22czP11pVcbpWA='
        }

        # 设置session
        self.session = requests.session()
        # 生成github_cookie文件
        self.session.cookies = cookielib.LWPCookieJar(filename='fabric_cookie')

    '''
        登陆时表单提交参数
        Form Data:
            commit:Sign in
            utf8:✓
            authenticity_token:yyZprIm4aghZ0u7r25ymZjisfTjGdUAdDowD9fKHM0oUvHD1WjUHbn2sW0Cz1VglZWdGno543jod2M8+jwLv6w==
            login:*****
            password:******
    
    '''
    def post_account(self, email, password):
        post_data = {
            'email': email,
            'password': password
        }
        headers = {
            'origin':'https://fabric.io',
            'Referer': 'https://fabric.io/login',
            #'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
            'Host':'fabric.io',
            'X-Requested-With':'XMLHttpRequest',
            'X-CRASHLYTICS-DEVELOPER-TOKEN':'0bb5ea45eb53fa71fa5758290be5a7d5bb867e77',
            'X-CSRF-Token': self.get_token()[0]
        }

        response = self.session.post(self.postUrl, data=post_data, headers=headers)
        print(response.status_code)
        # 保存cookies
        self.session.cookies.save()
        #print(self.session.cookies)

    def load_cookie(self):
        try:
            self.session.cookies.load(ignore_discard=True)
            print(self.session.cookies)
        except:
            print('cookie 获取不成功')

    # 获取authenticity_token
    def get_token(self):
        headers = {
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
            'Host':'fabric.io'
        }
        response = self.session.get(self.loginUrl, headers=headers)
        html = etree.HTML(response.text)
        authenticity_token = html.xpath('//meta[@name="csrf-token"]/@content')
        print(authenticity_token)
        return authenticity_token

    # 判断是否登陆成功
    def isLogin(self):
        self.load_cookie()
        headers = {
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
            'Host':'fabric.io'
        }
        url ='https://fabric.io/66b8b3/android/apps/com.alo7.android.student/issues?time=1554076800000:1554163199999&event_type=all&subFilter=state&state=all&build[0]=top-builds'
        response = self.session.get(url, headers=headers)

        html = etree.HTML(response.text)
        #print(response.text)
        value = html.xpath('//div[@class="flex-box flex-4"]')
        print(response.status_code)
        print(value)
       

if __name__ == "__main__":
    github = GithubLogin()
   
    # 输入自己email账号和密码
    #github.post_account(email='frank.dong@alo7.com', password='zqbx2oo8!')
    github.isLogin()
    # 验证是否登陆成功
    