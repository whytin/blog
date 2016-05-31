/*######################################################
#
#Author:          whytin
#Email:           whytin@yeah.net
#QQ:              583501947
#
#Filename:        schema.sql
#Last modified:   2016-05-30 21:12
#Description:     
#
######################################################*/

create table users(
	id integer primary key autoincrement,
	name char not null,
	password char not null,
	mail char 
);

