import json
import random

MOVIES = {
    'action': ['Inception', 'Mad Max', 'Die Hard'],
    'comedy': ['Air Bud', 'Superbad', 'Planes Trains and Automobiles'],
    'drama': ['The Shawshank Redemption', 'The Godfather', 'Pulp Fiction'],
    'fantasy': ['The Lord of the Rings', 'Harry Potter', 'The Chronicles of Narnia'],
    'horror': ['The Exorcist', 'Get Out', 'Hereditary'],
    'sci-fi': ['Interstellar', 'The Matrix', 'Eternal Sunshine of the Spotless Mind'],
    'thriller': ['The Girl with the Dragon Tattoo', 'Snoop Dogg', 'The Dark Knight']
}

def get_recommendations(preferences):
    recommendations = []
    for genre, movies in MOVIES.items():
        if genre in preferences:
            recommendations.extend(random.sample(movies, min(3, len(movies))))
    return recommendations

def main():
    print('Welcome to the Movie Recommendation System!')
    preferences = input('Enter your movie genres (comma-separated): ').split(', ')
    try:
        recommendations = get_recommendations(preferences)
        print('Recommended Movies:')
        for i, movie in enumerate(recommendations, 1):
            print(f'{i}. {movie}')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()
