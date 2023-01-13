from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from wtforms.widgets import TextArea
from app.models import User

style_StrField = {'class': 'form-control'}
style_SubField = {'class': 'btn btn-primary'}

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw=style_StrField)
    password = PasswordField('Password', validators=[DataRequired()], render_kw=style_StrField)
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login', render_kw=style_SubField)

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=15)], render_kw=style_StrField)
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw=style_StrField)
    password = PasswordField('Password', validators=[DataRequired()], render_kw=style_StrField)
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')], render_kw=style_StrField)
    submit = SubmitField('Sign Up', render_kw=style_SubField)

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class NoteForm(FlaskForm):
    data = StringField('New Note', validators=[DataRequired(), Length(min=4, max=10000-2)], widget=TextArea(), render_kw=style_StrField)
    submit = SubmitField('Add Note', render_kw=style_SubField)