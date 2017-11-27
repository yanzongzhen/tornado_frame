#coding=utf-8
from handlers.base.base_handler import BaseHandler
from libs.account.account_auth_libs import create_captcha_img,auth_captche,login


class CaptchaHandler(BaseHandler):
    """生成验证码"""
    def get(self):
        pre_code = self.get_argument('pre_code', '')
        code = self.get_argument('code', '')
        img = create_captcha_img(self, pre_code, code)
        self.set_header("Content-Type", "image/jpg")
        self.write(img)

class LoginHandler(BaseHandler):
    """登录函数"""
    def get(self):
        self.render("account/auth_login.html")

    def post(self):
        name = self.get_argument('name', '')
        password = self.get_argument('password', '')
        code = self.get_argument('code', '')
        captcha_code = self.get_argument('captcha', '')

        result = auth_captche(self, captcha_code, code)
        #{'status': False, 'msg': '请输入图形验证码'}
        if result['status'] is False:
            return self.write({'status': 400, 'msg': result['msg']})
        result = login(self, name, password)
        if result['status'] is True:
            return self.write({'status': 200, 'msg': result['msg']})
        return self.write({'status': 400, 'msg': result['msg']})


class RegisterHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('account/auth_register.html')