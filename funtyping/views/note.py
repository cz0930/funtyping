#-*- coding:utf-8 -*-
from funtyping import app
from flask import render_template,request,flash,redirect,url_for,session,escape,jsonify
from funtyping.models.user_models import *
import datetime
from funtyping.utils.util import get_user_id
from random import randint

@app.route('/latest')
def latest():
    if get_user_id():
        user_id = get_user_id()
        note = Note.query.filter_by(user_id=user_id).order_by('-id').first()
        if not note:
            return redirect(url_for('no_notes'))
        note.weekday = note.time.strftime('%A')
        note.time = note.time.date()
    else:
        return redirect(url_for('login'))
    return render_template('note.html', note=note)
@app.route('/nonotes')
def no_notes():
    return render_template('no_notes.html')

@app.route('/write',methods=['GET','POST'])
def write():
    if request.method == 'GET':
        return render_template('write.html')
    elif request.method == 'POST':
        note_date = request.form["note_date"]
        note_content = request.form["note_content"]
        note_date = datetime.datetime.strptime(note_date, '%Y-%m-%d')
        if get_user_id():
            user_id = get_user_id()
            write_note(user_id,note_date,note_content)
        else:
            return redirect(url_for('login'))
    return redirect(url_for('notes'))

@app.route('/notes/<datenum>')
@app.route('/notes/')
def notes(datenum=None):
    if get_user_id():
        user_id = get_user_id()
        notes = Note.query.filter_by(user_id=user_id).order_by('-id').all()
        date_list=[]
        if not notes:
            return redirect(url_for('no_notes'))
        elif datenum:
            for nn in notes:
                note = nn.time.date()
                if note.strftime('%Y%m')==datenum:
                    date_list = list(set(date_list))
                else:
                    pass
        else:
            for nn in notes:
                note = nn.time.date()
                date_list.append(note.strftime('%Y%m'))
            date_list = list(set(date_list))
    else:
        return redirect(url_for('login'))
    for nn in notes:
        nn.weekday = nn.time.strftime('%A')
        nn.time = nn.time.strftime('%Y-%m-%d')
    return render_template('note_list.html', notes=notes , date_list=date_list )

@app.route('/get_newer_note', methods=['GET'])
def get_newer_note():
    if get_user_id():
        note_id = int(request.args.get('note_id'))
        user_id = get_user_id()
        note = Note.query.filter(Note.user_id == user_id, Note.id<note_id).order_by('id').first()
        if not note:
            note = Note.query.filter_by(user_id=user_id).order_by('-id').first()
        note_id = note.id
        note_content = note.content            
        note_weekday = note.time.strftime('%A')
        note_time = note.time.strftime('%Y-%m-%d')
    return jsonify(id = note_id,weekday = note_weekday,time = note_time,content = note_content)

@app.route('/get_older_note', methods=['GET'])
def get_older_note():
    if get_user_id():
        note_id = int(request.args.get('note_id'))
        user_id = get_user_id()
        note = Note.query.filter(Note.user_id == user_id, Note.id>note_id).order_by('id').first()
        if not note:
            note = Note.query.filter_by(user_id=user_id).order_by('id').first()
        note_id = note.id
        note_content = note.content
        note_weekday = note.time.strftime('%A')
        note_time = note.time.strftime('%Y-%m-%d')
    return jsonify(id = note_id,weekday = note_weekday,time = note_time,content = note_content)

@app.route('/get_random_note', methods=['GET'])
def get_random_note():
    if get_user_id():
        note_id = int(request.args.get('note_id'))
        user_id = get_user_id()
        note_list = Note.query.filter_by(user_id=user_id).all()
        note = note_list[randint(0, len(note_list)-1)]
        note_id = note.id
        note_content = note.content
        note_weekday = note.time.strftime('%A')
        note_time = note.time.strftime('%Y-%m-%d')
    return jsonify(id = note_id,weekday = note_weekday,time = note_time,content = note_content)
