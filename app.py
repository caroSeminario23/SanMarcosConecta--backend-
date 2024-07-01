from flask import Flask
from flask_cors import CORS
from utils.db import db

from services.administrativo import administrativo_routes

from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION


app=Flask(__name__)

CORS(app, origins=['http://localhost:4200'], 
     methods=['GET', 'POST', 'PUT', 'DELETE'], 
     allow_headers=['Content-Type', 'Authorization'])


app.config['SQLALCHEMY_DATABASE_URI']=DATABASE_CONNECTION

#SQLAlchemy(app)
db.init_app(app)

app.register_blueprint(administrativo_routes, url_prefix='/administrativo_routes')


with app.app_context():
    db.create_all()

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True,port=5000)