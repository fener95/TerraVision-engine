# app/routes.py

from flask import Blueprint, render_template, request
from elasticsearch import Elasticsearch
from config import Config
from sentence_transformers import SentenceTransformer

main = Blueprint('main', __name__)

# Initialize Elasticsearch Client
es = Elasticsearch(
    f"https://{Config.ELASTICSEARCH_HOST}:{Config.ELASTICSEARCH_PORT}",
    basic_auth=(Config.ELASTICSEARCH_USER, Config.ELASTICSEARCH_PASSWORD),
    ca_certs=Config.ELASTICSEARCH_CA_CERT,
    verify_certs=True
)

# Load BERT model
model = SentenceTransformer('all-mpnet-base-v2')

@main.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        # Use only the 'solution' field for now
        solution = request.form.get('solution')

        if solution:
            # Vectorize the query
            query_vector = model.encode(solution).tolist()

            # Build Elasticsearch k-NN query
            query_body = {
                "size": 5,
                "query": {
                    "knn": {
                        "field": "description_vector",
                        "query_vector": query_vector,
                        "k": 5,
                        "num_candidates": 10
                    }
                }
            }

            response = es.search(index=Config.ELASTICSEARCH_INDEX, body=query_body)
            results = [hit['_source'] for hit in response['hits']['hits']]

    return render_template('index.html', results=results)
