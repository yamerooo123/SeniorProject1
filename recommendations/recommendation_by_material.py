
import mysql.connector #fetching table
import numpy as np#similarity calculation
from sklearn.feature_extraction.text import TfidfVectorizer#extract meaningful words
from sklearn.metrics.pairwise import cosine_similarity#cosine similarity lib
from nltk.corpus import stopwords#preprocess data
import string

#load NLTK stop words
stop_words = set(stopwords.words('english'))

#preprocess process
def preprocess_text(text):
    text = ''.join([char for char in text if char not in string.punctuation])
    text = text.lower()
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text

#get similar prod. using material col
def get_similar_products_mats(input_material):
    #if in development sets False, while deploying sets True
    is_jawsdb = True
    #connect to JawsDB
    if is_jawsdb:
        db_connection = mysql.connector.connect(
            host="dt3bgg3gu6nqye5f.cbetxkdyhwsb.us-east-1.rds.amazonaws.com",
            user="nxniqxcq5s01amgv",
            password="i0wsjo662673p490",
            database="oy8070wbdpo6vn6u"
        )
    else:
        #Connect to local database port:80
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="19752518M",
            database="web_project"  
        )
    cursor = db_connection.cursor()
    #SQL command
    query = f"SELECT type1, type2, brand, material, description, productName, productImage, price, rating FROM hello_shoefeatures WHERE material = '{input_material}' AND rating > 4"
    #retrieve queryset table
    cursor.execute(query)
    #Store fecthed queryset table in the variable
    shoe_data = cursor.fetchall()

    cursor.close()
    #exit DB
    db_connection.close()
    
    #clean data in desc col 
    descriptions = [preprocess_text(row[4]) for row in shoe_data]
    
    #Create metrix using TFID and extract words from desc col
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(descriptions)

    input_idx = None

    #loop over col to find mats col
    for i, shoe_features_column in enumerate(shoe_data):
        if shoe_features_column[3] == input_material:
            input_idx = i
            break
    #if none case
    if input_idx is None:
        raise ValueError("Input material not found in shoe data")
    
    similarity_scores = []

    for i, shoe_features_column in enumerate(shoe_data):
        type1 = shoe_features_column[0]
        type2 = shoe_features_column[1]
        brand = shoe_features_column[2]
        product_image = shoe_features_column[3] 
        material = shoe_features_column[4]
        description = shoe_features_column[5]
        product_image = shoe_features_column[6]
        price = shoe_features_column[7]
        rating = shoe_features_column[8]
        #calculate sim score using COSINE
        similarity_score = calculate_similarity_score(tfidf_matrix.getrow(input_idx), tfidf_matrix.getrow(i))
        
        #check if the current product is the same as the input product nd exclude it
        if i != input_idx:
            similarity_scores.append((shoe_features_column, similarity_score))
    
    #sort rec list from highest to lowest sim score
    sorted_recommendations = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    
    #find top 4 matched prod.
    top_4_recommendations = [rec[0] for rec in sorted_recommendations[:4]]
    
    return top_4_recommendations

#sim score calculation logic
def calculate_similarity_score(input_vector, product_vector):
    #dot prod formula
    dot_product = np.dot(input_vector.toarray(), product_vector.toarray().T)
    magnitude_input_material = np.linalg.norm(input_vector.toarray())
    magnitude_product = np.linalg.norm(product_vector.toarray())

    cosine_similarity = dot_product / (magnitude_input_material * magnitude_product)

    return cosine_similarity
