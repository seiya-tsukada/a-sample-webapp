#! /bin/env python
# coding: utf-8

#! /usr/bin/env python
# coding: utf-8

import sys, os, csv
import MySQLdb
import pprint

class DbConnect(object):

  host = "127.0.0.1"
  db_user = "root"
  db_passwd = "zaq12wsx"
  db_name = "my_app"

  conn = None
  cursor = None

  def db_define(self):
    self.conn = MySQLdb.connect(db=self.db_name, host=self.host, user=self.db_user, passwd=self.db_passwd)
    self.cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)

    return

  def db_close(self):
    self.cursor.close()
    self.conn.close()

    return

  def db_select(self, query):

    self.cursor.execute(query)

    rows = self.cursor.fetchall()

    return rows


  def db_execute(self, query):

    ret = None

    ret = self.cursor.execute(query)

    return ret

class CategoryModel(DbConnect):

  def __init__(self):
    self.db_define()

    return

  def get_category_all(self):

    sql = "SELECT * FROM category;"
    
    ret = self.db_select(sql)

    return ret

class ImagesModel(DbConnect):

  def __init__(self):
    self.db_define()

    return

  def get_images_all(self):

    sql = "SELECT * FROM images;"

    ret = self.db_select(sql)

    return ret

  def get_images(self, category):
    
    sql = "SELECT * FROM images WHERE images_category = '{0}'".format(category)

    ret = self.db_select(sql)

    return ret

  def get_images_limit(self, category, limit):

    sql = "SELECT * FROM images WHERE images_category = '{0}' LIMIT {1}".format(category, limit)

    ret = self.db_select(sql)

    return ret

  def get_image_afficode_for_asin(self, image_asin):

    sql = "SELECT * FROM images as im LEFT JOIN affiliate_code as ac ON im.images_asin = ac.affiliate_code_asin WHERE im.images_asin = '{0}'".format(image_asin)

    ret = self.db_select(sql)

    return ret

  def image_insert(self, image_hash):

    sql = "SELECT images_asin FROM images WHERE images_asin = '{0}'".format(image_hash["image_asin"])

    ret = self.db_select(sql)

    if len(ret) == 0:
      sql = "INSERT INTO images (images_id, images_url, images_category, images_genre, images_asin) VALUES (NULL, '{0}', '{1}', '{2}', '{3}');".format(image_hash["image_url"], image_hash["image_category"], image_hash["image_brand"], image_hash["image_asin"])  

      ret = self.db_execute(sql)

      if ret == 1:
        self.conn.commit()
        return int(1)
 
    return int(0)
