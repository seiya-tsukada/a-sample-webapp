#! /bin/env python
# coding: utf-8

from flask import Blueprint, render_template, request, url_for, redirect
from werkzeug import secure_filename
from model.admin import AdminModel
from model.form import AdminCategoryListForm
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

  image_asin_list = list()

  am = AdminModel()
  image_asin_list = am.get_image_afficode_all_for_db()

  return render_template("admin/image_asin_afficode.html", image_asin_list = image_asin_list, list_count = len(image_asin_list))

@admin.route("/category_list/", methods=["GET", "POST"])
def adminCategoryList():

  form = AdminCategoryListForm(request.form)
  am = AdminModel()

  category_list = am.get_category_list()

  if request.method == "POST" and form.validate():
  
    category_dict = {}
    category_dict["category_name"] = form.category_name.data.encode("utf-8")
    category_dict["category_print"] = form.category_print.data.encode("utf-8")
    category_dict["category_sort"] = int(form.category_sort.data)

    am.category_insert(category_dict)

    return redirect(url_for("admin.adminCategoryList", _external=True))

  return render_template("admin/category_list.html", form = form, category_list = category_list)

@admin.route("/register_category_list/", methods=["GET"])
def adminRegisterCategoryList():

  am = AdminModel()

  images_genre = am.get_images_genre()
    
  return render_template("admin/register_category_list.html", images_genre = images_genre)  

