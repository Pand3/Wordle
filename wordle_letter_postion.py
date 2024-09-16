

class letter_colour:
    def __init__(self, char:str):
        self.char: str = char
        self.inPosition: bool = False
        self.inWord: bool = False
        
    def __repr__(self):
        return f"[{self.char} is in word:{self.inWord} is in position:{self.inPosition}]"
        
    