# index_data.py

import os
import json
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from config import Config

load_dotenv()

# Initialize Elasticsearch Client
es = Elasticsearch(
    f"https://{Config.ELASTICSEARCH_HOST}:{Config.ELASTICSEARCH_PORT}",
    basic_auth=(Config.ELASTICSEARCH_USER, Config.ELASTICSEARCH_PASSWORD),
    ca_certs=Config.ELASTICSEARCH_CA_CERT,
    verify_certs=True
)

# Define ES_INDEX using Config
ES_INDEX = Config.ELASTICSEARCH_INDEX

# Load BERT model
model = SentenceTransformer('all-mpnet-base-v2')  # You can choose a suitable model

# Delete the existing index if it exists
if es.indices.exists(index=ES_INDEX):
    es.indices.delete(index=ES_INDEX)

# Create Index with Mappings
es.indices.create(
    index=ES_INDEX,
    body={
        'mappings': {
            'properties': {
                'title': {'type': 'text'},
                'description': {'type': 'text'},
                'description_vector': {
                    'type': 'dense_vector',
                    'dims': 768,
                    'index': True,
                    'similarity': 'cosine'  # Use 'cosine' similarity
                }
            }
        }
    }
)

# Load Your Dataset
with open('dataset.json', 'r', encoding='utf-8') as f:
    records = json.load(f)

# Prepare Data for Bulk Indexing
def gendata():
    for record in records:
        # Vectorize the description
        description = record['description']
        vector = model.encode(description).tolist()
        yield {
            "_index": ES_INDEX,
            "_id": record['id'],
            "_source": {
                'title': record['title'],
                'description': record['description'],
                'description_vector': vector
            }
        }

# Bulk Index Data
bulk(es, gendata())

print(f"Indexed {len(records)} records to Elasticsearch.")
