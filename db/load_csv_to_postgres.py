import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://USERNAME:PASSWORD@localhost:5432/DATABASE_NAME"
)

df = pd.read_csv("../sentiment_analysis/reviews_with_sentiment.csv")

df.to_sql("reviews", engine, if_exists="replace", index=False)

print("✅ CSV uploaded successfully to Postgres!") 

