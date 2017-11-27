#coding=utf-8
import tornado.httpserver
import tornado.web
import tornado.ioloop
import tornado.escape
from tornado.options import define, options
from config import settings
from handlers.main.main_urls import handlers
from models.account.account_user_model import User
from libs.db import create_talbes
from libs.db.dbsession import dbSession
#定义一个默认的端口
define("port", default=8000, help="run port ", type=int)
define("start", default=False, help="start server", type=bool)
define("t", default=False, help="create table", type=bool)
define("u", default=False, help="create user", type=bool)


if __name__ == "__main__":
    options.parse_command_line()
    if options.t:
        create_talbes.run()
    if options.u:
        user = User()
        user.username = 'zhangsan'
        user.password = '222'
        dbSession.add(user)
        dbSession.commit()


    if options.start:
        app = tornado.web.Application(handlers, **settings) #创建应用实例
        http_server = tornado.httpserver.HTTPServer(app) #通过应用实例创建服务器实例
        http_server.listen(options.port)  #监听9000端口
        print 'start server...'
        tornado.ioloop.IOLoop.instance().start() #启动服务器

