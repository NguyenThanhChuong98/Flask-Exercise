import os
<<<<<<< HEAD
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	SECRET_KEY=os.environ.get('SECRET_KEY') or 'you-will-never-guess'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
	'sqlite:///' + os.path.join(basedir,'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
=======

class Config(object):
	SECRET_KEY=os.environ.get('SECRET_KEY') or 'you-will-never-guess'
>>>>>>> 2115c72aa3474663f510c419a9f003b792a8c66f
