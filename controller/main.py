#! /bin/env python
# coding: utf-8

from flask import Blueprint, render_template, request, redirect, url_for
from model.main import UtilityModel
from model.db import CategoryModel, ImagesModel
from werkzeug import secure_filename
import os, commands, json
import pprint

main = Blueprint("main", __name__)

@main.route("/")
def index():

  cm = CategoryModel()
  um = UtilityModel()
  im = ImagesModel()

  category_list = cm.get_category_all()
  images_dict = um.get_category_image_list(category_list)
  
  return render_template("index.html", category_list = category_list, images_dict = images_dict)


@main.route("/<category>/")
@main.errorhandler(404)
def category(category):

  cm = CategoryModel()
  im = ImagesModel()
  um = UtilityModel()

  category_list = cm.get_category_all()

  category_name_s = um.get_category_name(category_list)

  if category in category_name_s:

    image_s = im.get_images(category)

    return render_template("category.html", category = category, image_s = image_s)
  else:
    return render_template("error/404.html"), 404
    
@main.route("/<category>/test/")
def test(category):

  cm = CategoryModel()
  um = UtilityModel()

  category_s = cm.get_category() 
  ret_list = um.dblist_to_dict(category_s)
  
  print ret_list
  return "a"
