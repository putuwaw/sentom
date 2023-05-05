# sentom

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Snowflake](https://img.shields.io/badge/Snowflake-white?style=for-the-badge&logo=snowflake&logoColor=#2eb4e7)
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)

Sentom (sentiment-topic-modeling) is a simple web application that allows you to do topic modeling on sentiment review using BERTopic. This application is built using Streamlit and Snowflake.

## Features 💡

Using Sentom, you can:

- [x] Do topic modeling on sentiment review
- [x] See the top keywords for each topic

## Prerequisites 📋

- [Python 3.8](https://www.python.org/downloads/release/python-380/)
- [Streamlit](https://streamlit.io/)
- [BERTopic](https://github.com/MaartenGr/BERTopic)
- [Snowflake](https://www.snowflake.com/)

## Installation 🛠

- Clone the repository:

```bash
git clone https://github.com/putuwaw/sentom.git
```

- Install the requirements:

```bash
pip install -r requirements.txt
```

- Create `secret.toml` file in `.streamlit` folder and fill it with your Snowflake credentials. See [Documentation](https://docs.streamlit.io/knowledge-base/tutorials/databases/snowflake) for more information.

- Run the application:

```bash
streamlit run Home.py
```

## License 📝

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements 🙏

BERTopic is a topic modeling technique that leverages hugs transformers and c-TF-IDF to create dense clusters allowing for easily interpretable topics whilst keeping important words in the topic descriptions Thank you to the developers and contributors of this open-source tool. Learn more about BERTopic [here](https://github.com/MaartenGr/BERTopic).
