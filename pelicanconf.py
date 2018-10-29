#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Chris Dinant'
SITENAME = 'Transferred Learnings'
SITEURL = 'https://chrisdinant.github.io'

PATH = 'content'

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
PLUGINS = ["neighbors", "better_figures_and_images", "render_math", "disqus_static"]

MARKDOWN = {
    'extension_configs': {
        # https://pythonhosted.org/Markdown/extensions/index.html#officially-supported-extensions
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.meta': {},
        'markdown.extensions.sane_lists': {},
        'markdown.extensions.smarty': {},
        'markdown.extensions.toc': {'permalink': True},
        'mdx_video': {},
        'mdx_titlecase.mdx_titlecase:TitlecaseExtension': {},
    },
    'output_format': 'html5',
    # Allow numbered lists to not start with 1. Used in following article:
    # https://kevin.deldycke.com/2016/12/falsehoods-programmers-believe-about-falsehoods-lists/
    # See: https://pythonhosted.org/Markdown/reference.html#lazy_ol
    'lazy_ol': False,
}


RESPONSIVE_IMAGES = True


# if you create jupyter files in the content dir, snapshots are saved with the same
# metadata. These need to be ignored. 
IGNORE_FILES = [".ipynb_checkpoints"]

IPYNB_USE_METACELL = True

THEME = "/home/chris/pelican/pelican-themes/pelican-striped-html5up"

DISQUS_SITENAME = "chrisdinant"
DISQUS_SECRET_KEY = "hIiLE8jkwilNIn287D5fkyjVd1esr2ZfnEv5j98i3vw5FY6AeKSP982vuSFNmZ39"
DISQUS_PUBLIC_KEY = "xhE0WCYT9Zg931oUcHaFP2Z6rNbfeATSZuoQAAv4VEMXwv9LmDrt1SsX5Lxrz8JD"