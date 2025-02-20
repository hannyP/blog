from flask_wtf import FlaskForm
from wtforms import *
# from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, URL,Email
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    author = StringField("Author name",validators=[DataRequired()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    email = StringField("Email",validators=[DataRequired()])
    password =PasswordField("Password",validators=[DataRequired()])
    name = StringField("Your Name",validators=[DataRequired()])
    submit = SubmitField("register")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("LET ME IN!")

class CommentForm(FlaskForm):
    comment = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("SUBMIT COMMENT")