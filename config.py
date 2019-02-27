
#config.py

import os

class Config(object):
    #setting debugging on
    DEBUG = True
    # connect to database
    SQLALCHEMY_DATABASE_URL = "mysql://root:root/mmu"
    #SQLALCHEMY_MODIFICATIONS_TRACK=False
    SECRET_KEY="thisis-secret-one"





