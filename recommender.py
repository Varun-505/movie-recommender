import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def load_data(movies_path="data/movies.csv", ratings_path="data/ratings.csv"):
    movies = pd.read_csv(movies_path, quotechar='"')
    ratings = pd.read_csv(ratings_path)
    return movies, ratings

def build_movie_similarity(movies, ratings, min_ratings=1):
    counts = ratings.groupby('movieId')['rating'].count()
    good_movies = counts[counts >= min_ratings].index
    movie_ratings = ratings[ratings['movieId'].isin(good_movies)]

    movie_matrix = movie_ratings.pivot_table(index='movieId', columns='userId', values='rating').fillna(0)

    if movie_matrix.shape[0] == 0:
        raise ValueError("No movies with enough ratings. Check your ratings.csv or lower min_ratings.")

    sim_matrix = cosine_similarity(movie_matrix.values)
    sim_df = pd.DataFrame(sim_matrix, index=movie_matrix.index, columns=movie_matrix.index)
    return sim_df, movie_matrix

def get_movie_recommendations(movie_title, movies, sim_df, top_n=5):
    movie_row = movies[movies['title'] == movie_title]
    if movie_row.empty:
        return []

    movie_id = movie_row['movieId'].values[0]

    if movie_id not in sim_df.index:
        return []

    scores = sim_df[movie_id].sort_values(ascending=False)
    top_ids = scores.index[scores.index != movie_id][:top_n]

    return movies[movies['movieId'].isin(top_ids)].to_dict('records')
