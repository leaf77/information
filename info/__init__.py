import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
#可以用来指定session的保存位置
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import CSRFProtect
from redis import StrictRedis
from sqlalchemy.orm import Session
from config import config
import pymysql
pymysql.install_as_MySQLdb()



# 初始化数据库
# 在flask很多扩展里面都可以先初始化扩展的对象，然后再去调用init_app方法去初始化
db = SQLAlchemy()

redis_store = None #type:StrictRedis
# redis_store:StrictRedis =None

def setup_log(config_name):
    #设置日志的记录等级
    logging.basicConfig(level=config[config_name].LOG_LEVEL)  # 调试debug级
    #创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)
    #创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    #为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    #为全局的日志工具对象（flask app的使用）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)

def create_app(config_name, passport_blu=None):
    #配置日志,并且传入配置名字，以便能获取到指定配置所对应的日志等级
    setup_log(config_name)
    #创建Flask对象
    app = Flask(__name__)
    #加载配置
    app.config.from_object(config[config_name])
    #通过app初始化
    db.init_app(app)
    #初始化redis存储对象
    global redis_store
    redis_store=StrictRedis(host=config[config_name].REDIS_HOST,port=config[config_name].REDIS_PORT)
    #开启当前项目CSRF保护,只做服务器验证功能
    # CSRFProtect(app)
    #设置session保存指定位置
    Session(app)

    #注册蓝图(啥时候注册啥时候导入)
    from info.modules.index import index_blu
    app.register_blueprint(index_blu)

    from info.modules.passport import passport_blu
    app.register_blueprint(passport_blu)

    return app