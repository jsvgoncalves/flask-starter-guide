# -*- coding: utf-8 -*-
#
# Joao Goncalves
from flask import url_for
from sampleapp.model import User as U
from pytest import fail


def test_user_insert(session):
    """Test the User insertion."""
    assert U.query.count() == 0
    u = U('name',
          'email')
    session.add(u)
    assert U.query.count() == 1


def test_routes(client, session):
    """Test the available routes and their accessible methods."""
    pass
    # index should allow both GET and POST requests
    # assert client.get(
    #     url_for('sampleapp.get_subscribers')).status_code == 200
    # assert client.post(
    #     url_for('sampleapp.get_subscribers')).status_code == 200
