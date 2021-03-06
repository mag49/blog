from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    
    id= db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255),unique=True, index=True)
    bio = db.Column(db.String(5000))
    profile_pic_path = db.Column(db.String)
    pass_secure = db.Column(db.String(255))
    date_joined = db.Column(db.DateTime,default=datetime.utcnow)
    
    blogs = db.relationship('Blog',backref = 'user', lazy='dynamic')
    
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    
    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)
        
    def verify_password(self, password):
        return check_password_hash(self.pass_secure,password)
    
    def __repr__(self):
        return f'User {self.username}'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
        
class Blog(db.Model):
    __tablename__ = 'blogs'
    
    id = db.Column(db.Integer,primary_key = True)
    blog_title = db.Column(db.String)
    blog_content = db.Column(db.String(1000))
    category = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comments = db.relationship('Comment' , backref= 'blog_id', lazy='dynamic')
    
    def save_blog(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_blogs(cls,category):
        blogs=Blog.query.filter_by(category=category).all() 
        return blogs  
    
    @classmethod
    def get_blog(cls,id):
        blog = Blog.query.filter_by(id=id).first() 
        return blog
    
class Comment(db.Model):
    __tablename__ = 'comments'
        
    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(1000))
    username=db.Column(db.String(255))
    blog = db.Column(db.Integer,db.ForeignKey('blogs.id'))
        
    def save_comment(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_comments(cls,blog_id):
        comments = Comment.query.filter_by(id=blog_id).all()
        return comments
    