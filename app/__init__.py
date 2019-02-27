from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
# create db object
db = SQLAlchemy(app)
migrate = Migrate(db, app)


from app import views 

