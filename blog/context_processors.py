#!/usr/bin/env python
# encoding: utf-8


"""
@version: 1.0 Beta
@author: Deepak
@license: MIT Licence
@contact: medgloss@gmail.com
@site: https://www.medgloss.com/
@software: Visual Studio Code
@file: context_processors.py
"""
from .models import Category, Article, Tag, BlogSettings
from Medgloss.utils import cache, get_blog_setting

from datetime import datetime
import logging

logger = logging.getLogger(__name__)


def seo_processor(requests):
    key = 'seo_processor'
    value = cache.get(key)
    if value:
        return value
    else:
        logger.info('set processor cache.')
        setting = get_blog_setting()
        value = {
            'SITE_NAME': setting.sitename,
            'SHOW_GOOGLE_ADSENSE': setting.show_google_adsense,
            'GOOGLE_ADSENSE_CODES': setting.google_adsense_codes,
            'SITE_SEO_DESCRIPTION': setting.site_seo_description,
            'SITE_DESCRIPTION': setting.site_description,
            'SITE_KEYWORDS': setting.site_keywords,
            'SITE_BASE_URL': requests.scheme + '://' + requests.get_host() + '/',
            'ARTICLE_SUB_LENGTH': setting.article_sub_length,
            'nav_category_list': Category.objects.all(),
            'nav_pages': Article.objects.filter(
                type='p',
                status='p'),
            'OPEN_SITE_COMMENT': setting.open_site_comment,

            'ANALYTICS_CODE': setting.analyticscode,


            "CURRENT_YEAR": datetime.now().year}
        cache.set(key, value, 60 * 60 * 10)
        return value
