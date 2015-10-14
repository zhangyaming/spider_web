# encoding: utf-8
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spider_web.settings')

import django
django.setup()

from app.models import News, Comments




#函数定义
def add_news()