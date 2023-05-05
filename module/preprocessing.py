import pandas as pd
import string
import nltk

try:
    stopwords = set(nltk.corpus.stopwords.words("english"))
    lemmatizer = nltk.stem.WordNetLemmatizer()
except LookupError:
    nltk.download("stopwords")
    nltk.download("wordnet")
    stopwords = set(nltk.corpus.stopwords.words("english"))
    lemmatizer = nltk.stem.WordNetLemmatizer()


def case_folding(df: pd.DataFrame) -> pd.DataFrame:
    return df['TEXT'].str.lower()


def punctuation_removal(df: pd.DataFrame) -> pd.DataFrame:
    return df['TEXT'].str.translate(str.maketrans('', '', string.punctuation))


def number_removal(df: pd.DataFrame) -> pd.DataFrame:
    return df['TEXT'].str.replace('\d+', '', regex=True)


def stopword_removal(df: pd.DataFrame) -> pd.DataFrame:
    return df['TEXT'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stopwords)]))


def lemmatization(df: pd.DataFrame) -> pd.DataFrame:
    return df['TEXT'].apply(lambda x: ' '.join([lemmatizer.lemmatize(word) for word in x.split()]))


def preprocess(df: pd.DataFrame) -> list:
    # drop null values
    df.dropna(inplace=True)

    # case folding
    df['TEXT'] = case_folding(df)

    # punctuation removal
    df['TEXT'] = punctuation_removal(df)

    # number removal
    df['TEXT'] = number_removal(df)

    # stopword removal
    df['TEXT'] = stopword_removal(df)

    # lemmatization
    df['TEXT'] = lemmatization(df)

    return df['TEXT'].tolist()
