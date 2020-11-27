import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \ 
        'sqlite:///' + os.path.join(basedir, 'app.db') #location of the applications's database - if the database isn't defined it will configure a database named app.db located in the main directory of the application.
    SQLALCHEMY_TRACK_MODIFICATIONS = False