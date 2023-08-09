import pymysql
import math

import main

# Connect to MySQL
db_connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="amharic_documents"
)
cursor = db_connection.cursor()

# Sample user query (replace with user input)
user_query = "በየዓመቱ የሚያዘጋጀው"

# Stemmer function (replace with your actual stemmer logic)
def stemmer(text):
    return text  # Replace with your stemmer logic

# Preprocess user query
query_words = user_query.lower().split()
stemmed_query = [main.stemmer(word) for word in query_words]

# Get document count
cursor.execute("SELECT COUNT(*) FROM amharic_documents")
total_documents = cursor.fetchone()[0]

# Calculate TF-IDF for query terms
tf_idf_query = {}
for term in stemmed_query:
    cursor.execute("SELECT document_id, tf, idf FROM inverted_index WHERE word = %s", (term,))
    result = cursor.fetchone()
    if result:
        doc_id, tf, idf = result
        tf_idf_query[doc_id] = tf * idf

# Calculate cosine similarity and rank documents
results = []
for doc_id in range(1, total_documents + 1):
    cursor.execute("SELECT article FROM amharic_documents WHERE id = %s", (doc_id,))
    document = cursor.fetchone()[0]

    tf_idf_vector = []
    for term in stemmed_query:
        cursor.execute("SELECT tf, idf FROM inverted_index WHERE word = %s AND document_id = %s", (term, doc_id))
        result = cursor.fetchone()
        if result:
            tf, idf = result
            tf_idf_vector.append(tf * idf)
        else:
            tf_idf_vector.append(0)

    # Calculate cosine similarity
    dot_product = sum(a * b for a, b in zip(tf_idf_vector, tf_idf_query.values()))
    norm_query = math.sqrt(sum(val ** 2 for val in tf_idf_query.values()))
    norm_doc = math.sqrt(sum(val ** 2 for val in tf_idf_vector))
    cosine_similarity = dot_product / (max(norm_query * norm_doc, 1e-10))  # Avoid division by zero

    results.append((doc_id, cosine_similarity))

# Sort and display top 25 results
results.sort(key=lambda x: x[1], reverse=True)
top_25_results = results[:25]
for rank, (doc_id, similarity) in enumerate(top_25_results, start=1):
    cursor.execute("SELECT article FROM amharic_documents WHERE id = %s", (doc_id,))
    document = cursor.fetchone()[0]

    # Print debugging information
    print(f"Rank {rank}: Document {doc_id} (Cosine Similarity: {similarity:.4f})")
    print(f"Dot Product: {dot_product}")
    print(f"Norm Query: {norm_query}")
    print(f"Norm Document: {norm_doc}")

    print(document)
    print('=' * 40)

# Close the database connection
cursor.close()
db_connection.close()
