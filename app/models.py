from . import db

#...

# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer,primary_key = True)
#     username = db.Column(db.String(255))
#     role_id = db.relationship('Role',backref = 'role',lazy="dynamic")

#     def __repr__(self):
#         return f'User {self.username}'

# class Role(db.Model):
#     __tablename__ = 'roles'

#     id = db.Column(db.Integer,primary_key = True)
#     name = db.Column(db.String(255))
#     user_role = db.Column(db.Integer, db.ForeignKey('users.id'))


#     def __repr__(self):
#         return f'User {self.name}'        