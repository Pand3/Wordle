def main():
    input_path = "Data/Word_source.txt" 
    output_path = "Data/Wordle_words.txt"
    valid_words = [] 

    with open(input_path, "r") as f:
        for line in f.readlines():
            word = line.strip() ## removes all the white space in the line
            if len(word) == 5:
                valid_words.append(word)
    
    with open(output_path, "w") as f:
        for words in valid_words:
            f.write(words + "\n") ## have to add new line as it has been stripped 
    
    print(f"You have {len(valid_words)} valid words in the data base")  
        
if __name__ == '__main__':
    main()
