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

DISPLAY_PAGES_ON_MENU = True
HEADER_COVERS_BY_CATEGORY = {'data-science': '/extra/dark.jpg', 'not-data-science': '/images/markus-spiske-78531-unsplash.jpg'}

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
    "disqus_static",
    "pelican-open_graph"
]

RESPONSIVE_IMAGES = True

# if you create jupyter files in the content dir, snapshots are saved with the same
# metadata. These need to be ignored. 
IGNORE_FILES = [".ipynb_checkpoints"]

IPYNB_USE_METACELL = True

THEME = "/home/chris/pelican/attila" # note, not in pelican-themes directory

GOOGLE_SITE_VERIFICATION = "yQh84bCkno9EjLcuqA5P2dztLWkwgr5WVqTJa9Za_6g"

DISQUS_SITENAME = "chrisdinant"
DISQUS_SECRET_KEY = "hIiLE8jkwilNIn287D5fkyjVd1esr2ZfnEv5j98i3vw5FY6AeKSP982vuSFNmZ39"
DISQUS_PUBLIC_KEY = "xhE0WCYT9Zg931oUcHaFP2Z6rNbfeATSZuoQAAv4VEMXwv9LmDrt1SsX5Lxrz8JD"

AUTHORS_BIO = {
  "chris dinant": {
    "name": "chris dinant",
    "cover": "extra/bg1.png",
    "image": "extra/delta9.png",
    "twitter": "chrisdinant",
    "linkedin": "chris-dinant",
    "github": "chrisdinant",
    "location": "Copenhagen",
    "bio": "Only if you can explain something in simple terms do you really understand it. That's what I'm trying to do with this blog."
  }
}
