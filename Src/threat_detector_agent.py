import pandas as pd
import os

def detect_threats(input_path, output_path):
    print(f"Scanning for threats in: {input_path}")
    df = pd.read_csv(input_path)
    
    # 1. Filtering Negative Results only
    negative_reviews = df[df['sentiment'] == 'Negative'].copy()
    
    # 2. Risk Keywords 
    threat_keywords = ['fake', 'worst', 'allergic', 'rash', 'expired', 'waste', 'broken', 'disappointing']
    
    def check_threat_level(text):
        text = str(text).lower()
        if any(word in text for word in threat_keywords):
            return 'High Risk'
        return 'Moderate Risk'
    
    negative_reviews['threat_level'] = negative_reviews['review_text'].apply(check_threat_level)
    
    # 3. Product-wise Grouping
    # To check in which products we have the most issues
    product_threats = negative_reviews[negative_reviews['threat_level'] == 'High Risk'].groupby('product_name').size().reset_index(name='threat_count')
    product_threats = product_threats.sort_values(by='threat_count', ascending=False)
    
    print("\nTop 5 High-Risk Products:")
    print(product_threats.head(5))
    
    # 4. Save the full threat report
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    negative_reviews.to_csv(output_path, index=False)
    
    #Saving a separate summary report for high-risk products
    summary_path = output_path.replace(".csv", "_summary.csv")
    product_threats.to_csv(summary_path, index=False)
    print(f"\nSummary report saved to: {summary_path}")

if __name__ == "__main__":
    input_file = "data/processed/analyzed_sephora_reviews.csv"
    output_file = "data/processed/threat_report.csv"
    detect_threats(input_file, output_file)