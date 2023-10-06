import random
import time

# List of words for the typing test
word_list = [
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape",
    "honeydew", "kiwi", "lemon", "mango", "orange", "papaya", "quince",
    "raspberry", "strawberry", "tangerine", "watermelon"
]

# Function to generate a random word
def get_random_word():
    return random.choice(word_list)

# Function to conduct the typing test
def typing_test():
    print("Welcome to the Speed Typing Test!")
    input("Press Enter to start...")
    
    start_time = time.time()
    correct_words = 0
    
    while True:
        target_word = get_random_word()
        print(f"Type this word: {target_word}")
        
        user_input = input("Your input: ")
        
        if user_input == target_word:
            correct_words += 1
        
        elapsed_time = time.time() - start_time
        
        print(f"Time elapsed: {elapsed_time:.2f} seconds")
        print(f"Words correct: {correct_words}")
        
        more = input("Do you want to continue? (y/n): ").lower()
        if more != 'y':
            break
    
    print(f"Test complete! You typed {correct_words} words correctly in {elapsed_time:.2f} seconds.")

# Start the typing test
typing_test()
