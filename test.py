#!/usr/bin/env python
#-*-coding: utf-8-*-

import loglib
import os
from logging import getLogger

if __name__ == "__main__":
    logger = getLogger(__name__)
    
logger.info(__file__)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
logger.info(os.getcwd())
