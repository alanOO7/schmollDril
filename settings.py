#!/usr/bin/env python
# coding=utf-8
# -*- coding: UTF-8 -*-
import os
#from logger_format import log_format
#from Lib import logger_format as log_format
import sys   #reload()之前必须要引入模块

reload(sys)
sys.setdefaultencoding('utf-8')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_CFG = os.path.join(BASE_DIR, 'logging.json')
sys.path.append(BASE_DIR+"/Lib")
from logger_format import log_format
# set log file
logger = log_format()

#-*- encoding:utf-8 -*-
