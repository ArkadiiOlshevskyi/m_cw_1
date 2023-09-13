'''
Sentence Smash
Write a function that takes an array of words and smashes
them together into a sentence and returns the sentence.
You can ignore any need to sanitize words or add punctuation,
but you should add spaces between each word. Be careful,
there shouldn't be a space at the beginning or the end of the sentence!

Example
['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'

'''

# example 1
# def smash(words):
#     words_2 = ' '
#     for w in words:
#         words_2 += w + ' '
#     return words_2.strip()


# example 2
def smash(words):
    return ' '.join(words)


if __name__ == '__main__':
    words = ['hello', 'world', 'this', 'is', 'great']
    smash(words)
    print(smash(words))
