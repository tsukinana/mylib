#!/usr/bin/env python
#-*-coding: utf-8-*-

from lib.log import org_get_logger
import os

logger = org_get_logger(__name__)    
logger.info(__file__)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
logger.info(os.getcwd())
