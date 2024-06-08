import pandas as pd
import nltk
import string
import matplotlib
import matplotlib.pyplot as plt


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams

from collections import Counter
from wordcloud import WordCloud


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline


matplotlib.use('TkAgg')


#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('wordnet')


stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

#proměnná pro počet uníkátních slov při vykreslení grafu word-cloud
number_of_unique_words=100

#funkce na předzpracování textu
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

#funkce pro vytvoření slovníku
def build_word_frequency(texts):
    all_words = ' '.join(texts).split()
    word_freq = Counter(all_words)
    return word_freq

#funkce pro vytvoření grafu Zipova zákona
def plot_zipf(word_freq):
    freqs = [freq for word, freq in word_freq.most_common()]
    ranks = range(1, len(freqs) + 1)
    plt.figure(figsize=(10, 6))
    plt.plot(ranks, freqs)
    plt.yscale('log')
    plt.xscale('linear')
    plt.title('Zipf\'s Law')
    plt.xlabel('Rank')
    plt.ylabel('Frequency')
    plt.show()

#funkce pro generování n-gramu
def generate_ngrams(text, n):
    words = text.split()
    return list(ngrams(words, n))

def build_ngram_frequency(texts, n):
    all_ngrams = []
    for text in texts:
        n_grams = generate_ngrams(text, n)
        all_ngrams.extend(n_grams)
    ngram_freq = Counter(all_ngrams)
    return ngram_freq

#funkce pro vizualizaci dat pomocí grafu word cloud (slovní mraky)
def plot_word_cloud(word_freq, title, max_words=None):
    wordcloud = WordCloud(width=800, height=400, background_color='white', max_words=max_words)
    wordcloud.generate_from_frequencies(dict(word_freq))
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(title)
    plt.axis('off')
    plt.show()

# Kontrola frekvence slov a odstranění duplicit
def get_most_common_words(text, max_words):
    words = text.split()
    word_counts = Counter(words)
    most_common_words = word_counts.most_common(max_words)
    return ' '.join([word for word, _ in most_common_words])

def get_most_common_words(texts, max_words=None):
    all_text = ' '.join(texts)
    words = all_text.split()
    most_common_words = Counter(words).most_common(max_words)
    return most_common_words

#načtení dat
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


#print("\nMerged Top Game Reviews:")
#print(top_game_reviews.head())
#print("\nMerged Worst Game Reviews:")
#print(worst_game_reviews.head())


# Předzpracování recenzí pomocí funkce preprocess_text()
top_game_reviews['cleaned_review'] = top_game_reviews['review'].apply(preprocess_text)
worst_game_reviews['cleaned_review'] = worst_game_reviews['review'].apply(preprocess_text)


#print("\nPreprocessed Top Game Reviews:")
#print(top_game_reviews[['review', 'cleaned_review']].head())
#print("\nPreprocessed Worst Game Reviews:")
#print(worst_game_reviews[['review', 'cleaned_review']].head())


# Spojení všech recenzí do jednoho velkého textu, jednotlivé recenze jsou odděleny mezerou
top_reviews_text = ' '.join(top_game_reviews['cleaned_review'])
worst_reviews_text = ' '.join(worst_game_reviews['cleaned_review'])

## Vykreslení grafu word clouds
#plot_word_cloud(top_reviews_text, 'Top Game Reviews Word Cloud')
#plot_word_cloud(worst_reviews_text, 'Worst Game Reviews Word Cloud')

top_words = top_reviews_text.split()
worst_words = worst_reviews_text.split()

top_word_counts = Counter(top_words)
worst_word_counts = Counter(worst_words)

# Zobrazení 10 (xx) nejčastějších slov
#print("Top 10 words in top game reviews:", top_word_counts.most_common(10))
#print("Top 10 words in worst game reviews:", worst_word_counts.most_common(10))

#plot_word_cloud(' '.join(top_words), 'Top Game Reviews Word Cloud')
#plot_word_cloud(' '.join(worst_words), 'Worst Game Reviews Word Cloud')


# Kombinace textů
all_reviews_text = pd.concat([top_game_reviews['cleaned_review'], worst_game_reviews['cleaned_review']])

# Vytvoření slovníku frekvence slov
word_freq = build_word_frequency(all_reviews_text)
print("100 most frequency words (word, frequency):\n", word_freq.most_common(100))  # Zobrazení 10 nejčastějších slov

#Vytvoření grafu Zipova zákona:
plot_zipf(word_freq)

#proměnná pro počet n-gramů
number_of_ngram = 100

# Filtrace prázdných recenzí
top_game_reviews = top_game_reviews[top_game_reviews['cleaned_review'].str.strip() != '']
worst_game_reviews = worst_game_reviews[worst_game_reviews['cleaned_review'].str.strip() != '']

# Předzpracované texty pro nejlepší recenze
best_reviews_text = top_game_reviews['cleaned_review'].tolist()
worst_reviews_text = worst_game_reviews['cleaned_review'].tolist()

# Vytvoření frekvenčních slovníků pro bigramy a trigramy pro nejlepší recenze
best_bigram_freq = build_ngram_frequency(best_reviews_text, 2)
best_trigram_freq = build_ngram_frequency(best_reviews_text, 3)

# Zobrazení 10 nejčastějších bigramů a trigramů pro nejlepší recenze
print("Top 10 Bigrams in Best Reviews:", best_bigram_freq.most_common(number_of_ngram))
print("Top 10 Trigrams in Best Reviews:", best_trigram_freq.most_common(number_of_ngram))

