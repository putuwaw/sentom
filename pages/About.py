import streamlit as st


st.header("Sentom")
st.write('''
            Sentom is a simple web application that allows you to do topic modeling on sentiment. 
            This application was created in order to join the Streamlit Summit Hackaton.
        ''')

st.subheader("Tech Stack")
st.write("The following tech stack was used to build this app:")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/streamlit.png")
    st.markdown("###### [Streamlit](https://streamlit.io/)")

with col2:
    st.image("images/snowflake.png")
    st.markdown("###### [Snowflake](https://snowflake.com/)")

with col3:
    st.image("images/bertopic.png")
    st.markdown("###### [BERTopic](https://www.google.com)")


st.subheader("Source Code")
st.write(
    "The source code for this app can be found [here](https://github.com/putuwaw/sentom).")
