# Customer-Experience-Analytics-for-Fintech-Apps-in-ET-W2
Customer Experience Analytics for Fintech Apps
Project Overview
This project analyzes user experiences of three fintech banking apps using Google Play reviews. The analysis includes sentiment evaluation, rating distributions, and thematic insights to understand customer satisfaction and key pain points.

Task 1: Web Scraping & Preprocessing
Objective:
- Collect user reviews, ratings, dates, and app names for three banks, preprocess the data, and save it as a clean CSV for analysis.

Methodology:
Web Scraping
-Used google-play-scraper to collect reviews from the Google Play store.
- Targeted minimum 400 reviews per bank (1,200 reviews total).
- Extracted review text, rating, review date, app name, and source.

Preprocessing
- Removed duplicate reviews.
- Handled missing data (<5% missing).
- Normalized dates to YYYY-MM-DD.
- Saved a clean CSV with columns: review, rating, date, bank, source.
  
Task 2: Sentiment Analysis & Ratings (In Progress)
Completed Work:
- Loaded the preprocessed CSV dataset.
- Conducted sentiment analysis on all reviews.
- Standardized sentiment labels (Positive, Negative) and mapped to numeric scores.
- Aggregated sentiment by bank and rating.
  
Generated visualizations for:
- Sentiment distribution across banks.
- Ratings per bank.

Usage Instructions
Clone the repository:
- git clone <your-repo-URL>

Install dependencies:
- pip install -r requirements.txt

Run the preprocessing script:
- python comp.py


Run sentiment analysis and visualization scripts as they become available.
