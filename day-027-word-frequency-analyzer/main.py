def analyze_word_frequency(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read().lower()
        words = text.split()
        word_count = {}
        for word in words:
            if word.isalpha():
                word_count[word] = word_count.get(word, 0) + 1
        sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
        return sorted_word_count
    except FileNotFoundError:
        return 'File not found'
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    file_path = input('Enter the path to the text file: ')
    result = analyze_word_frequency(file_path)
    if isinstance(result, list):
        for word, count in result[:10]:
            print(f'{word}: {count}')
    else:
        print(result)
