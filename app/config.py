import os

class Config:
    FREEZER_DESTINATION = '../docs'
    FREEZER_REMOVE_EXTRA_FILES = False
    FREEZER_DEFAULT_MIMETYPE = 'text/html'
    FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite', 'fenced_code']
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key')
    SITE_URL = 'https://harmanankohli.github.io/HarmananKohli'
    SITE_NAME = 'Harmanan Kohli | LLM/AI Engineer'
