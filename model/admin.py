#! /bin/env python
# coding: utf-8

from model.db import CategoryModel, ImagesModel, AffiliatecodeModel
import csv , time
import pprint

class AdminModel(object):

  def get_category_list(self):
    cm = CategoryModel()

    ret = cm.get_category_all()

    return ret
  
  def category_insert(self, category_dict):
    cm = CategoryModel()

    ret = cm.category_insert(category_dict)

    return ret    

  def get_image_list_for_file_all(self, target_file):
    ret = list()

    f = open(target_file, "r")
    
    data_reader = csv.reader(f)
    
    for data in data_reader:
      tmp_dict = dict()
      tmp_dict["image_url"] = data[0]
      tmp_dict["image_brand"] = data[1]
      tmp_dict["image_asin"] = data[2]
      tmp_dict["image_category"] = data[3]
      
      ret.append(tmp_dict)

    return ret 

  def get_image_list_for_file_asin_select(self, target_file, image_asin_s):
    ret = list()

    f = open(target_file, "r")

    data_reader = csv.reader(f)

    for data in data_reader:
      tmp_dict = dict()
      tmp_dict["image_url"] = data[0]
      tmp_dict["image_brand"] = data[1]
      tmp_dict["image_asin"] = data[2]  # asin
      tmp_dict["image_category"] = data[3]

      if data[2] in image_asin_s:
        ret.append(tmp_dict)

    return ret

  def get_image_afficode_all_for_db(self):

    ret = list()
  
    im = ImagesModel()
    ret = im.get_image_afficode_all()
  
    return ret

  def image_insert(self, image_hash_s):
    im = ImagesModel()
    count = 0
    ret_count = 0 

    for image_hash in image_hash_s:
      ret_count = im.image_insert(image_hash)
      count = count + ret_count 
      time.sleep(0.5)      

    return count

  def image_delete(self, asin):
    im = ImagesModel()

    ret = im.image_delete(asin)

    if ret == 0:
      return "OK"
    else:
      return "NG"

  def affiliate_insert(self, asin, affiliate_code):

    afm = AffiliatecodeModel()

    ret = afm.affiliate_insert(asin, affiliate_code)
    
    time.sleep(0.5)

    if ret == 0:
      return "OK"
    else:
      return "NG"
