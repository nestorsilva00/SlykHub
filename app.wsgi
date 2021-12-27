#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/SlykHub/")

from app import app as application
application.secret_key = '8pe6[uS{xj+rP:X^'