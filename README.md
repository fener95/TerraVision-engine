🌱 MetaSearch Engine for Agriculture 🌾
Welcome to the MetaSearch Engine for Agriculture! This project is a semantic search application designed to help users find sustainable agricultural solutions efficiently. It leverages the power of machine learning and Elasticsearch to provide relevant results based on user queries.

📖 Table of Contents 

- Introduction
- Features
- Architecture
- Demo
- Installation
- Usage
- Technologies Used
- Contributing
- License
- Contact

Introduction

In the quest for sustainable agriculture, finding the right solutions can be challenging. The MetaSearch Engine, combined with Semantic analysis, simplifies this by providing a user-friendly platform where farmers and stakeholders can search for agricultural products and services tailored to their needs.

Features

🔍 Semantic Search: Find relevant agricultural solutions based on the meaning of your query, not just keywords.
⚡ Fast and Efficient: Real-time search results powered by Elasticsearch.
🌐 User-Friendly Interface: Easy-to-use web application built with Flask.
📊 Scalable Architecture: Designed to handle growing datasets and user traffic.
💾 Caching Mechanism: Improved performance with query result caching.
Architecture
The application follows a modular architecture:

User Interface (UI): A Flask web app where users input their queries.
Data Layer:
Dataset containing agricultural products and solutions.
Data processing and vectorization using a pre-trained BERT model.
Search Engine:
Elasticsearch for indexing and searching vectorized data.
Semantic Search Workflow:
User inputs are encoded into vectors.
Elasticsearch performs similarity matching.
Relevant results are displayed to the user.
Caching Mechanism: SQLite database caches query results.
(Include an architecture diagram if available)

Demo
Coming soon! 🚀

Installation
Follow these steps to set up the project locally.

Prerequisites
Python 3.10 or higher
pip package manager
Elasticsearch 8.x
Git

Steps
Clone the Repository:

git clone https://github.com/fener95/TerraVision-engine.git
cd TerraVision-engine

Create a Virtual Environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies:

pip install -r requirements.txt
Set Up Environment Variables:

Create a .env file in the root directory and add the following:

env

ELASTICSEARCH_HOST=localhost
ELASTICSEARCH_PORT=9200
ELASTICSEARCH_USER=elastic
ELASTICSEARCH_PASSWORD=your_elastic_password  # Replace with your actual password
ELASTICSEARCH_INDEX=sustainable_solutions
ELASTICSEARCH_CA_CERT=path_to_your_http_ca.crt  # Update the path accordingly
Start Elasticsearch:

Ensure Elasticsearch is running. Navigate to your Elasticsearch installation directory and run:

bash

./bin/elasticsearch  # On Windows use `.\bin\elasticsearch.bat`
Index the Data:

Run the indexing script to populate Elasticsearch with the dataset.


python index_data.py
Run the Application:


python app.py
Access the Web Interface:

Open your browser and navigate to http://localhost:5000.

Usage
Navigate to the Web App:

Visit http://localhost:5000.

Perform a Search:

Enter your query in the "Solution Needed" field.
Click "Search".
View Results:

Browse through the list of relevant agricultural solutions.

Technologies Used
Python 🐍
Flask 🌶️
Elasticsearch 🔎
SentenceTransformers 🧠
SQLite 💾
HTML/CSS 🎨
Contributing
Contributions are welcome! Please read the contribution guidelines before making a pull request.

Fork the repository.
Create your feature branch: git checkout -b feature/YourFeature
Commit your changes: git commit -m 'Add some feature'
Push to the branch: git push origin feature/YourFeature
Open a pull request.
License:

Contacts:
👤


Emails: 
