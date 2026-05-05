import pandas as pd
import os

def clean_data(input_path, output_path):
    # 1. Load the dataset
    print(f"Loading data from: {input_path}")
    df = pd.read_csv(input_path)
    
    # 2. Basic Cleaning
    columns_to_keep = ['product_name', 'review_text', 'rating'] 
    
    # Check if columns exist before filtering
    existing_cols = [col for col in columns_to_keep if col in df.columns]
    df = df[existing_cols]
    
    # 3. Handling Missing Values
    df = df.dropna(subset=['review_text'])
    
    # 4. Text Normalization
    df['review_text'] = df['review_text'].str.lower().str.replace('[^\w\s]', '', regex=True)
    
    # 5. Save the cleaned data
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to: {output_path}")

if __name__ == "__main__":
    input_file = "data/raw/reviews_0-250.csv"
    output_file = "data/processed/cleaned_sephora_reviews.csv"
    
    clean_data(input_file, output_file)