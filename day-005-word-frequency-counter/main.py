import re
from collections import Counter
def count_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        words = re.findall(r'\w+', text.lower())
        word_count = Counter(words)
        return word_count.most_common(10)

if __name__ == '__main__':
    try:
        file_path = input('Enter the path to the text file: ')
        result = count_words(file_path)
        print('\nTop 10 most common words:')
        for word, count in result:
            print(f'{word}: {count}')
    except FileNotFoundError:
        print('File not found. Please enter a valid path.')
