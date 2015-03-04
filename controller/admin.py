#! /bin/env python
# coding: utf-8

from flask import Blueprint, render_template, request, url_for, redirect
from werkzeug import secure_filename
from model.admin import AdminModel
import os, commands, json
import pprint

admin = Blueprint("admin", __name__)

@admin.route("/")
def index():

  return render_template("admin/index.html")

@admin.route("/image_register_list/", methods=["GET", "POST"])
def adminImageRegisterList():

  if request.method == "POST":
    upload_dir = "/tmp"
    f = request.files["file_name"]
    file_name = secure_filename(f.filename)

    upload_file_name = os.path.join(upload_dir, file_name)
    f.save(upload_file_name)

    am = AdminModel()
    image_s = am.get_image_list_for_file_all(upload_file_name)

    return render_template("admin/image_register_list.html", image_s = image_s, upload_file_name = upload_file_name)

  return render_template("admin/image_register_list.html")

@admin.route("/image_register/", methods=["POST"])
def adminImageRegister():
  
  register_count = 0
  image_asin_s = request.form.getlist("image_asin")
  upload_file_name = request.form.get("upload_file_name")

  am = AdminModel()
  image_hash_s = am.get_image_list_for_file_asin_select(upload_file_name, image_asin_s)
  register_count = am.image_insert(image_hash_s)

  os.remove(upload_file_name)
 
  return render_template("admin/image_register.html", register_count = register_count)

@admin.route("/image_asin_afficode/")
def adminAsinAfficode():

  return render_template("admin/image_asin_afficode.html")

#@admin.route("/upload/", methods=["GET", "POST"])
#def adminUpload():
#
#  if request.method == "POST":
#    upload_dir = "/tmp"
#    f = request.files["file_name"]
#    file_name = secure_filename(f.filename)
#
#    upload_file_name = os.path.join(upload_dir, file_name)
#    f.save(upload_file_name)
#
#    exec_command = "python /var/app/script/import.py {0}".format(upload_file_name)
#    ans = commands.getoutput(exec_command)
# 
#    return render_template("admin/upload.html", message = "success") 
#
#  return render_template("admin/upload.html")

