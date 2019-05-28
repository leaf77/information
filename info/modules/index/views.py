from info import redis_store
from . import index_blu

@index_blu.route('/')
def index():
    #向redis中保存一个值 name leaf77
    redis_store.set("name","leaf77")
    return 'index'