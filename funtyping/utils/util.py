#-*- coding:utf-8 -*-
from flask import Flask, session, escape
def get_user_id():
    if 'user_id' in session:
        return escape(session['user_id'])
    return 0
