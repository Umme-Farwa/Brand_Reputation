import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_kiko_report():

    current_dir = os.path.dirname(os.path.abspath(__file__))

    file_path = os.path.join(
        current_dir,
        '..',
        '..',
        'data',
        'processed',
        'kiko_threat_report.csv'
    )

    # =========================================
    # CHECK FILE
    # =========================================
    if not os.path.exists(file_path):

        print(f"❌ Error: File not found! Path: {file_path}")
        return

    # =========================================
    # LOAD DATA
    # =========================================
    df = pd.read_csv(file_path)

    # =========================================
    # STYLE
    # =========================================
    sns.set_theme(style="whitegrid")

    fig = plt.figure(figsize=(16, 10))

    plt.subplots_adjust(
        hspace=0.4,
        wspace=0.4
    )

    fig.suptitle(
        "KIKO MILANO - REPUTATION THREAT ASSESSMENT",
        fontsize=22,
        fontweight='bold',
        color='#1a5276'
    )

    # =========================================
    # VISUAL 1 - DONUT CHART
    # =========================================
    plt.subplot(2, 2, 1)

    threat_counts = (
        df['threat_category']
        .value_counts()
    )

    colors = [
        '#2ecc71',
        '#e74c3c',
        '#3498db',
        '#9b59b6',
        '#f39c12',
        '#34495e'
    ]

    wedges, texts, autotexts = plt.pie(

        threat_counts,

        autopct='%1.1f%%',

        colors=colors[:len(threat_counts)],

        startangle=140,

        explode=[0.05] * len(threat_counts),

        shadow=True,

        pctdistance=1.2,

        textprops={
            'fontsize': 10,
            'fontweight': 'bold'
        }
    )

    # Donut effect
    centre_circle = plt.Circle(
        (0, 0),
        0.70,
        fc='white'
    )

    fig.gca().add_artist(centre_circle)

    # Legend
    plt.legend(
        wedges,
        threat_counts.index,
        title="Risk Categories",
        loc="center left",
        bbox_to_anchor=(1, 0, 0.5, 1),
        frameon=True
    )

    plt.title(
        "Distribution of Threats",
        fontsize=15,
        fontweight='bold',
        pad=25
    )

    # =========================================
    # VISUAL 2 - BAR CHART
    # =========================================
    plt.subplot(2, 2, 2)

    avg_rating = (
        df.groupby('source')['rating']
        .mean()
        .sort_values()
    )

    ax = sns.barplot(
        x=avg_rating.index,
        y=avg_rating.values,
        hue=avg_rating.index,
        palette="YlGnBu",
        legend=False
    )

    plt.title(
        "Average Sentiment Rating",
        fontsize=15,
        fontweight='bold'
    )

    plt.ylim(0, 5)

    # Value labels
    for p in ax.patches:

        ax.annotate(

            format(p.get_height(), '.2f'),

            (
                p.get_x() + p.get_width() / 2.,
                p.get_height()
            ),

            ha='center',

            va='center',

            xytext=(0, 10),

            textcoords='offset points',

            fontweight='bold'
        )

    # =========================================
    # VISUAL 3 - THREAT COMPARISON
    # =========================================
    plt.subplot(2, 1, 2)

    threats_only = df[
        df['threat_category']
        != 'Neutral/Positive'
    ]

    if not threats_only.empty:

        sns.countplot(

            data=threats_only,

            x='source',

            hue='threat_category',

            palette="muted"
        )

        plt.title(
            "Regional Risk Breakdown: YouTube vs Trustpilot",
            fontsize=15,
            fontweight='bold'
        )

        plt.legend(
            title="Risk Type",
            loc='upper right'
        )

    else:

        plt.text(
            0.5,
            0.5,
            "No specific risks detected.",
            ha='center',
            fontsize=14
        )

    # =========================================
    # FOOTER
    # =========================================
    footer = (
        f"Analyzed {len(df)} reviews | "
        f"Total Threats: {len(threats_only)}"
    )

    plt.figtext(

        0.5,

        0.02,

        footer,

        ha="center",

        fontsize=12,

        fontweight='bold',

        bbox={
            "facecolor": "#fcf3cf",
            "alpha": 0.8,
            "pad": 8
        }
    )

    # =========================================
    # CREATE REPORTS FOLDER
    # =========================================
    reports_dir = os.path.join(
        current_dir,
        '..',
        '..',
        'reports'
    )

    os.makedirs(
        reports_dir,
        exist_ok=True
    )

    # =========================================
    # SAVE REPORT
    # =========================================
    report_path = os.path.join(
        reports_dir,
        'kiko_reputation_report.png'
    )

    plt.savefig(
        report_path,
        dpi=300,
        bbox_inches='tight'
    )

    print(f"✅ Report saved at: {report_path}")

    print("✅ Report Displayed Successfully!")

    # =========================================
    # SHOW REPORT
    # =========================================
    plt.show()


# =========================================
# RUN
# =========================================
if __name__ == "__main__":
    generate_kiko_report()
