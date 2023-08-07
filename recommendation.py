import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
shoes_dataset = pd.read_csv('MachineLearning/Modified_Shoe_prices.csv')

# Choose columns to be used for recommendation
features = ['Brand', 'Type', 'Gender', 'Material']

# Remove rows with null values
for feature in features:
    shoes_dataset[feature] = shoes_dataset[feature].fillna('')

# Combine columns in features variable into one column
def combined_features(row):
    return row['Brand'] + " " + row['Type'] + " " + row['Gender'] + " " + row['Material']

shoes_dataset['combined_features'] = shoes_dataset.apply(combined_features, axis=1)

# Capture the null value
cv = CountVectorizer()
count_matrix = cv.fit_transform(shoes_dataset['combined_features'])

# Find similarity
cosine_sim = cosine_similarity(count_matrix)

# Search for similar shoes test
#shoes_input = "Reebok Classic Leather"

#get similar shoes using shoes input, similarity measure, dataset and top 10
def get_similar_shoes(shoes_input, cosine_sim, shoes_dataset, top_n=5):
    # Combine attributes from shoes_input into a single string
    combined_input = " ".join(shoes_input)

    # Find the index of the input shoe in the dataset
    search_results = shoes_dataset[shoes_dataset["combined_features"].str.contains(combined_input, case=False)].index

    if len(search_results) == 0:
        print("No matches found for:", combined_input)
        return []

    search_results = search_results[0]  # Get the first index value from the Index object
    output = list(enumerate(cosine_sim[search_results]))
    sorted_model_desc = sorted(output, key=lambda x: x[1], reverse=True)

    similar_shoes = []
    i = 0
    for shoes in sorted_model_desc:
        if shoes[0] != search_results:
            similar_shoes.append(shoes_dataset.loc[shoes[0], "Model"])
            i += 1
            if i >= top_n:
                break

    return similar_shoes

#Test
shoes_input = ['Lifestyle','WOmen','leather']
similar_shoes = get_similar_shoes(shoes_input, cosine_sim, shoes_dataset)
print(similar_shoes)