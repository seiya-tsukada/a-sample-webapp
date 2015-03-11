#! /bin/env python
# coding: utf-8

from flask import Blueprint, request, jsonify
from model.admin import AdminModel
import os, time, json
import pprint

api = Blueprint("api", __name__)

@api.route("/afficode_register/", methods=["POST"])
def AfficodeRegister():

  if request.is_xhr:

    ret = None
    am = AdminModel()

    post_param = request.json
    
    ret = am.affiliate_insert(post_param["asin"], post_param["affiliate_code_url"])

    return jsonify({"return" : ret})
  else:
    return "Error"

@api.route("/afficode_delete/", methods=["POST"])
def AfficodeDelete():

  if request.is_xhr:

    ret = None
    am = AdminModel()

    post_param = request.json

    ret = am.image_delete(post_param["asin"])

    return jsonify({"return" : ret})
  else:
    return "Error"
