__author__ = 'tan'
import os
import random
import string

USERNAME = 'tech-testing-ha2-26@bk.ru'
PASSWORD = os.environ['TTHA2PASSWORD']
DOMAIN = '@bk.ru'
CAMPAIGN = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(6)])
REF = 'https://play.google.com/store/apps/details?id=com.rovio.retry'
TEXT = 'qqqqqq'
TITLE = 'eeeeee'
SMALL_IMAGE  = '866.jpg'
BIG_IMAGE  = 'luli.jpg'
