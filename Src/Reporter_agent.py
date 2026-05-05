import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_report(summary_path):
    print(f"Generating visual report from: {summary_path}")
    df = pd.read_csv(summary_path)
    
    # only top 10 products for clear visualization
    top_threats = df.head(10)
    
    # Graph size and style
    plt.figure(figsize=(12, 6))
    sns.set_theme(style="whitegrid")
    
    # Bar Plot
    ax = sns.barplot(x='threat_count', y='product_name', data=top_threats, palette='Reds_r')
    
    # Labels and Title (According to roadmap metrics)
    plt.title('Top Products with High-Risk Reputational Threats', fontsize=16)
    plt.xlabel('Number of High-Risk Mentions', fontsize=12)
    plt.ylabel('Product Name', fontsize=12)
    
    #Writing count on each bar
    for i in ax.containers:
        ax.bar_label(i,)
    
    #Saving Report
    report_dir = "data/reports"
    os.makedirs(report_dir, exist_ok=True)
    report_path = os.path.join(report_dir, "threat_visualization.png")
    plt.tight_layout()
    plt.savefig(report_path)
    
    print(f"Visual report saved to: {report_path}")
    plt.show()

if __name__ == "__main__":
    #using summary that we created in threat_detector_agent for the report
    summary_file = "data/processed/threat_report_summary.csv"
    generate_report(summary_file)