from main import hangout
from flask import render_template, session, flash, redirect, url_for, request
from flask.blueprints import Blueprint
from flask_login import current_user, login_user
from flask_login.utils import login_required, login_user, logout_user
from . import app, bcrypt, db, login_manager
from .models import User, HangOutGroup, Event
from .form import Login, Register
from datetime import datetime



mainbp = Blueprint('main', __name__)
