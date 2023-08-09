import pymysql
import math

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

# Populate Inverted Index and Calculate df (document frequency)
word_df = {}  # Dictionary to store the document frequency for each word
for doc_id, document in amharic_documents:
    # Preprocess the document (e.g., remove non-textual content, tokenize)
    words = document.split()

    # Update the inverted index and calculate df
    for word in set(words):  # Use set() to avoid duplicate counts
        if word in inverted_index:
            inverted_index[word].append((doc_id, words.count(word)))
        else:
            inverted_index[word] = [(doc_id, words.count(word))]

        # Update df for the word
        word_df[word] = word_df.get(word, 0) + 1

# Calculate idf
total_documents = len(amharic_documents)
word_idf = {word: math.log(total_documents / (df + 1)) for word, df in word_df.items()}

# Calculate tf_idf and Update the inverted index table
# ... (previous code)

# Calculate tf_idf and Update the inverted index table
for word, postings in inverted_index.items():
    idf = word_idf[word]  # Retrieve idf for the word

    for doc_id, word_freq in postings:
        # Calculate term frequency (tf)
        total_words_in_doc = len(amharic_documents[doc_id - 1][1].split())
        tf = word_freq / total_words_in_doc

        # Calculate term frequency-inverse document frequency (tf_idf)
        tf_idf = tf * idf

        # Update the inverted index table with tf and tf_idf values
        update_query = "UPDATE inverted_index SET tf = %s, idf = %s, tf_idf = %s WHERE word = %s AND document_id = %s"
        cursor.execute(update_query, (tf, idf, tf_idf, word, doc_id))
        db_connection.commit()

        # Print the calculated values for verification
        print(f"Word: {word}, Document ID: {doc_id}, tf: {tf}, idf: {idf}, tf_idf: {tf_idf}")

# Close the database connection
cursor.close()
db_connection.close()
