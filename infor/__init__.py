from flask import Flask
#可以用来指定session的保存位置
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import CSRFProtect
from redis import StrictRedis
from sqlalchemy.orm import Session

from config import config

# 初始化数据库
# 在flask很多扩展里面都可以先初始化扩展的对象，然后再去调用init_app方法去初始化
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    #加载配置
    app.config.from_object(config[config_name])
    #通过app初始化
    db.init_app(app)
    #初始化redis存储对象
    redis_store=StrictRedis(host=config[config_name].REDIS_HOST,port=config[config_name].REDIS_PORT)
    #开启当前项目CSRF保护,只做服务器验证功能
    CSRFProtect(app)
    #设置session保存指定位置
    Session(app)

    return app