#Generate recommendation using Wishlist and Rating columns
import mysql.connector
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#generate recommendation using product brand
def get_similar_products(input_rating, input_wishlist, input_source):
    is_jawsdb = True
    #connect to mysql
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
    #use SQL commeand to find gender(type1), category(type2), brand, material and description based on the input brand from views.py
    if input_source == 'product_page':
        #if the request is from men product page
        query = f"SELECT product_id, type1, type2, brand, material, description, productName, productImage, price, rating FROM hello_shoefeatures WHERE brand = '{input_wishlist}' AND material = '{input_rating}'"
    else:
        #if the request is from women product page
        query = f"SELECT product_id, type1, type2, brand, material, description, productName, productImage, price, rating FROM hello_womenshoefeatures WHERE brand = '{input_wishlist}' AND material = '{input_rating}'"
    #execute the SQL command
    cursor.execute(query)
    #show the query table using fetchall
    shoe_data = cursor.fetchall()

    cursor.close()
    #close the connection
    db_connection.close()
    #find similarity between input brand and query table using recommend_products function
    recommendations = recommend_products(input_rating, input_wishlist, shoe_data)
    #return results
    return recommendations
#find similarity between input brand and query table
def recommend_products(input_brand, input_material, shoe_data):
    # Extract description column by iterating over columns in the query table
    descriptions = [row[5] for row in shoe_data]
    
    # Use TF-IDF Vectorizer to generate the matrix of word frequencies in the description column
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(descriptions)

    input_idx = None

    for i, shoe_features_column in enumerate(shoe_data):
        if shoe_features_column[3] == input_brand:
            input_idx = i
            break 

    if input_idx is None:
        raise ValueError("Input brand not found in shoe data")
    
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

        #Calculate the similarity score between input product and current product
        similarity_score = calculate_similarity_score(tfidf_matrix.getrow(input_idx), tfidf_matrix.getrow(i))
        
        #Check if the current product is the same as the input product, and exclude it
        if i != input_idx:
            similarity_scores.append((shoe_features_column, similarity_score))
    
    #Sort the recommendations by similarity score in descending order
    sorted_recommendations = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    
    #Limit the number of recommendations to 4, excluding the input product
    top_4_recommendations = [rec[0] for rec in sorted_recommendations[:4]]
    
    return top_4_recommendations

def calculate_similarity_score(input_vector, product_vector):
    dot_product = np.dot(input_vector.toarray(), product_vector.toarray().T)
    magnitude_input_brand = np.linalg.norm(input_vector.toarray())
    magnitude_product = np.linalg.norm(product_vector.toarray())

    cosine_similarity = dot_product / (magnitude_input_brand * magnitude_product)

    return cosine_similarity
