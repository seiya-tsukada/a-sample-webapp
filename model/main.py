#! /bin/env python
# coding: utf-8

import pprint
from model.db import ImagesModel

class UtilityModel(object):

  def get_category_name(self, category_s):
    ret_list = []

    for category in category_s:
      ret_list.append(category["category_name"])

    return ret_list


  def get_category_name(self, category_s):
    ret = []
  
    for category in category_s:
      ret.append(category["category_name"])

    return ret


  def get_category_image_list(self, category_s):
    ret = dict()
    im = ImagesModel()
    limit = 6

    category_name_list = self.get_category_name(category_s)
    
    for category_name in category_name_list:
      
      tmp_list = list()

      tmp_list = im.get_images_limit(category_name, limit)

      ret[category_name] = tmp_list

    return ret 
