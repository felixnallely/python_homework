#Task 4: 
def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter.lower())

        display = ""
        for char in secret_word: 
            if char.lower() in guesses:
                display += char
            else:
                display += "_"
        print(display)

        for char in secret_word: 
            if char not in guesses: 
                return False
            else: 
                return True 
    return hangman_closure 

if __name__ == "__main__":
    word = input("Enter secret word: ").lower()
    hangman = make_hangman(word)

    print("\nLet us play Hangman!")
    print("_" * len(word))
    
    while True:
        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1:
            print("Enter one letter only.")
            continue

        done = hangman(guess)

        if done:
            print("You guessed the secret word!")
            break