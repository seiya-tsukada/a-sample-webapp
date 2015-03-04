#! /bin/env python
# coding: utf-8

from flask import Blueprint, render_template, request, url_for, redirect
from werkzeug import secure_filename
from model.db import ImagesModel
import os, commands, json
from pprint import pprint

tbox = Blueprint("tbox", __name__)

@tbox.route("/", methods=["GET"])
def index():

  image_asin = request.args.get("image_asin")
  im = ImagesModel()
  image_print_url = None
  
  image_hash = im.get_image_afficode_for_asin(image_asin)

  image_print_url = unicode(image_hash[0]["affiliate_code_url"], "utf-8") if image_hash[0]["affiliate_code_url"] else ""

  return render_template("tbox/index.html", image_print_url = image_print_url)
