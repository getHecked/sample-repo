#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Defines the Facebook form. Called from app.py."""

from wtforms import DecimalField
from wtforms import Form
from wtforms import IntegerField
from wtforms import PasswordField
from wtforms import StringField
from wtforms import TextAreaField
from wtforms import validators


class FacebookMessageForm(Form):
    """Sets the main format for the Facebook Form."""

    # Login details for users
    login = StringField('Facebook E-Mail',
                        [validators.Length(min=1, max=100),
                         validators.DataRequired()])
    password = PasswordField('Facebook Password',
                             [validators.Length(min=1, max=100),
                              validators.DataRequired()])
    # Recipients Facebook ID
    facebook_uid = IntegerField('Facebook UID',
                                [validators.DataRequired()])
    # Message itself
    number_of_messages = IntegerField('Number of messages to send',
                                      [validators.DataRequired()])
    time_interval_between_messages = DecimalField(
        'Number of seconds between messages',
        [validators.DataRequired()]
        )
    message_text = TextAreaField('Message',
                                 [validators.Length(min=1, max=100)])
