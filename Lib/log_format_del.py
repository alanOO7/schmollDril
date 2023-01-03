#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import logging
from logging.handlers import RotatingFileHandler


def log_format(log_file_name):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # log level: critical > error > warning > info > debug
    formatter = logging.Formatter('[%(asctime)s - %(name)s - %(levelname)s]: %(message)s')

    # set log rotate
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_dir = os.path.join(base_dir, 'log')
    log_file = os.path.join(log_dir, log_file_name)
    if not logger.handlers:
        rh = RotatingFileHandler(log_file, maxBytes=100 * 1024 * 1024, backupCount=5)
        rh.setLevel(logging.INFO)
        rh.setFormatter(formatter)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)

        logger.addHandler(rh)
        logger.addHandler(ch)

    return logger
