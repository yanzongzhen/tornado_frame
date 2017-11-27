#coding=utf-8
from tornado.web import StaticFileHandler
from main_handler import MainHandler
from handlers.account.account_urls import accounts_urls

handlers = [
    (r'/', MainHandler),
]

handlers += accounts_urls

