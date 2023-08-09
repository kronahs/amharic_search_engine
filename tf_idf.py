import pymysql
import main

# Connect to MySQL
db_connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="amharic_documents"
)
cursor = db_connection.cursor()

# Retrieve Amharic Documents
cursor.execute("SELECT id, article FROM amharic_documents")
amharic_documents = cursor.fetchall()

# Initialize Inverted Index
inverted_index = {}

# Process Amharic Documents and Build Inverted Index
for doc_id, document in amharic_documents:
    # Preprocess the document (e.g., remove non-textual content, tokenize)
    words = document.split()
    stemmed_words = main.stemmer(' '.join(words))

    # Update the inverted index
    for word in stemmed_words:
        if word in inverted_index:
            inverted_index[word].append((doc_id, stemmed_words.count(word)))
        else:
            inverted_index[word] = [(doc_id, stemmed_words.count(word))]

# Calculate the Document Frequency (DF) for each term (number of documents containing the term)
document_frequency = {word: len(postings) for word, postings in inverted_index.items()}

# Calculate the Total Number of Documents
total_documents = len(amharic_documents)

# Prepare data for updating the table with TF, IDF, and composite values
bulk_update_data = []

for word, postings in inverted_index.items():
    for doc_id, frequency in postings:
        tf = frequency / len(amharic_documents)  # Term Frequency
        idf = math.log(total_documents / (document_frequency[word] + 1))  # Inverse Document Frequency with smoothing
        composite = tf * idf  # Composite attribute

        # Append data for bulk update
        bulk_update_data.append((tf, idf, composite, word, doc_id))

print(f"Number of entries in inverted_index dictionary: {len(bulk_update_data)}")

# Update the Inverted Index Table with TF, IDF, and Composite Values (Bulk Update)
try:
    update_query = "UPDATE inverted_index SET tf=%s, idf=%s, tf_idf=%s WHERE word=%s AND document_id=%s"
    cursor.executemany(update_query, bulk_update_data)
    db_connection.commit()
    print(f"TF, IDF, and composite values updated for {cursor.rowcount} entries in the inverted_index table!")
except pymysql.Error as e:
    db_connection.rollback()  # Rollback the transaction in case of an error
    print(f"Error: {e}")

# Close the database connection
cursor.close()
db_connection.close()
