# -*- coding: utf-8 -*-
#
# Joao Goncalves


from flask import request, render_template, flash, Blueprint
from model import User
from database import db
import json

# For the Form
from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import DataRequired, Email, Regexp
from wtforms_alchemy import ModelForm

blueprint = Blueprint('sampleapp', __name__,
                      template_folder='templates')


class UserForm(ModelForm, Form):
    """Handle subscribe form neatly with WTForms."""
    class Meta:
        model = User

    name = StringField(u'Name:', validators=[DataRequired()])
    email = StringField(u'Email', validators=[Email(), DataRequired()])


@blueprint.route('/', methods=['GET', 'POST'])
def index():
    """Returns the newly added users since the last request.

    API used by the backend application
    """
    users = []
    for row in User.query.all():
        users.append((row.id, row.name, row.email))
    return render_template('list.html', users=json.dumps(users))


def form_subscribe(data):
    """Handle subscription form submission."""
    try:
        # Try to find an existing user to update
        u = User.query.filter_by(name=e_data['name']).first()
        # !TODO: This requires refactoring..
        if u:
            # Update User
            u.name = e_data['name']
            u.email = e_data['email']
        else:
            # Create new User
            u = User(e_data['name'],
                     e_data['email'])
        db.session.add(u)
        db.session.commit()
        return True
    except Exception, e:
        print('form_subscribe():', str(e))
        flash(u'Saving to database failed.', 'Error')
        # Should return the errors (possibly duplicate or?)
        return False
