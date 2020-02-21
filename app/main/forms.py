from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required
from flask_login import current_user

class BlogForm(FlaskForm):
    title = StringField('Blog title', validators=[Required()])
    content = TextAreaField('Text',validators=[Required()])
    category = SelectField('Type',choices=[('lifestyle','lifesytle blog'),('travelblogs','Travel Blogs')])
    submit = SubmitField('Submit')
    
class CommentForm(FlaskForm):
    username = StringField('Username', validators=[Required()])
    text = TextAreaField('Leave a comment:',validators=[Required()])
    submit = SubmitField('submit')
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('tell us about you.',validators=[Required])