from wordle_letter_postion import letter_colour

class wordle_log:
    
    MAX_WORDS = 6
    MAX_LETTERS = 5

    def __init__(self, secrete_word):
        self.secrete_word = secrete_word.upper()
        self.attempt = []
    
    ## checks if user inputted erroneous data
    def Notvalid(self, word):
        return len(word) != self.MAX_LETTERS    
    
    ## checks if user has found the secrete word 
    @property
    def solved(self):
        return self.attempt[-1].upper() == self.secrete_word
    
    ## checks if each character is in position or is in the secrete word 
    def feedback(self,word): # guess function
        word = word.upper() 
        result = []

        for char in range(self.MAX_LETTERS): ## loops through each letter 
            character = letter_colour(word[char]) ## character object for each letter 
            character.inWord = word[char] in self.secrete_word
            character.inPosition = word[char] == self.secrete_word[char]
            
            result.append(character)
        
        return result
    
    ## returns the ammount of guesses left 
    @property
    def remaining_guesses(self) -> int:
        return self.MAX_WORDS - len(self.attempt)
    
    ## checks if user has failed 
    @property
    def unsolved(self):
        return self.remaining_guesses == 0 and not self.solved
    
    
        
    
        
    