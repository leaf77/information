#新闻详情模块的蓝图

from flask import Blueprint

#创建蓝图对象
news_blu=Blueprint("news",__name__, url_prefix="/news")

from . import views