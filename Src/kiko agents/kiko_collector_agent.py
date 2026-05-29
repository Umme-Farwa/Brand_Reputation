import pandas as pd
from googleapiclient.discovery import build
import os

def collect_kiko_youtube(api_key, query, max_videos=5):
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Search request
    search_req = youtube.search().list(
        q=query,
        part="snippet",
        type="video",
        maxResults=max_videos
    ).execute()

    all_comments = []

    for item in search_req['items']:
        v_id = item['id']['videoId']
        v_title = item['snippet']['title']

        try:
            # Fetch comments
            comments_req = youtube.commentThreads().list(
                part="snippet",
                videoId=v_id,
                maxResults=20,
                textFormat="plainText"
            ).execute()

            for c in comments_req['items']:
                text = c['snippet']['topLevelComment']['snippet']['textDisplay']

                all_comments.append({
                    'product_name': v_title,
                    'review_text': text,
                    'rating': 3,
                    'source': 'YouTube'
                })

        except Exception as e:
            print(f"Error fetching comments: {e}")
            continue

    # Create DataFrame
    df = pd.DataFrame(all_comments)

    # ✅ REMOVE DUPLICATES
    df['review_text'] = (
        df['review_text']
        .astype(str)
        .str.strip()
        .str.lower()
    )

    df = df.drop_duplicates(subset=['review_text'])

    # Output folder
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(
        current_dir,
        '..',
        '..',
        'data', 
        'raw',
        'kiko_youtube_raw.csv'
    )
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # ✅ OVERWRITE OLD FILE
    df.to_csv(file_path, index=False, mode='w')

    print(f"SUCCESS: {len(df)} unique reviews saved at {file_path}")


if __name__ == "__main__":
    MY_KEY = "YOUR_ACTUAL_API_KEY_HERE"
    collect_kiko_youtube(MY_KEY, "Kiko Milano reviews skin reaction")

