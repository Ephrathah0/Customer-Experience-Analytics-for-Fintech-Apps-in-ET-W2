# Bank Reviews Scraper

## Methodology
- Scraped reviews, ratings, dates, and app names for three banks using `google-play-scraper`.
- Targeted at least 400 reviews per bank (1200+ total).
- Preprocessed:
  - Removed duplicates
  - Normalized dates (YYYY-MM-DD)
- Saved as CSV with columns: review, rating, date, bank, source