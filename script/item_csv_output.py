#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import csv

def check_argv(argvs):
  argc = len(argvs)

  if argc != 2:
    sys.stderr.write("not argvs")
    sys.exit(1)

  return

def csv_output(target_file, category):
  f = None   
  f = open(target_file, "r")

  data_reader = csv.reader(f)

  for row in data_reader:
    title = row[0]
    asin = row[1]
    url = row[2]
    image = row[3]
    amount = row[4]
    brand = row[5]

    output = "{0},{1},{2},{3}".format(image, brand, asin, category)

    print output

def main(category):
  target_dir = "/var/app/script/amazon_item/"

  target_file_s = os.listdir(target_dir)

  for i_file in target_file_s:
    csv_output("{0}{1}".format(target_dir, i_file), category)

if __name__ == "__main__":
  argvs = sys.argv
  check_argv(argvs) 

  main(argvs[1])

  sys.exit(0)
