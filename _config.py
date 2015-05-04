"""
basedir returns a normalized absolutized
version of the pathname of the directory

DATABASE_PATH defines the full path for
the database by joining basedir and DATABASE

WTF_CSFR_ENABLED = TRUE prevents cross-site request forgery,
makes app more secure (uses Flask-WTF extension.)

Re: Secret key, use of random key generator for security.
"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))

# configurations
DATABASE = 'flasktaskr.db'
WTF_CSFR_ENABLED = True
SECRET_KEY = 'my_precious'

DATABASE_PATH = os.path.join(basedir, DATABASE)

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
