import os
import inspect

# Flask
DEBUG = True

# Amazon S3 Settings
AWS_KEY = ''
AWS_SECRET_KEY = ''
AWS_BUCKET = 'www.vpr.net'
AWS_DIRECTORY = 'apps/now-playing/'

NPR_API_KEY = ''

COMPOSER_UCS = '5180286ee1c8bf264f49f078'

GOOGLE_SPREADSHEET = {'USER': '',
    'PASSWORD': '',
    'SOURCE': ''}

# Cache Settings (units in seconds)
STATIC_EXPIRES = 60 * 24 * 3600
HTML_EXPIRES = 3600

# Frozen Flask
FREEZER_DEFAULT_MIMETYPE = 'text/html'
FREEZER_IGNORE_MIMETYPE_WARNINGS = True
FREEZER_DESTINATION = 'News-static'
FREEZER_BASE_URL = 'http://%s/%s' % (AWS_BUCKET, AWS_DIRECTORY)
FREEZER_STATIC_IGNORE = ['Gruntfile*', 'node_modules', 'package.json',
    'dev', '.sass-cache']

WEBFACTION_PATH = AWS_DIRECTORY

ABSOLUTE_PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '/'
