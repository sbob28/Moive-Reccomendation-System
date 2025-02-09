import pickle
import streamlit as st
import requests

# Function to fetch movie posters
def fetch_poster(movie_id):
    api_key = "7cff34c02011699bbc9c515dd295bde5"  # Replace with your actual TMDb API key
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    response = requests.get(url)
    data = response.json()
    
    if 'poster_path' in data and data['poster_path']:
        return f"https://image.tmdb.org/t/p/w500{data['poster_path']}"
    else:
        return "https://via.placeholder.com/500"  # Placeholder image if no poster is found

# Function to recommend movies
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]  # Fix incorrect comparison
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movies_name = []
    recommended_movies_poster = []

    for i in distances[1:6]:  # Skip the first one since it's the same movie
        movie_id = movies.iloc[i[0]]['movie_id']
        recommended_movies_name.append(movies.iloc[i[0]]['title'])  # Fix incorrect field
        recommended_movies_poster.append(fetch_poster(movie_id))

    return recommended_movies_name, recommended_movies_poster

# Streamlit UI
st.header("Movies Recommendation System Using Machine Learning")

# Load movie data
movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))

# Dropdown for movie selection
movie_list = movies['title'].values
selected_movie = st.selectbox('Type a movie name to get a recommendation', movie_list)

if st.button('Show Recommendations'):
    recommended_movies_name, recommended_movies_poster = recommend(selected_movie)

    # Display recommendations in columns
    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.text(recommended_movies_name[i])
            st.image(recommended_movies_poster[i])
