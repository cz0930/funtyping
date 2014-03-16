#-*- coding:utf-8 -*-

from flask import Flask 
from funtyping.utils.util import get_user_id

app = Flask("funtyping")
app.config.from_pyfile('app_config.cfg')

app.jinja_env.globals.update(static='/static')
app.jinja_env.globals.update(get_user_id=get_user_id)

from funtyping.views.regist import regist


