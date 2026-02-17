fav_movies = ["The Shawshank Redemption", "The Godfather", "The Dark Knight", "Pulp Fiction"]
print("My favorite movies are:")
for movie in fav_movies:
    print(movie)
fav_movies.append("Inception")
print("\nAfter adding a new movie:")
for movie in fav_movies:
    print(movie)
fav_movies.insert(2, "The Matrix")
print("\nAfter inserting a movie at index 2:")  
for movie in fav_movies:
    print(movie)
del fav_movies[1]
print("\nAfter deleting the movie at index 1:")
for movie in fav_movies:
    print(movie)