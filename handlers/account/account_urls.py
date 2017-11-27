#coding=utf-8

from account_auth_handler import LoginHandler, CaptchaHandler,RegisterHandler

accounts_urls = [
    (r'/auth/user_login', LoginHandler),
    (r'/auth/captcha', CaptchaHandler),
    (r'/auth/user_register', RegisterHandler),
]

