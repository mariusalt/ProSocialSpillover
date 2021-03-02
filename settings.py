from os import environ
import dj_database_url
import os
#from boto.mturk import qualification

import otree.settings
SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
 #   'use_browser_bots':True,
}

SESSION_CONFIGS = [
    {
     'name': 'dce',
     'display_name': 'dce',
     'num_demo_participants': 50,
     'app_sequence': ['Introduction','dce','dce1','don','ambi']
 },
    {
     'name': 'dce1',
     'display_name': 'dce1',
     'num_demo_participants': 1,
     'app_sequence': ['Introduction','dce1','don','ambi']
 },
    {
     'name': 'ambi',
     'display_name': 'ambi',
     'num_demo_participants': 1,
     'app_sequence': ['ambi']
 },
    {
     'name': 'ques',
     'display_name': 'ques',
     'num_demo_participants': 10,
     'app_sequence': ['Introduction','don','ambi']
 },
 {
     'name': 'don',
     'display_name': 'don',
     'num_demo_participants': 1,
     'app_sequence': ['don','ambi']
 }
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'de'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '*n6csl6k*yqmed_jdub%97rs_!ew($yg6q_7)uod%(6r(yh#+y'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']


