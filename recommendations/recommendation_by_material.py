# Generate recommendation using Material column
import mysql.connector
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_similar_products_mats(input_material, input_brand, input_source):
    is_jawsdb = True
    # Connect to MySQL
    if is_jawsdb:
        # Connect to JawsDB
        db_connection = mysql.connector.connect(
            host="dt3bgg3gu6nqye5f.cbetxkdyhwsb.us-east-1.rds.amazonaws.com",
            user="nxniqxcq5s01amgv",
            password="i0wsjo662673p490",
            database="oy8070wbdpo6vn6u"
        )
    else:
        # Connect to local database
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="19752518M",
            database="web_project"  
        )
    cursor = db_connection.cursor()
    
    # Use SQL command to find recommendation products based on the input material from views.py
    if input_source == 'product_page':
        # If the request is from the men's product page
        query = f"SELECT product_id, type1, type2, brand, material, description, productName, productImage, price, rating FROM hello_shoefeatures WHERE material = '{input_material}' AND brand <> '{input_brand}'"
    else:
        # If the request is from the women's product page
        query = f"SELECT product_id, type1, type2, brand, material, description, productName, productImage, price, rating FROM hello_womenshoefeatures WHERE material = '{input_material}'  AND brand <> '{input_brand}'"
    
    # Execute the SQL command
    cursor.execute(query)
    
    # Fetch the query table
    shoe_data = cursor.fetchall()
    
    # Find similarity between input material and query table using the recommend_products_mats function
    recommendations = recommend_products_mats(input_material, shoe_data)
    
    cursor.close()
    
    # Close the connection
    db_connection.close()
    
    # Return product items and similarity scores
    return recommendations

# Find similarity between input material and query table
def recommend_products_mats(input_material, shoe_data):
    # Extract description column by iterating over columns in the query table
    descriptions = [row[5] for row in shoe_data]
    
    # Use TF-IDF Vectorizer to generate the matrix of word frequencies in the description column
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(descriptions)

    input_idx = None

    # Since we are using material, there is no input_material to find an index for

    similarity_scores = []

    for i, shoe_features_column in enumerate(shoe_data):
        product_id = shoe_features_column[0]
        type1 = shoe_features_column[1]
        type2 = shoe_features_column[2]
        brand = shoe_features_column[3]
        product_image = shoe_features_column[4]
        material = shoe_features_column[5]  
        description = shoe_features_column[6]
        product_image = shoe_features_column[7]
        price = shoe_features_column[8]
        rating = shoe_features_column[9]

        # Calculate the similarity score between input material and the material of the current product
        similarity_score = calculate_similarity_score(tfidf_matrix.getrow(0), tfidf_matrix.getrow(i))
        similarity_scores.append((shoe_features_column, similarity_score))
    
    # Sort the recommendations by similarity score in descending order
    sorted_recommendations = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    
    # Limit the number of recommendations to 4
    top_4_recommendations = [(rec[0], rec[1]) for rec in sorted_recommendations[:4]]
    
    return top_4_recommendations

def calculate_similarity_score(input_vector, product_vector):
    dot_product = np.dot(input_vector.toarray(), product_vector.toarray().T)
    magnitude_input_brand = np.linalg.norm(input_vector.toarray())
    magnitude_product = np.linalg.norm(product_vector.toarray())

    cosine_similarity = dot_product / (magnitude_input_brand * magnitude_product)

    return cosine_similarity
