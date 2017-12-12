import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SECRET_KEY = 'you-will-never-guess'
#SQLALCHEMY_DATABASE_URI = 'sqlite:///Student.sqlite3'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
