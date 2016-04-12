#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'Thomas'}
    return render_template("index.html",
                           title = 'Heme',
                           user = user)