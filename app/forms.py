from typing import Text
from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.widgets import TextArea

class ContactForm(FlaskForm):
    name = TextField('Name')
    email = TextField('Email')
    subject = TextField("Subject")
    message = TextField("Message", widget=TextArea())