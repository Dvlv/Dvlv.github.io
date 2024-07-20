#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Dvlv'
SITENAME = 'Dvlv\'s Blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Github', 'https://github.com/Dvlv'),('Javascript Licence', '/pages/js-licence.html'),)

MYVAR = "tsting"

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

INDEX_SAVE_AS = 'blog.html'

MENUITEMS = (
    ('Contact', '/pages/contact-me.html'),
    ('Blog', '/blog.html'),
    ('Tkinter By Example', '/pages/tkinter-by-example.html'),
    ('Tkinter Cookbook', '/pages/the-tkinter-cookbook.html'),
    ('Tkinter GUI Programming', '/pages/tkinter-gui-programming-by-example.html'),
    ('Flask By Example', '/pages/learn-flask-by-example.html'),
    ('Silverblue Beginner\'s Guide', '/pages/a-beginners-guide-to-fedora-silverblue.html'),
)

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

THEME = 'themes/dvlv'

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        # This is for enabling the TOC generation
        "markdown.extensions.toc": {"title": "Table of Contents"},
    },
    "output_format": "html5",
}

