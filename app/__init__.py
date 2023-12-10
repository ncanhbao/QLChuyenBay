from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = 'DAFDJFSKDFNSKDF*&^yFDSNFBDSBFDSBFSFJDSNFJIDFJS'
app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:%s@localhost/flightdb?charset=utf8mb4" % quote('Admin@123')

db = SQLAlchemy(app=app)