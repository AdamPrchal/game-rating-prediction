import pandas as pd
import nltk
import string
import matplotlib

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

matplotlib.use('TkAgg')


nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

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

#funkce pro vizualizaci dat pomocí word cloud (slovní mraky)
def plot_word_cloud(text, title):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(title)
    plt.axis('off')
    plt.show()


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


# Předzpracování recenzí pomocí funkce preprocess_text()
top_game_reviews['cleaned_review'] = top_game_reviews['review'].apply(preprocess_text)
worst_game_reviews['cleaned_review'] = worst_game_reviews['review'].apply(preprocess_text)

## Výpis předzpracovaných dat
#print("\nPreprocessed Top Game Reviews:")
#print(top_game_reviews[['review', 'cleaned_review']].head())
#print("\nPreprocessed Worst Game Reviews:")
#print(worst_game_reviews[['review', 'cleaned_review']].head())


# Spojení všech recenzí do jednoho velkého textu, jednotlivé recenze jsou odděleny mezerou
top_reviews_text = ' '.join(top_game_reviews['cleaned_review'])
worst_reviews_text = ' '.join(worst_game_reviews['cleaned_review'])

# Vykreslení grafu word clouds
plot_word_cloud(top_reviews_text, 'Top Game Reviews Word Cloud')
plot_word_cloud(worst_reviews_text, 'Worst Game Reviews Word Cloud')

