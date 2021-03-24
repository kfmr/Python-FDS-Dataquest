# Calculate the lenght of the strings from the words list
words = ['tissue', 'psychology', 'blind', 'assessment', 'dynamic', 'hero', 'circulation', 'merchant', 'publication', 'interference', 'show', 'joy', 'sour', 'aloof', 'grass', 'distortion', 'exclude', 'pressure', 'bullet', 'calf']

word_len = []

for word in words:
    word = len(word)
    word_len.append(word)

print(word_len)