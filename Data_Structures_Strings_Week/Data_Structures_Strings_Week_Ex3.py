#Exercise 3: Encapsulate this code in a function named count, and generalize it
#so that it accepts the string and the letter as arguments.

def count(word, letter):
    counted = 0
    for char in word:
        if char == letter:
            counted = counted + 1
    return counted

word_count = input('Enter word:')
letter_count = input('Enter letter:')
sift = count(word_count, letter_count)
print('Calculated:', sift)
