#! /bin/env python
# coding: utf-8

from wtforms import Form, StringField, TextAreaField, validators

class AdminCategoryListForm(Form):

  category_name = StringField("category_name", [validators.Length(min=1, message=u"カテゴリー名を入力してください")])
  category_print = StringField("category_print", [validators.Length(min=1, message=u"カテゴリー表示名を入力してください")])
  category_sort = StringField("category_sort", [
    validators.Length(min=1, message=u"ソート番号を入力してください"),
    validators.Regexp("^[0-9]+$", message=u"番号で入力してください")
  ])
