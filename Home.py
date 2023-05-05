import streamlit as st
from module import preprocessing
from bertopic import BERTopic
import pandas as pd

conn = st.experimental_connection('snowpark')


@st.cache_data
def get_pros_sentiment():
    df_pros = conn.query(
        'SELECT REVIEW_PROS AS text FROM revelio_sentiment_individual_reviews LIMIT 100;', ttl=600)
    return df_pros


@st.cache_data
def get_cons_sentiment():
    df_cons = conn.query(
        'SELECT REVIEW_CONS AS text FROM revelio_sentiment_individual_reviews LIMIT 100;', ttl=600)
    return df_cons


def preprocess(df: pd.DataFrame) -> list:
    return preprocessing.preprocess(df)


@st.cache_data
def create_pros_model(document):
    topic_model = BERTopic(
        language="english", calculate_probabilities=True, verbose=True)
    topics, probs = topic_model.fit_transform(document)
    return topic_model


@st.cache_data
def create_cons_model(document):
    topic_model = BERTopic(
        language="english", calculate_probabilities=True, verbose=True)
    topics, probs = topic_model.fit_transform(document)
    return topic_model


st.header("Topic Modeling from Sentiment")
st.write("This is a simple example of using BERTopic to perform topic modeling on a dataset of sentiment reviews.")

pros, cons = st.tabs(["Pros", "Cons"])
with pros:
    df_pros = get_pros_sentiment()
    st.markdown("##### Dataset preview")
    st.write(df_pros.head(5))
    df_pros = df_pros.head(100)
    df_pros = preprocess(df_pros)
    model_pros = create_pros_model(df_pros)
    st.markdown("##### Topic keywords")
    st.write("The following are the top 5 keywords for each topic:")
    st.plotly_chart(model_pros.visualize_barchart(top_n_topics=5))
    st.markdown("##### Summary")
    st.write("From the keywords above, we can see that the positive sentiment are about great work, company, and employee.")

with cons:
    df_cons = get_cons_sentiment()
    st.markdown("##### Dataset preview")
    st.write(df_cons.head(5))
    df_cons = df_cons.head(100)
    df_cons = preprocess(df_cons)
    model_cons = create_cons_model(df_cons)
    st.markdown("##### Topic keywords")
    st.write("The following are the top 5 keywords for each topic:")
    st.plotly_chart(model_cons.visualize_barchart(top_n_topics=5))
    st.markdown("##### Summary")
    st.write("From the keywords above, we can see that the negative sentiment are about work hour, pay, management, and staff.")
