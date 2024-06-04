import pandas as pd
import nltk
import string


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    if isinstance(text, str):
        # Převod textu na malá písmena
        text = text.lower()
        # Odstranění interpunkce
        text = text.translate(str.maketrans('', '', string.punctuation))
        # Tokenizace
        words = word_tokenize(text)
        # Odstranění stop slov a lemmatizace
        words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
        return ' '.join(words)
    else:
        return ''



top_game_ids = pd.read_csv('./data/top_game_app_ids.csv')
top_game_reviews = pd.read_csv('./data/top_game_app_ids_normalized_reviews.csv')
worst_game_ids = pd.read_csv('./data/worst_game_app_ids.csv')
worst_game_reviews = pd.read_csv('./data/worst_game_app_ids_normalized_reviews.csv')


#print("Top Game IDs:")
#print(top_game_ids.head())
#print("\nTop Game Reviews:")
#print(top_game_reviews.head())
#print("\nWorst Game IDs:")
#print(worst_game_ids.head())
#print("\nWorst Game Reviews:")
#print(worst_game_reviews.head())


# Spojení top herních recenzí s názvy her
top_game_reviews = top_game_reviews.merge(top_game_ids, on='app_id', how='left')

# Spojení nejhorších herních recenzí s názvy her
worst_game_reviews = worst_game_reviews.merge(worst_game_ids, on='app_id', how='left')

# Kontrola výsledných datasetů
#print("\nMerged Top Game Reviews:")
#print(top_game_reviews.head())
#print("\nMerged Worst Game Reviews:")
#print(worst_game_reviews.head())


# Aplikace předzpracování na recenze
top_game_reviews['cleaned_review'] = top_game_reviews['review'].apply(preprocess_text)
worst_game_reviews['cleaned_review'] = worst_game_reviews['review'].apply(preprocess_text)

# Kontrola předzpracovaných dat
print("\nPreprocessed Top Game Reviews:")
print(top_game_reviews[['review', 'cleaned_review']].head())
print("\nPreprocessed Worst Game Reviews:")
print(worst_game_reviews[['review', 'cleaned_review']].head())

