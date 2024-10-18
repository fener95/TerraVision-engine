# app/cache_utils.py

import sqlite3
import json
from datetime import datetime, timedelta
from threading import Lock

# Create a lock for thread-safe database access
db_lock = Lock()

# Function to get a database connection per thread
def get_db_connection():
    conn = sqlite3.connect('metasearch.db', check_same_thread=False)
    return conn

# Initialize the cache table
def init_cache():
    with db_lock:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cache (
                query TEXT PRIMARY KEY,
                results TEXT,
                timestamp DATETIME
            )
        ''')
        conn.commit()
        conn.close()

# Check if the query is cached
def get_cached_results(query):
    with db_lock:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT results, timestamp FROM cache WHERE query=?", (query,))
        row = cursor.fetchone()
        conn.close()
    if row:
        timestamp = datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S')
        if timestamp > datetime.now() - timedelta(days=1):
            return json.loads(row[0])  # Return cached results
    return None

# Cache the query results
def cache_query_results(query, results):
    results_json = json.dumps(results)
    with db_lock:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO cache (query, results, timestamp) VALUES (?, ?, ?)",
                       (query, results_json, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        conn.commit()
        conn.close()
