import pandas as pd
from textblob import TextBlob
import os

def analyze_sentiment(input_path, output_path):
    # 1. Loading Processed data
    print(f"Analyzing sentiment for: {input_path}")
    df = pd.read_csv(input_path)
    
    # 2. Sentiment Function
    # TextBlob polarity gives score (-1 to 1)
    def get_sentiment(text):
        analysis = TextBlob(str(text))
        if analysis.sentiment.polarity > 0:
            return 'Positive'
        elif analysis.sentiment.polarity == 0:
            return 'Neutral'
        else:
            return 'Negative'
    
    # 3. Apply Sentiment Analysis
    df['sentiment'] = df['review_text'].apply(get_sentiment)
    
    # 4. Checking Results
    print("\nSentiment Distribution:")
    print(df['sentiment'].value_counts())
    
    # 5. Saving results
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"\nAnalyzed data saved to: {output_path}")

if __name__ == "__main__":
    input_file = "data/processed/cleaned_sephora_reviews.csv"
    output_file = "data/processed/analyzed_sephora_reviews.csv"
    
    analyze_sentiment(input_file, output_file)