#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import json
import os
import logging.config
import logging
#from settings import *


def set_logging(default_path="logging.json", default_level=logging.INFO, env_key="LOG_CFG"):
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, "r") as f:
            config = json.load(f)
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
    print "path{0}",path

set_logging()


def log_format():
    logger = logging.getLogger()
    return logger
