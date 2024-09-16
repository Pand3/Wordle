from Wordle_logic import wordle_log
from colorama import Fore
from typing import List
from wordle_letter_postion import letter_colour
import random 

def main():
    wordle_words = load_words("Data/Wordle_words.txt")
    secret_word = random.choice(list(wordle_words))
    wordle = wordle_log(secret_word)
    
    while wordle.remaining_guesses: #can still attempt to guess 
        user_guess = str(input("\nGuess: "))
        
        if wordle.Notvalid(user_guess): ## ensure word is 5 letters 
            print(Fore.RED +f"\nWord has to be {wordle.MAX_LETTERS} letters" + Fore.RESET)
            continue 
        
        if not user_guess.upper() in wordle_words:
            print(Fore.RED+"\nThis is not a valid word, try again!"+Fore.RESET)
            continue
        
        ## adds attempt to the attempt string 
        wordle.attempt.append(user_guess)
        display_results(wordle)
        # result = wordle.feedback(user_guess)
        # print(*result, sep = '\n')
        
        if wordle.solved:
            print(Fore.GREEN + "\nYou win!" + Fore.RESET)
            break
    
    if wordle.unsolved:
        print(Fore.RED +"You lose!"+ Fore.RESET)
        print(Fore.RED+f"\nThe secrete word is {Fore.GREEN+wordle.secrete_word+ Fore.RESET}")
        
def load_words(file: str):
    word_set = set()
    with open(file, 'r') as f:
        for lines in f.readlines():
            words = lines.strip().upper()
            word_set.add(words)
    return word_set 
    
def display_results(wordle: wordle_log):
    lines = []
    print(f"\nYou have {wordle.remaining_guesses} remaining guesses\n")
    for word in wordle.attempt: ## goes through each word in the attempt
        result = wordle.feedback(word)
        coloured_result = convert_to_col(result)
        lines.append(coloured_result)
    
    ## prints out empty lines 
    for _ in range(wordle.remaining_guesses):
        lines.append(" ".join(('_' * wordle.MAX_LETTERS)))
    
    display_border(lines)


def convert_to_col(result: List[letter_colour]):
    result_with_col = []
    for letter in result:
        if letter.inPosition:
            colour = Fore.GREEN
            
        elif letter.inWord:
            colour = Fore.YELLOW
            
        else:
            colour = Fore.WHITE
            
        coloured_letter = colour + letter.char + Fore.RESET 
        result_with_col.append(coloured_letter)
    return " ".join(result_with_col)
    
def display_border(lines: List[str], size: int = 9, padding: int = 1):
    
    content_length = size + padding * 2 
    top_boarder = "┌" + "─" * content_length + "┐"
    bottom_boarder = "└" + "─" * content_length + "┘" 
    space = " " * padding 
    
    print(top_boarder)
    for line in lines:
        print("│"+ space + line + space + "│")
    print(bottom_boarder)
    
    
if __name__ == "__main__":
    main()