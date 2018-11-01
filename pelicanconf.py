#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Chris Dinant'
SITENAME = 'Transferred Learnings'
SITEURL = 'https://chrisdinant.github.io'
SITESUBTITLE = 'I have very short long term memory'

PATH = 'content'

SITE_LOGO = '/extra/delta9.png'
HEADER_COVER = '/extra/bg1.jpg'
TWITTER_IMAGE = '/extra/delta9.png'
HEADER_COLOR = 'black'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

DISPLAY_PAGES_ON_MENU = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = [
    'images',
    'extra',
]

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},      
}

MARKUP = ('md')

PLUGIN_PATHS = ["/home/chris/pelican/pelican-plugins"]
PLUGINS = [
    "neighbors",
    "assets", 
    "better_figures_and_images", 
    "render_math", 
    "disqus_static"
]

RESPONSIVE_IMAGES = True


# if you create jupyter files in the content dir, snapshots are saved with the same
# metadata. These need to be ignored. 
IGNORE_FILES = [".ipynb_checkpoints"]

IPYNB_USE_METACELL = True

THEME = "/home/chris/pelican/attila" # note, not in pelican-themes directory

DISQUS_SITENAME = "chrisdinant"
DISQUS_SECRET_KEY = "hIiLE8jkwilNIn287D5fkyjVd1esr2ZfnEv5j98i3vw5FY6AeKSP982vuSFNmZ39"
DISQUS_PUBLIC_KEY = "xhE0WCYT9Zg931oUcHaFP2Z6rNbfeATSZuoQAAv4VEMXwv9LmDrt1SsX5Lxrz8JD"

AUTHORS_BIO = {
  "delta9": {
    "name": "chris dinant",
    "cover": "extra/bg1.png",
    "image": "extra/delta9.png",
    "website": "https://chrisdinant.github.io",
    "linkedin": "chris-dinant",
    "github": "chrisdinant",
    "location": "Copenhagen",
    "bio": "This is the place for a small biography with max 200 characters. Well, now 100 are left. Cool, hugh?"
  }
}