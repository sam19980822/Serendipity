from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms import StringField, SubmitField, FileField, PasswordField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed, FileRequired
from flask_pagedown.fields import PageDownField
from flask_pagedown import PageDown

class registForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    re_enter_password = PasswordField('re-enter password', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    submit = SubmitField('Submit')

class loginForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class postForm(FlaskForm):
    #  加入一個form，單純的一個PageDownField跟提交欄位測試
    title = StringField('title')
    pagedown = PageDownField('Enter your markdown')
    submit = SubmitField('post')


class PhotoForm(FlaskForm):
    photo = FileField('image', validators=[
        FileRequired(),
        FileAllowed(['jpg','png'], 'Imahes only!')])