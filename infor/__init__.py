from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import CSRFProtect
from redis import StrictRedis
from sqlalchemy.orm import Session

from config import Config

app = Flask(__name__)
"""加载配置 """
app.config.from_object(Config)

#初始化数据库
db=SQLAlchemy(app)
#初始化redis存储对象
redis_store=StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT)
#开启当前项目CSRF保护,只做服务器验证功能
CSRFProtect(app)
#设置session保存指定位置
Session(app)