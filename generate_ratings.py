import csv
import random
import os

os.makedirs("data", exist_ok=True)

num_users = 10
num_movies = 100

with open("data/ratings.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["userId", "movieId", "rating", "timestamp"])
    ts = 978300000
    for user in range(1, num_users+1):
        for movie in range(1, num_movies+1):
            rating = round(random.uniform(1, 5), 1)
            writer.writerow([user, movie, rating, ts])
            ts += 1

print("ratings.csv generated successfully in data/")
