import sys
from collections import Counter

def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            word_count = Counter(words)
            return word_count
    except FileNotFoundError:
        print(f'File {file_path} not found. Please check the path and try again.')
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python word_frequency_analyzer.py <text_file>')
        sys.exit(1)

    file_path = sys.argv[1]
    word_count = count_words(file_path)
    for word, count in word_count.most_common():
        print(f'{word}: {count}')
