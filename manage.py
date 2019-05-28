from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

class Config(object):

    """项目的配置信息"""
    DEBUG = True
    """为数据库添加配置"""
    SQLALCHEMY_DATABASE_URL="mysql://root:mysql@127.0.0.1:3306/information27"
    SQLALCHEMY_TRACK_MODIFICATIONS=False

"""加载配置 """
app.config.from_object(Config)

db=SQLAlchemy(app)

@app.route('/')
def index():
    return 'Hello world'


if __name__ == '__main__':
    app.run(debug=True,port=9999)

