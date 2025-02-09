# Moive-Reccomendation-System

# Movie Recommender System

## Overview
This project is a **Movie Recommender System** that suggests movies based on content similarity. It processes movie metadata, applies text-based similarity techniques, and uses **Cosine Similarity** to find and recommend similar movies.

## Features

### Data Wrangling & Preprocessing
- Cleans and organizes the movie dataset, handling missing values and merging relevant data (e.g., movies and credits datasets).
- Extracts key information such as cast, crew, genres, and plot summaries to create a structured dataset.

### Text-Based Similarity Matching
- Combines extracted movie details into a single descriptive tag for each movie.
- Uses these tags to compare movies based on their content.

### Vectorization with Count Vectorizer
- Converts text into numerical data using **Count Vectorization**, which creates word frequency representations.

### Global Word Frequency Analysis
- Processes a dataset of **4,806 movies** and extracts the **9,000 most frequently used words** to enhance comparison accuracy.

### Feature Representation
- Represents each movie as a **feature vector** in a high-dimensional space, facilitating mathematical comparisons.

### Cosine Similarity Calculation
- Measures the closeness of movies using **Cosine Similarity**, determining how similar two movies are based on their text data.

### Recommendation System
- When a user enters a movie title, the system finds and displays the **top 5 most similar movies** based on content analysis.

## Dataset
You can download the dataset from the link below:
[Download Dataset (TMDB_5000Movies.zip)](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

## Implementation

### Jupyter Notebook
- The **Movie Recommender System** was developed in **Jupyter Notebook** for data processing and feature extraction.
- The dataset was **cleaned, transformed, and vectorized** using **Count Vectorization**.
- **Cosine Similarity** was applied to compare movies, and a function was created to generate recommendations.
- **Exploratory Data Analysis (EDA)** and visualizations helped refine the recommendation process.
- Inline comments throughout the notebook explain the code and processes.

### VS Code
- **VS Code** was used to write, test, and run the **Streamlit-based Movie Recommender System**.
- It facilitated coding the **UI**, integrating the recommendation logic, and fetching movie posters via the **TMDb API**.
- Allowed smooth debugging, importing necessary libraries, and managing **pickle files** for storing movie data and similarity scores.

### Streamlit Web App
- **Streamlit** was used to build and deploy the interactive web app.
- Features a **user-friendly interface** with:
  - **Dropdown menu** for movie selection
  - **Button** to generate recommendations
  - **Columns** to display movie titles and posters
- Eliminates the need for complex web development, making it easy to use.

## Dependencies
To run this project, install the required libraries:
```bash
pip install pandas numpy scikit-learn streamlit pickle5 requests
```

## How to Run
1. Open Jupyter Notebook and execute the cells to preprocess data and generate similarity scores.
2. Run the Streamlit app using:
```bash
streamlit run app.py
```
3. Select a movie from the dropdown and get recommendations!

## Author
Developed by **Srividya Bobba**

## License
This project is licensed under the **MIT License**.
