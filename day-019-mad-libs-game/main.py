def mad_libs():
    print("Welcome to the Mad Libs game!")
    nouns = input("Enter three nouns separated by commas: ").split(",")
    verbs = input("Enter two verbs separated by commas: ").split(",")
    adjectives = input("Enter four adjectives separated by commas: ").split(",")

    story = f"Once upon a time, there was a {adjectives[0]} {nouns[0]} who loved to {verbs[0]}. One day, they met a {adjectives[1]} {nouns[1]} and decided to go on an adventure together. They {verbs[1]} through the enchanted forest, climbed over {adjectives[2]} mountains, and found a {adjectives[3]} treasure at the end of their journey."

    print(story)

mad_libs()
