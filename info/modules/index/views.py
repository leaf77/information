from flask import current_app
from flask import render_template
from flask import session

from info.models import User, News
from . import index_blu

@index_blu.route('/')
def index():
    """
    显示首页
    1. 如果用户已经登录，将当前登录用户的数据传到模板中，供模板显示
    :return:
    """
    #显示用户是否登录的逻辑
    #取到用户id
    user_id = session.get("user_id",None)
    user = None
    if user_id:
        try:
            user = User.query.get(user_id)
        except Exception as e:
            current_app.logger.error(e)

    #右侧的新闻排行的逻辑
    news_list = []
    try:
        news_list = News.query.order_by(News.clicks.desc()).limit(6)
    except Exception as e:
        current_app.logger.error(e)

    # 定义一个空的字典列表，里面装的就是字典
    news_dict_li = []
    # 遍历对象列表，将对象的字典添加到字典列表中
    for news in news_list:
        news_dict_li.append(news.to_basic_dict())

    data = {
        "user": user.to_dict() if user else None,
        "news_dict_li":news_dict_li
    }

    return render_template('news/index.html', data=data)

#在打开网页的时候，浏览器会默认去请求根路径+favicon.ico作网站标签的小图标
#send_static_file 是flask去查找指定的静态文件所调用的方法
@index_blu.route('/favicon.ico')
def favicon():
    return current_app.send_static_file('news/favicon.ico')