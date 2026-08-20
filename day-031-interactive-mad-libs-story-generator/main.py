def get_user_input(prompt):
    return input(prompt)

def create_story(name, adjective, noun):
    return f'Once upon a time, there was a {adjective} {noun} named {name}. It lived in a magical land where...'

if __name__ == '__main__':
    try:
        name = get_user_input('Enter a name: ')
        adjective = get_user_input('Enter an adjective: ')
        noun = get_user_input('Enter a noun: ')
        story = create_story(name, adjective, noun)
        print(story)
    except Exception as e:
        print(f'Error: {e}')
