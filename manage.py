from flask import session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from infor import create_app,db

#通过指定的配置名字创建对应配置的app
#create_app 就类似于工厂方法
app=create_app('development')

manager = Manager(app)
#将app于db关联
Migrate(app,db)
#将迁移命令添加到manager中
manager.add_command("db",MigrateCommand)


@app.route('/')
def index():
    session["name"]='leaf77'
    return 'index777777'


if __name__ == '__main__':
    manager.run()

