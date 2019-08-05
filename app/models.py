from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime
from . import login_manager

 
class PhotoProfile(db.Model):

   __tablename__ = 'profile_photos'

   id = db.Column(db.Integer,primary_key = True)
   pic_path = db.Column(db.String())
   user_id = db.Column(db.Integer,db.ForeignKey("users.id"))




class Pitch(db.Model):
    __tablename__ = 'pitch'

    id = db.Column(db.Integer, primary_key = True )
    title = db.Column(db.String(100))
    content = db.Column(db.Text(1600))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    category = db.Column(db.String(255))
    def __repr__(self):
        return f"Pitch('{self.title}')"

    @classmethod
    def get_all_pitches(cls):
        '''
        Function that queries database and returns all posted pitches.
        '''
        return Pitch.query.all()
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def clear_pitch(cls):
        Pitch.all_pitchs.clear()



class User(UserMixin,db.Model):
    __tablename__ = 'users'
    pitch = db.relationship('Pitch', backref = 'users', lazy="dynamic")
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    password = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    
   
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    
   

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    






    