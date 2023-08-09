import mysql.connector
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#generate recommendation using product brand
def get_similar_products(input_brand, input_material):
    #connect to mysql
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="19752518M",
        database="web_project"  
    )
    cursor = db_connection.cursor()
    #use SQL commeand to find gender(type1), category(type2), brand, material and description based on the input brand from views.py
    query = f"SELECT type1, type2, brand, material, description FROM hello_shoefeatures WHERE brand = '{input_brand}' AND material = '{input_material}'"
    #execute the SQL command
    cursor.execute(query)
    #show the quert table using fetchall
    shoe_data = cursor.fetchall()

    cursor.close()
    #close the connection
    db_connection.close()
    #find similarity between input brand and query table using recommend_products function
    recommendations = recommend_products(input_brand, input_material, shoe_data)
    #return results
    return recommendations
#find similarity between input brand and query table
def recommend_products(input_brand,input_material,shoe_data):
    #extract description columan by iterating over column in query table 
    descriptions = [row[4] for row in shoe_data]
    #use TFIDF Vectorizer to generate the matrix frequent word count in description column
    vectorizer = TfidfVectorizer()
    #generate frequent word matrix
    tfidf_matrix = vectorizer.fit_transform(descriptions)

    input_idx = None

    for i, shoe_features_column in enumerate(shoe_data):
        if shoe_features_column[2] == input_brand:
            input_idx = i
            break  # Move the break statement inside the if block

    if input_idx is None:
        raise ValueError("Input brand not found in shoe data")
    
    similarity_scores = []  # List to store similarity scores

    for i, shoe_features_column in enumerate(shoe_data):
        type1 = shoe_features_column[0]
        type2 = shoe_features_column[1]
        brand = shoe_features_column[2]
        material = shoe_features_column[3]

        similarity_score = calculate_similarity_score(tfidf_matrix.getrow(input_idx), tfidf_matrix.getrow(i))
        similarity_scores.append((shoe_features_column, similarity_score))
    
    # Sort the recommendations by similarity score in descending order
    sorted_recommendations = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    
    top_5_recommendations = [rec[0] for rec in sorted_recommendations[:5]]
    
    return top_5_recommendations

def calculate_similarity_score(input_vector, product_vector):
    dot_product = np.dot(input_vector.toarray(), product_vector.toarray().T)
    magnitude_input_brand = np.linalg.norm(input_vector.toarray())
    magnitude_product = np.linalg.norm(product_vector.toarray())

    cosine_similarity = dot_product / (magnitude_input_brand * magnitude_product)

    return cosine_similarity
