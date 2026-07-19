import streamlit as st
import pickle
import joblib

st.title("Movie Recommendation System")

with open("movies.pickle", "rb") as f:
    movies = pickle.load(f)

similarities = joblib.load("similarities.joblib")

movie_name = st.selectbox(
    "Enter a movie name",
    movies["title"].values
)

def recommend(movie_name):
    movie_index = movies[movies["title"] == movie_name].index[0]

    recommendations = similarities[movie_index]

    movie_list = sorted(
        enumerate(recommendations),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


if st.button("Recommend"):
    st.write("### Recommended Movies")

    r = recommend(movie_name)

    for movie in r:
        st.write(movie)