######################################################
#
#Author:          whytin
#Email:           whytin@yeah.net
#QQ:              583501947
#
#Filename:        blog.py
#Last modified:   2016-05-30 21:16
#Description:     
#
######################################################

import sqlite3
from flask import Flask, render_template, request, session, redirect, url_for, flash
from models import *

DEBUG = True
SECRET_KEY = 'complex'

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
	error = None
	if request.method == 'POST':
		passwd = verify([request.form['username']])
		if request.form['password'] != passwd[2]:
			error = 'Error password'
		else:
			session['username']=request.form['username']
			session['logged_in']=True
			flash('You were logged in')
			return redirect(url_for('index'))
	return render_template('login.html',error=error)

@app.route('/logout')
def logout():
	session.pop('username',None)
	session.pop('logged_in',None)
	flash('You were logged out')
	return redirect(url_for('index'))


@app.route('/regest', methods=['GET','POST'])
def regest():
	if request.method == 'POST':
		regestion(request.form['username'],request.form['password'],request.form['mail'])
		flash('Successfully regestion')
		return redirect(url_for('index'))
	return render_template('regest.html')


if __name__ == '__main__':
	app.run()

