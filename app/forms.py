from flask_wtf import FlaskForm
from wtforms import String field, TextField, SubmitField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField('Name',validators =[DataRequired()])
    email = StringField('Email',validators=[DataRequired(), Email()])
    subject = StringField('Subject',validators =[DataRequired()])
    message = TextField('Message',validators = [DataRequired()])
    send = SubmitField('Send')
