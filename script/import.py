#! /usr/bin/env python
# coding: utf-8

import sys, os, csv
import MySQLdb
from pprint import pprint

class Importer:
  
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

    self.cursor.execute(query)

    return

  def csv_import(self, number):

    argvs = sys.argv
    target_file = argvs[1]
    download_dir = "/var/app/static/images/"
    
    f = open(target_file, 'r')

    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
      name = row[2] + str(number) + ".jpg"
      category = row[2]
      genre = row[1]
      ret = None

      wget_cmd = "wget {0} -O {1}{2}".format(row[0], download_dir, name)

      ret = os.system(wget_cmd)
      if ret == 0:
        insert_cmd = "INSERT INTO images (images_id, images_name, images_category, images_genre) VALUES (NULL, '{0}', '{1}', '{2}');".format(name, category, genre)

        self.cursor.execute(insert_cmd)

        number = number + 1    
      else:
        os.remove(download_dir + name)

    f.close()
    
    self.conn.commit()
    os.remove(target_file)

    return
  

if __name__ == "__main__":

  importer = Importer()
  importer.db_define()

  query = None 
  rows = None
  number = None

  query = "SELECT MAX(images_id) + 1 AS number FROM images"
  rows = importer.db_select(query)

  number = rows[0]["number"] if rows[0]["number"] != None else 1
  importer.csv_import(number)

  importer.db_close() 

  sys.exit(0) 
