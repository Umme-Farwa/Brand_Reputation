import pandas as pd
import os
from deep_translator import GoogleTranslator
from langdetect import detect
from textblob import TextBlob



# 1. SENTIMENT ANALYSIS LOGIC

def get_sentiment_rating(text):

    try:

        if pd.isna(text) or len(str(text)) < 3:
            return 3

        analysis = TextBlob(str(text))

        polarity = analysis.sentiment.polarity

        # Convert polarity to 1-5 rating
        if polarity > 0.4:
            return 5

        elif polarity > 0.1:
            return 4

        elif polarity > -0.1:
            return 3

        elif polarity > -0.4:
            return 2

        else:
            return 1

    except:
        return 3



# 2. TRANSLATOR LOGIC
#
def universal_translator(text, index, total):

    try:

        if index % 50 == 0:
            print(f"🔄 Processing review {index} of {total}...")

        text_str = str(text)

        if pd.isna(text) or len(text_str) < 3:
            return text_str

        # Detect language
        lang = detect(text_str)

        # Translate only if not English
        if lang != 'en':

            return GoogleTranslator(
                source='auto',
                target='en'
            ).translate(text_str)

        return text_str

    except:
        return str(text)


# 3. MAIN PARSER

def run_kiko_parser():

    current_dir = os.path.dirname(os.path.abspath(__file__))

    yt_file = os.path.join(
        current_dir,
        '../../data/raw/kiko_youtube_raw.csv'
    )

    tp_file = os.path.join(
        current_dir,
        '../../data/raw/kiko_trustpilot_raw.xlsx'
    )

    output_file = os.path.join(
        current_dir,
        '../../data/processed/kiko_final_integrated.csv'
    )

    final_data = []

    
    # LOAD YOUTUBE DATA
   
    if os.path.exists(yt_file):

        print("Reading YouTube Data...")

        df_yt = pd.read_csv(yt_file)

        # Clean review text
        df_yt['review_text'] = (
            df_yt['review_text']
            .astype(str)
            .str.strip()
            .str.lower()
        )

        # Remove duplicates
        df_yt = df_yt.drop_duplicates(
            subset=['review_text']
        )

        print(f"✅ Unique YouTube Reviews: {len(df_yt)}")

        for _, row in df_yt.iterrows():

            final_data.append({

                'product': row.get(
                    'product_name',
                    'YouTube Product'
                ),

                'review_original': row.get(
                    'review_text',
                    ''
                ),

                'source': 'YouTube',

                'review_date': '',

                # YouTube has no real rating
                'original_rating': None
            })

   
    # LOAD TRUSTPILOT DATA
    
    if os.path.exists(tp_file):

        print("Reading Trustpilot Data...")

        df_tp = pd.read_excel(
            tp_file,
            engine='openpyxl'
        )

        # Clean review text
        df_tp['reviewDescription'] = (
            df_tp['reviewDescription']
            .astype(str)
            .str.strip()
            .str.lower()
        )

        # Remove duplicates
        df_tp = df_tp.drop_duplicates(
            subset=['reviewDescription']
        )

        print(f"Unique Trustpilot Reviews: {len(df_tp)}")

        for _, row in df_tp.iterrows():

            final_data.append({

                'product': 'Kiko Milano General',

                'review_original': row.get(
                    'reviewDescription',
                    ''
                ),

                'source': 'Trustpilot',

                'review_date': row.get(
                    'reviewDate',
                    ''
                ),

                # Use actual Trustpilot rating
                'original_rating': row.get(
                    'rating',
                    3
                )
            })

   
    # FINAL PROCESSING
   
    if final_data:

        df_final = pd.DataFrame(final_data)

        # Final text cleaning
        df_final['review_original'] = (
            df_final['review_original']
            .astype(str)
            .str.strip()
            .str.lower()
        )

        # Remove duplicates
        df_final = df_final.drop_duplicates(
            subset=['review_original']
        )

        print(
            f"✅ Final Unique Reviews: {len(df_final)}"
        )

        total_count = len(df_final)

        print(
            f"📊 Total {total_count} reviews found."
        )

        print("🚀 Starting NLP Pipeline...")

       
        # TRANSLATION
       
        translated_reviews = []

        for i, rev in enumerate(
            df_final['review_original']
        ):

            translated_reviews.append(
                universal_translator(
                    rev,
                    i,
                    total_count
                )
            )

        df_final['review_en'] = translated_reviews

    
        # FINAL RATING LOGIC
        
        final_ratings = []

        for _, row in df_final.iterrows():

            # Trustpilot → use real rating
            if row['source'] == 'Trustpilot':

                final_ratings.append(
                    row['original_rating']
                )

            # YouTube → infer sentiment
            else:

                final_ratings.append(
                    get_sentiment_rating(
                        row['review_en']
                    )
                )

        df_final['rating'] = final_ratings

        
        # DELETE OLD FILE
  
        if os.path.exists(output_file):

            os.remove(output_file)

            print(
                "🧹 Old integrated file deleted."
            )

        # Create output folder
        os.makedirs(
            os.path.dirname(output_file),
            exist_ok=True
        )

        # Save file
        df_final.to_csv(
            output_file,
            index=False,
            mode='w'
        )

        print(
            f"SUCCESS: Data saved at:\n{output_file}"
        )

        print(
            f"Final Row Count: {len(df_final)}"
        )

    else:

        print(
            "Error: Raw files missing or empty."
        )

# RUN

if __name__ == "__main__":
    run_kiko_parser()
