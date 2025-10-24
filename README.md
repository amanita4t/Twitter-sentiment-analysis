Twitter Sentiment Analysis
 Overview

This project analyzes public tweets in real-time to determine their sentiment polarity (positive, negative, or neutral) and subjectivity using the TextBlob library. The results are stored in a structured CSV file for further data exploration and visualization.

It leverages the Twitter API v2 to fetch tweets containing specific keywords and applies natural language processing techniques to extract meaningful insights from user opinions.

Features

- Fetches live tweets using Twitter API v2.

- Cleans and processes tweet text for analysis.

- Computes:
    Polarity → sentiment score between -1.0 (negative) and 1.0 (positive).
    Subjectivity → score between 0.0 (objective) and 1.0 (subjective).

- Stores results in a well-organized CSV file with: Index, Tweet content, Polarity, Subjectivity
- Easily customizable for any keyword or hashtag.

Tech Stack

- Python 3.10+

- Tweepy – for accessing the Twitter API.

- TextBlob – for NLP sentiment analysis.

- Pandas – for data handling and CSV export.

Setup & Installation

    1 Clone the repository

    git clone https://github.com/yourusername/Twitter-Sentiment-Analysis.git
    cd Twitter-Sentiment-Analysis

    2 Create a virtual environment

    python -m venv .venv
    source .venv/bin/activate   # On macOS/Linux
    .venv\Scripts\activate      # On Windows

    3. Install dependencies

    pip install -r requirements.txt

    4 Set up your Twitter API credentials

    Create a .env file in the project root and add:
    BEARER_TOKEN=your_twitter_api_v2_bearer_token

    5 Run the analysis

    python main.py
