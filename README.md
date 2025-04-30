# Gender & Movie Success: Do Female Directors Get a Fair Shot?

This project explores whether the gender of a movie's director has any measurable impact on how successful the film is — both critically and commercially. I focused on three main indicators of success: box office gross, IMDb audience rating, and Rotten Tomatoes critic score. The goal was to see if female-directed films perform differently from male-directed ones, and whether any patterns emerge in how these movies are received.

---

## Data Sources

| Source | Description | Used For |
|--------|-------------|----------|
| [Kaggle IMDb Top 1000 Movies Dataset](https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows) | Contains metadata on the top 1000 IMDb-rated movies, including gross revenue, IMDb rating, director, and cast | Baseline movie data, Gross, IMDb Rating |
| [Genderize API](https://genderize.io/) | Predicts gender based on first names | Used to determine the gender of each director |
| [OMDb API](https://www.omdbapi.com/) | Public movie database API that provides critic and audience ratings, including Rotten Tomatoes scores | Used to fetch Rotten Tomatoes Scores per movie |

---

## Analysis

After cleaning the Kaggle dataset and filtering out movies with missing Rotten Tomatoes scores, I used the Genderize API to identify the gender of each film’s director. Then, I compared male- vs. female-directed movies across:

- **Average Gross Revenue**
- **Average IMDb Rating**
- **Average Rotten Tomatoes Score**

I also explored distributional differences using boxplots and histograms to visualize spread, medians, and outliers for each metric by gender. Finally, I created a grouped summary chart to compare all three metrics side-by-side.

---

## Summary of Results

- **Gross**: On average, male-directed movies had higher box office revenue, but female-directed films showed notable success in many cases.
- **IMDb + RT Scores**: Ratings between male- and female-directed films were comparable, and in some cases, female-directed films were rated slightly higher on average.
- **Representation**: Female directors were significantly underrepresented in the dataset, highlighting an ongoing gap in opportunity.

---

## How to Run This Project

To reproduce the full pipeline and analysis:

### Setup

To run this project and reproduce the full analysis, follow these steps:

1. **Download or clone the repository.**

2. **Install Python and all required libraries** listed in `requirements.txt`. These include libraries like `pandas`, `matplotlib`, `seaborn`, `requests`, and `python-dotenv`.

3. **Create a `.env` file** in the root of the repository. This file will store the API keys required to run the pipeline. Add the following lines to your `.env` file (with your actual credentials):

>  **Do not include your API keys in the repository.** This `.env` file is used securely to keep them private.

4. **Open and run the notebook file: `results.ipynb`**

Once your `.env` file is set up, open `results.ipynb` and run all the cells from top to bottom. The notebook will:
- Load and clean the movie data
- Use the Genderize API to determine director gender
- Use the OMDb API to fetch Rotten Tomatoes scores
- Generate all visualizations used in the analysis

All functional code lives in the `src/` folder. The notebook simply calls those functions, so you do not need to edit or run any `.py` files directly.



