from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
from flask import Flask, render_template, request

class users_db(db.Model):
    __tablename__ = "users_db"
    user_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable = True)
    profile_picture_name = db.Column(db.String, nullable = True)
    shared_file_name = db.Column(db.String, nullable = True)
    num_downloads = db.Column(db.Integer, nullable = True)
    num_uploads = db.Column(db.Integer, nullable = True)
    

   
# class pictures_db(db.Model):
#     __tablename__ = "pictures_db"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String, nullable=False)
#     flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)
