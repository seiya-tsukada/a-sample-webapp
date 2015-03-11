#! /bin/env python
# coding: utf-8

from flask import Flask
from controller.main import main
from controller.admin import admin
from controller.tbox import tbox
from controller.my_affi import my_affi
from controller.api import api

app = Flask(__name__)

# To controller
# main contents
app.register_blueprint(main)

# admin tools
app.register_blueprint(admin, url_prefix="/admin")

# thinkbox page
app.register_blueprint(tbox, url_prefix="/tbox")

# affiliate page
app.register_blueprint(my_affi, url_prefix="/my_affi")

# api
app.register_blueprint(api, url_prefix="/api")

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