# Vytvoření frekvenčních slovníků pro bigramy a trigramy pro nejhorší recenze
worst_bigram_freq = build_ngram_frequency(worst_reviews_text, 2)
worst_trigram_freq = build_ngram_frequency(worst_reviews_text, 3)

# Zobrazení 10 nejčastějších bigramů a trigramů pro nejhorší recenze
print("Top 10 Bigrams in Worst Reviews:", worst_bigram_freq.most_common(number_of_ngram))
print("Top 10 Trigrams in Worst Reviews:", worst_trigram_freq.most_common(number_of_ngram))


# Vytvoření frekvenčních slovníků pro bigramy a trigramy pro všechny recenze
all_bigram_freq = build_ngram_frequency(all_reviews_text, 2)
all_trigram_freq = build_ngram_frequency(all_reviews_text, 3)

# Zobrazení 10 nejčastějších bigramů a trigramů pro všechny recenze
print("Top 100 Bigrams in All Reviews:", all_bigram_freq.most_common(number_of_ngram))
print("Top 100 Trigrams in All Reviews:", all_trigram_freq.most_common(number_of_ngram))

# Vytvoření seznamů nejčastějších slov pro nejlepší a nejhorší recenze
best_reviews_common_text = get_most_common_words(best_reviews_text, max_words=number_of_unique_words)
worst_reviews_common_text = get_most_common_words(worst_reviews_text, max_words=number_of_unique_words)

# Zobrazení nejčastějších slov
print("Most common words in best reviews:", best_reviews_common_text)
print("Most common words in worst reviews:", worst_reviews_common_text)

# Generování a zobrazení word cloud
plot_word_cloud(best_reviews_common_text, 'Top Game Reviews Word Cloud', max_words=number_of_unique_words)
plot_word_cloud(worst_reviews_common_text, 'Worst Game Reviews Word Cloud', max_words=number_of_unique_words)




#Implementace bag of Words (BoW)

# Přidání sentimentálních štítků (1 pro pozitivní, 0 pro negativní)
top_game_reviews['sentiment'] = 1
worst_game_reviews['sentiment'] = 0

# Kombinace dat
all_reviews = pd.concat([top_game_reviews, worst_game_reviews])
X = all_reviews['cleaned_review']
y = all_reviews['sentiment']

# Bag-of-Words model

# Zvýšení počtu iterací pro logistickou regresi
#POZNÁMKA - bez použití max_iter_value byla hodnota Accuracy 0.8974, po přidání se zvýšila na 0.91084
# při testování jsem zjistil že bude stačit hodnota 2000, skutečný počet iterací byl cca 1963
max_iter_value = 2000


bow_vectorizer = CountVectorizer(max_features=5000)  # Omezte na top 5000 slov
X_bow = bow_vectorizer.fit_transform(X)

# Rozdělení dat na trénovací a testovací sadu
X_train_bow, X_test_bow, y_train, y_test = train_test_split(X_bow, y, test_size=0.2, random_state=42)

# Trénink modelu s BoW
model_bow = LogisticRegression(max_iter=max_iter_value)
model_bow.fit(X_train_bow, y_train)

# Predikce a vyhodnocení
y_pred_bow = model_bow.predict(X_test_bow)
accuracy_bow = accuracy_score(y_test, y_pred_bow)

print("Accuracy with BoW:", accuracy_bow)


# Trénink modelu s BoW a škálováním
pipeline_bow = make_pipeline(StandardScaler(with_mean=False), LogisticRegression(max_iter=max_iter_value))
pipeline_bow.fit(X_train_bow, y_train)

# Predikce a vyhodnocení
y_pred_bow = pipeline_bow.predict(X_test_bow)
accuracy_bow = accuracy_score(y_test, y_pred_bow)
n_iter_bow = pipeline_bow.named_steps['logisticregression'].n_iter_[0]

print("Accuracy with BoW and StandardScaler:", accuracy_bow)
print("Number of iterations for BoW:", n_iter_bow)


#TF-IDF Model
#testování TF-IDF modelu při stejném počtu iterací
max_iter_value=2000
tfidf_vectorizer = TfidfVectorizer(max_features=5000)  # Omezte na top 5000 slov
X_tfidf = tfidf_vectorizer.fit_transform(X)

# Rozdělení dat na trénovací a testovací sadu
X_train_tfidf, X_test_tfidf, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

# Trénink modelu s TF-IDF bez škálování
model_tfidf_no_scaling = LogisticRegression(max_iter=max_iter_value)
model_tfidf_no_scaling.fit(X_train_tfidf, y_train)

# Predikce a vyhodnocení
y_pred_tfidf_no_scaling = model_tfidf_no_scaling.predict(X_test_tfidf)
accuracy_tfidf_no_scaling = accuracy_score(y_test, y_pred_tfidf_no_scaling)
print("Accuracy with TF-IDF without StandardScaler:", accuracy_tfidf_no_scaling)

# Trénink modelu s TF-IDF a škálováním
pipeline_tfidf = make_pipeline(StandardScaler(with_mean=False), LogisticRegression(max_iter=max_iter_value))
pipeline_tfidf.fit(X_train_tfidf, y_train)

# Predikce a vyhodnocení
y_pred_tfidf = pipeline_tfidf.predict(X_test_tfidf)
accuracy_tfidf = accuracy_score(y_test, y_pred_tfidf)
print("Accuracy with TF-IDF and StandardScaler:", accuracy_tfidf)
