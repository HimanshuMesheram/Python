import json
import os

class MovieTracker:
    FILE_NAME = "movies.json"

    def __init__(self):
        self.initialize_file()

    def menu(self):
        while True:
            print("\n--- MOVIE TRACKER ---")
            print("1. Add Movie")
            print("2. View All Movies")
            print("3. Search Movie")
            print("4. Exit")

            choice = input("Enter choice: ").strip()

            if choice == '1':
                self.add_movie()
            elif choice == '2':
                self.view_movies()
            elif choice == '3':
                self.search_movies()
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid choice!")

    def initialize_file(self):
        if not os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, 'w') as file:
                json.dump([], file)

    def read_movies(self):
        with open(self.FILE_NAME, 'r') as file:
            return json.load(file)

    def write_movies(self, movies):
        with open(self.FILE_NAME, 'w') as file:
            json.dump(movies, file, indent=4)

    def add_movie(self):
        movies = self.read_movies()
        title = input("Enter Title: ").strip()

        for movie in movies:
            if movie["Title"].lower() == title.lower():
                print("Movie already exists!")
                return

        genre = input("Enter Genre: ").strip()

        try:
            rating = float(input("Enter Rating (out of 10): "))
            if rating < 0 or rating > 10:
                print("Rating must be between 0 and 10.")
                return
        except ValueError:
            print("Invalid rating!")
            return

        movies.append({
            "Title": title,
            "Genre": genre,
            "Rating": rating
        })

        self.write_movies(movies)
        print("Movie added successfully!")

    # View all movies (table format)
    def view_movies(self):
        movies = self.read_movies()

        if not movies:
            print("No movies found.")
            return

        print("\n" + "="*60)
        print(f"{'Title':<20}{'Genre':<20}{'Rating':<10}")
        print("="*60)

        for movie in movies:
            print(f"{movie['Title']:<20}{movie['Genre']:<20}{movie['Rating']:<10}")

        print("="*60)

    # Search movies (by title or genre, partial match)
    def search_movies(self):
        keyword = input("Enter title/genre to search: ").strip().lower()
        movies = self.read_movies()

        results = [
            m for m in movies
            if keyword in m["Title"].lower() or keyword in m["Genre"].lower()
        ]

        if not results:
            print("No matching movies found.")
            return

        print("\nSearch Results:")
        print("="*60)
        print(f"{'Title':<20}{'Genre':<20}{'Rating':<10}")
        print("="*60)

        for movie in results:
            print(f"{movie['Title']:<20}{movie['Genre']:<20}{movie['Rating']:<10}")

        print("="*60)

    
mt = MovieTracker()
mt.menu()