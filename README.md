# 🎬 Movie Recommender System

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=yellow)
![Streamlit](https://img.shields.io/badge/Streamlit-1.26-orange?logo=streamlit&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-green)

A simple, interactive **Movie Recommender System** built with **Python, Pandas, Scikit-learn, and Streamlit**.  
This project recommends movies to users based on **cosine similarity** of user ratings.

---

## 🔥 Features

- Interactive **web app** built with Streamlit
- **Content-based filtering** using cosine similarity
- Preloaded with **100 movies** and **1000 ratings**
- Provides **top 5 recommended movies** for any selected movie
- Easily extendable to more movies, users, or hybrid recommendation algorithms

---

## 🛠️ Skills & Technologies

- **Python** – core logic and data handling  
- **Pandas** – data manipulation and pivot tables  
- **NumPy** – numerical computations  
- **Scikit-learn** – cosine similarity  
- **Streamlit** – interactive web app deployment  
- **Git & GitHub** – version control and project publishing  
- **CSV data handling** – movie and ratings datasets

---

## 📸 Screenshots

**Main App Interface**

<img width="1856" height="988" alt="image" src="https://github.com/user-attachments/assets/ba958c71-104d-4008-a845-7efa017f542d" />

**Movie Recommendations**

<img width="1897" height="986" alt="image" src="https://github.com/user-attachments/assets/c58c1206-7202-4d3a-9dfb-7efa365d66d3" />

---

## 🚀 Deployment Instructions

### 1️⃣ Clone the repository

git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender

### 2️⃣ Set up Python environment

python -m venv venv
venv\Scripts\activate      # Windows
# or
source venv/bin/activate   # Mac/Linux

3️⃣ Install dependencies

pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

4️⃣ Generate the ratings CSV (if not already included)

python generate_ratings.py

5️⃣ Run the app

bash
streamlit run app.py


* Open the URL displayed in your browser (usually `http://localhost:8501`).
* Select a movie from the dropdown and click **Recommend**.
* See **top 5 recommended movies** with genres.

## 📂 Project Structure

movie-recommender/
├── app.py                 # Streamlit app
├── recommender.py         # Recommendation logic
├── generate_ratings.py    # Ratings CSV generator
├── requirements.txt       # Dependencies
├── README.md              # Project description
└── data/
    ├── movies.csv         # Movie dataset
    └── ratings.csv        # User ratings dataset

## ⚡ Future Improvements

* Add **user-based collaborative filtering**
* Deploy to **Streamlit Cloud or Heroku**
* Add **movie posters & trailers** to recommendations
* Extend dataset to **thousands of movies & users**

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

```
