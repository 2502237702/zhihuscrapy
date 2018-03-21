#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/21 14:41
# @Author  : LiuShaoheng


import tushare as ts

result = ts.get_hs300s()

key = result['code'].tolist

print(key)


