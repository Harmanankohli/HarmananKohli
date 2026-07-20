import os

class Config:
    FREEZER_DESTINATION = '../docs'
    FREEZER_RELATIVE_URLS = True
    FREEZER_REMOVE_EXTRA_FILES = True
    FREEZER_DEFAULT_MIMETYPE = 'text/html'
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key')
    SITE_URL = 'https://harmanankohli.github.io/HarmananKohli'
    SITE_NAME = 'Harmanan Kohli | LLM/AI Engineer'
