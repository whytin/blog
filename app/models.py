######################################################
#
#Author:          whytin
#Email:           whytin@yeah.net
#QQ:              583501947
#
#Filename:        models.py
#Last modified:   2016-05-30 21:19
#Description:     
#
######################################################

import sqlite3

db = '../tmp/blog.db'

def connect_db():
	return sqlite3.connect(db)

#class User(object):
#	def __init__(self,id,name,password,mail):
#		self.id = id
#		self.name = name
#		self.password = password
#		self.mail = mail
	
def regestion(name,password,mail):
	sql = 'insert into users (name,password,mail) VALUES (?,?,?)'
	conn = connect_db()
	cursor = conn.cursor()
	cursor.execute(sql,(name,password,mail))
	conn.commit()
	cursor.close()
	conn.close()

def verify(name):
	sql = 'select * from users where name=?'
	conn = connect_db()
	cursor = conn.cursor()
	rv = cursor.execute(sql,name)
	passwd = rv.fetchall()
	conn.commit()
	cursor.close()
	conn.close()
	return passwd[0]

