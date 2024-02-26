#!/usr/bin/python3
"""
This module contains the index
"""
from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
# Import all views here to register them
from api.v1.views.index import *
from api.v1.views.states import *
