#! /bin/env python
# coding: utf-8

from flask import Blueprint, render_template

my_affi = Blueprint("my_affi", __name__)

@my_affi.route("/", methods=["GET"])
def index():

  return render_template("my_affi/index.html")
