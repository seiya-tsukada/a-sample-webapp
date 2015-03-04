#! /usr/bin/env python
# coding: utf-8

from bottlenose import api
from BeautifulSoup import BeautifulSoup
import pprint, sys, datetime

def check_argv(argvs):
  argc = len(argvs)

  if argc != 5:
    sys.stderr.write("not argvs")
    sys.exit(1)
  
  return 

def check_search_index(search_index):
  search_index_list = [ "Apparel", "Watches" ]

  if search_index not in search_index_list:
    sys.stderr.write("invalid search index argument")
    sys.exit(2)

  return
  
def get_item_via_amazon(search_index, keyword, page_num):
  AMAZON_ACCESS_KEY_ID = "AKIAJ523XFETCVI2NL2Q"
  AMAZON_SECRET_KEY = "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"
  AMAZON_ASSOC_TAG = "subaccst-22"
  
  amazon = api.Amazon(AMAZON_ACCESS_KEY_ID, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG,  Region="JP")
  
  response = amazon.ItemSearch(SearchIndex=search_index, Keywords=keyword, ItemPage=page_num, ResponseGroup="Large")
  soup = BeautifulSoup(response)
  
  return soup.findAll("item")

def write_item_info(item_all, brand):
  
  d_now = datetime.datetime.now()
  prefix = d_now.strftime("%m%d%s")
  target_file = "/var/app/script/amazon_item/file{0}".format(prefix)

  f = open(target_file, "a")

  for i in item_all:
    print_line = None

    i_title = i.find("title").text.encode("utf-8")
    i_asin = i.find("asin").text
    i_url = "http://www.amazon.co.jp/dp/{0}".format(i_asin)

    try:
      i_image = i.find("mediumimage").find("url").text
    except Exception, e:
      i_image = e
  
    try:
      i_amount = i.find("amount").text
    except Exception, e:
      i_amount = e
  
    print_line = "{0},{1},{2},{3},{4},{5}\n".format(i_title, i_asin, i_url, i_image, i_amount, brand)

    f.write(print_line)

  f.close()

if __name__ == "__main__":

  argvs = sys.argv
  check_argv(argvs)

  search_index = argvs[1]
  check_search_index(search_index)
  
  category = unicode(argvs[2], "utf-8")
  brand = unicode(argvs[3], "utf-8")
  keyword = category + " " + brand

  page_num = argvs[4]
  
  item_all = get_item_via_amazon(search_index, keyword, page_num)
  write_item_info(item_all, brand)

  print "success!!"
  sys.exit(0)
