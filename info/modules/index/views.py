from flask import current_app
from flask import render_template
from flask import session

from info.models import User
from . import index_blu

@index_blu.route('/')
def index():
    """
    显示首页
    1. 如果用户已经登录，将当前登录用户的数据传到模板中，供模板显示
    :return:
    """
    user_id = session.get("user_id",None)
    user = None
    if user_id:
        try:
            user = User.query.get(user_id)
        except Exception as e:
            current_app.logger.error(e)

    data = {
        "user": user.to_dict() if user else None
    }

    return render_template('news/index.html', data=data)

#在打开网页的时候，浏览器会默认去请求根路径+favicon.ico作网站标签的小图标
#send_static_file 是flask去查找指定的静态文件所调用的方法
@index_blu.route('/favicon.ico')
def favicon():
    return current_app.send_static_file('news/favicon.ico')