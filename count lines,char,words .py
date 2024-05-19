def count(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        word_count = len(text.split())
        character_count = len(text)
        line_count = text.count('\n') + 1  
    return word_count, character_count, line_count

file_path = 'example.txt'  
word_count, character_count, line_count = count(file_path)
print("Number of words:", word_count)
print("Number of characters:", character_count)
print("Number of lines:", line_count)
