def count(file_path):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    vowel_count = 0
    consonant_count = 0
    
    with open(file_path, 'r') as file:
        text = file.read()
        for char in text:
            if char.isalpha():
                if char in vowels:
                    vowel_count += 1
                elif char in consonants:
                    consonant_count += 1

    return vowel_count, consonant_count

file_path = 'example.txt' 
vowel_count, consonant_count = count(file_path)
print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)
