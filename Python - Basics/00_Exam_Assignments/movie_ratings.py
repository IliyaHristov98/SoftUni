number_of_movies = int(input())
best_movie = ''
best_movie_rating = 0
worst_movie = ''
worst_movie_rating = 10
total_rating = 0

for movie in range(number_of_movies):
    name = input()
    rating = float(input())
    total_rating += rating
    if rating > best_movie_rating:
        best_movie_rating = rating
        best_movie = name

    if rating < worst_movie_rating:
        worst_movie = name
        worst_movie_rating = rating

average_rating = total_rating / number_of_movies

print(f'{best_movie} is with highest rating: {best_movie_rating:.1f}\n'
      f'{worst_movie} is with lowest rating: {worst_movie_rating:.1f}\n'
      f'Average rating: {average_rating:.1f}')
