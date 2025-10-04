import streamlit as st
from recommender import load_data, build_movie_similarity, get_movie_recommendations

st.title("Movie Recommender System")

movies, ratings = load_data()
sim_df, movie_matrix = build_movie_similarity(movies, ratings, min_ratings=1)

movie_list = movies['title'].tolist()
selected_movie = st.selectbox("Select a movie", movie_list)

if st.button("Recommend"):
    recommendations = get_movie_recommendations(selected_movie, movies, sim_df)
    if not recommendations:
        st.write("No recommendations found.")
    else:
        st.write("### Recommended Movies:")
        for rec in recommendations:
            st.write(f"**{rec['title']}** - {rec['genres']}")
