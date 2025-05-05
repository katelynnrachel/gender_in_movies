import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

gender_colors = {
    'male': '#1f77b4', 
    'female': '#e377c2'    
}

def plot_gross_by_gender(df):
    plt.figure(figsize=(8, 6))
    sns.barplot(data=df, x='Director_Gender', y='Gross', hue='Director_Gender', palette=gender_colors, legend=False)
    plt.legend().remove()
    plt.title('Average Gross Earnings by Director Gender')
    plt.xlabel('Director Gender')
    plt.ylabel('Average Gross ($)')
    plt.tight_layout()
    plt.show()

def plot_imdb_by_gender(df):
    plt.figure(figsize=(8, 6))
    sns.barplot(data=df, x='Director_Gender', y='IMDB_Rating', hue='Director_Gender', palette=gender_colors, legend=False)
    plt.legend().remove()
    plt.title('Average IMDb Rating by Director Gender')
    plt.xlabel('Director Gender')
    plt.ylabel('Average IMDb Rating')
    plt.tight_layout()
    plt.show()

def plot_boxplot_gross_by_gender(df):
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df, x='Director_Gender', y='Gross', palette=gender_colors)
    plt.title('Distribution of Gross Revenue by Director Gender')
    plt.xlabel('Director Gender')
    plt.ylabel('Gross Revenue ($)')
    plt.tight_layout()
    plt.show()

def plot_rotten_tomatoes_by_gender(df):
    plt.figure(figsize=(8, 6))
    sns.barplot(data=df, x='Director_Gender', y='Rotten_Tomatoes_Score', hue='Director_Gender', palette=gender_colors, legend=False)
    plt.legend().remove()
    plt.title('Average Rotten Tomatoes Score by Director Gender')
    plt.xlabel('Director Gender')
    plt.ylabel('Average Rotten Tomatoes Score (%)')
    plt.tight_layout()
    plt.show()

def plot_boxplot_imdb_by_gender(df):
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df, x='Director_Gender', y='IMDB_Rating', palette=gender_colors)
    plt.title('Distribution of IMDb Ratings by Director Gender')
    plt.xlabel('Director Gender')
    plt.ylabel('IMDb Rating')
    plt.tight_layout()
    plt.show()

def plot_hist_rt_scores(df):
    plt.figure(figsize=(8, 6))
    sns.histplot(data=df, x='Rotten_Tomatoes_Score', hue='Director_Gender', bins=20, kde=True, palette=gender_colors)
    plt.title('Distribution of Rotten Tomatoes Scores By Gender Director')
    plt.xlabel('Rotten Tomatoes Score (%)')
    plt.ylabel('Number of Movies')
    plt.tight_layout()
    plt.show()

def plot_scatter_imdb_vs_gross(df):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x='IMDB_Rating', y='Gross', hue='Director_Gender', palette=gender_colors, alpha=0.6)
    plt.title('IMDb Rating vs Gross Revenue by Director Gender')
    plt.xlabel('IMDb Rating')
    plt.ylabel('Gross ($)')
    plt.tight_layout()
    plt.show()