# config.py

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    ELASTICSEARCH_HOST = os.getenv('ELASTICSEARCH_HOST', 'localhost')
    ELASTICSEARCH_PORT = os.getenv('ELASTICSEARCH_PORT', '9200')
    ELASTICSEARCH_USER = os.getenv('ELASTICSEARCH_USER')
    ELASTICSEARCH_PASSWORD = os.getenv('ELASTICSEARCH_PASSWORD')
    ELASTICSEARCH_INDEX = os.getenv('ELASTICSEARCH_INDEX', 'sustainable_solutions')
    ELASTICSEARCH_CA_CERT = os.getenv('ELASTICSEARCH_CA_CERT')  # Make sure this is included
