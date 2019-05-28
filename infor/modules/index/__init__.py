from flask import Blueprint

#创建蓝图对象
index_blu=Blueprint("index",__name__)

from . import views