import pandas as pd
import os
import re


# =========================================
# NEGATIVE CONTEXT WORDS
# =========================================
NEGATIONS = [
    "no",
    "not",
    "never",
    "without",
    "hardly",
    "none"
]


# =========================================
# THREAT PATTERNS
# =========================================
THREAT_PATTERNS = {

    "Health & Safety Threat": [
        "rash",
        "allergy",
        "allergic",
        "reaction",
        "burning",
        "itch",
        "itching",
        "redness",
        "pimples",
        "swelling",
        "skin irritation"
    ],

    "Fraud & Scam Threat": [
        "scam",
        "fake",
        "fraud",
        "stole",
        "stolen",
        "never arrived",
        "empty box",
        "counterfeit"
    ],

    "Product Quality Threat": [
        "broken",
        "dry",
        "bad quality",
        "waste of money",
        "patchy",
        "smell bad",
        "cheap quality",
        "damaged"
    ],

    "Customer Service Threat": [
        "rude support",
        "bad customer service",
        "ignored",
        "no response",
        "unhelpful"
    ],

    "Delivery Threat": [
        "late delivery",
        "never arrived",
        "delivery issue",
        "missing package",
        "wrong item"
    ]
}


# =========================================
# CONTEXTUAL THREAT DETECTION
# =========================================
def identify_threats(text):

    text = str(text).lower()

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    for category, keywords in THREAT_PATTERNS.items():

        for keyword in keywords:

            # Find keyword
            if keyword in text:

                # Check nearby words for negation
                keyword_position = text.find(keyword)

                start = max(0, keyword_position - 25)

                context_window = text[start:keyword_position]

                # Example:
                # "no allergy"
                # "not fake"

                if any(
                    neg in context_window
                    for neg in NEGATIONS
                ):

                    continue

                return category

    return "Neutral/Positive"


# =========================================
# MAIN DETECTOR
# =========================================
def run_threat_detector():

    current_dir = os.path.dirname(
        os.path.abspath(__file__)
    )

    input_file = os.path.join(
        current_dir,
        '../../data/processed/kiko_final_integrated.csv'
    )

    output_file = os.path.join(
        current_dir,
        '../../data/processed/kiko_threat_report.csv'
    )

    if not os.path.exists(input_file):

        print(
            "❌ Error: Integrated file not found!"
        )

        return

    # Load data
    df = pd.read_csv(input_file)

    print("🔍 Analyzing reviews for threats...")

    # Threat detection
    df['threat_category'] = (
        df['review_en']
        .apply(identify_threats)
    )

    # Threat count
    threat_count = df[
        df['threat_category']
        != 'Neutral/Positive'
    ].shape[0]

    # Save output
    df.to_csv(
        output_file,
        index=False,
        mode='w'
    )

    print(
        f"✅ SUCCESS: {threat_count} threats detected."
    )

    print(
        f"📁 Threat report saved at:\n{output_file}"
    )


# =========================================
# RUN
# =========================================
if __name__ == "__main__":
    run_threat_detector()
