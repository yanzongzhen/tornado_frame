#coding=utf-8
from datetime import datetime
from utils.captcha.captcha import create_captcha
from models.account.account_user_model import User

def create_captcha_img(self, pre_code, code):
    """生成验证码，保存到redis"""
    if pre_code:
        self.conn.delete("captcha:%s" %pre_code)
    text, img = create_captcha()
    self.conn.setex("captcha:%s" % code, text.lower(), 60)
    return img


def auth_captche(self, captche_code, code):
    """校验验证码"""
    print captche_code, code
    if captche_code == '':
        return {'status': False, 'msg': '请输入图形验证码'}
    elif self.conn.get("captcha:%s" % code) != captche_code.lower():
        return {'status': False, 'msg': '输入的图形验证码不正确'}
    return {'status': True, 'msg': '正确'}


def login(self, name, password):
    """登录函数"""
    print name, password
    if name == '' and password == '':
        return {'status': False, 'msg': '请输入用户名或密码'}
    user= User.by_name(name)#注意
    if user and user.auth_password(password):#注意
        user.last_login = datetime.now()
        user.loginnum += 1
        self.db.add(user)
        self.db.commit()
        self.session.set('user_name', user.username)
        return {'status': True, 'msg': '登录成功'}
    return {'status': False, 'msg': '用户名输入错误或者密码不正确'}








