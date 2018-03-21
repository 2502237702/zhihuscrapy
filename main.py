#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/20 22:41
# @Author  : LiuShaoheng


import os
import sys
from scrapy.cmdline import execute


sys.path.append(os.path.dirname(os.path.abspath(__file__)))

execute(['scrapy', 'crawl', 'zhihu'])











